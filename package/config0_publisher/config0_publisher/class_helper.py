#!/usr/bin/env python

import logging
import re
import os
import boto3
import gzip
from io import BytesIO
from time import sleep
from time import time

from config0_publisher.loggerly import Config0Logger

class SetClassVarsHelper:
    """
    This class is used to set class variables based on different sources.
    The sources are:
    1. kwargs: a dictionary of key-value pairs
    2. env_vars: a dictionary of environment variables
    3. set_env_vars: a dictionary of key-value pairs, where the value is a boolean indicating whether the variable is required or not. If the variable is required and is not found in any of the sources, an exception will be raised.
    4. set_default_null: a boolean indicating whether to set the variables to None if they are not found in any of the sources.

    The variables are set using the exec function, which allows for dynamic variable creation.
    """

    def __init__(self,set_env_vars=None,kwargs=None,env_vars=None,set_default_null=None):
        """
        Args:
            set_env_vars (dict, optional): A dictionary of key-value pairs indicating the required variables and whether they are required. If a variable is required and is not found in any of the sources, an exception will be raised.
            kwargs (dict, optional): A dictionary of key-value pairs to be used as the source of the variables.
            env_vars (dict, optional): A dictionary of environment variables to be used as the source of the variables.
            set_default_null (bool, optional): A boolean indicating whether to set the variables to None if they are not found in any of the sources.
        """
        if set_env_vars:
            self.set_env_vars = set_env_vars
        else:
            self.set_env_vars = None

        self.kwargs = kwargs

        self.env_vars = env_vars

        if not self.env_vars:
            self.env_vars = {}

        self.set_default_null = set_default_null

    def set_class_vars_srcs(self):
        """
        This function sets the class variables based on the sources defined in the constructor.
        """
        if not self.set_env_vars:
            return

        for env_var,must_exists in self.set_env_vars.items():

            if env_var in self.kwargs:
                exec('self.{}="{}"'.format(env_var,
                                         self.kwargs[env_var]))
                continue

            if env_var.upper() in self.env_vars:
                exec('self.{}="{}"'.format(env_var,
                                           self.env_vars[env_var.upper()]))
                continue

            if must_exists:
                raise Exception("variable {} needs to be set".format(env_var))

            if self.set_default_null:
                self.logger.debug("set None for variable {}".format(env_var))
                exec('self.{}=None'.format(env_var))
