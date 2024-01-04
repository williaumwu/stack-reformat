#!/usr/bin/env python
#
#Project: config0-helper: Config0 is a SaaS for building and managing 
#software and DevOps automation. This particular packages is a python
#helper for publishing stacks, hostgroups, shellouts/scripts and other
#assets used for automation
#
#Examples include cloud infrastructure, CI/CD, and data analytics
#
#Copyright (C) Gary Leong - All Rights Reserved
#Unauthorized copying of this file, via any medium is strictly prohibited
#Proprietary and confidential
#Written by Gary Leong  <gary@config0.com, May 11,2022

import os
import json

from config0_publisher.loggerly import Config0Logger
from config0_publisher.utilities import OnDiskTmpDir
from config0_publisher.resource_manage import ResourceCmdHelper
from config0_publisher.utilities import to_json

class AwsCli(ResourceCmdHelper):
    """
    This class provides a helper for interacting with the AWS CLI.

    Args:
        app_name (str): The name of the application.

    Attributes:
        classname (str): The name of the class.
        logger (Config0Logger): A logger for the class.
        file_config (dict): A dictionary of configuration options.
        file_config_loc (str): The location of the configuration file.
        tempdir (OnDiskTmpDir): A temporary directory object.
        resource_tags_keys (list): A list of resource tag keys.

    """

    def __init__(self,**kwargs):

        ResourceCmdHelper.__init__(self,
                                   app_name="awscli")

        self.classname = 'AwsCli'
        self.logger = Config0Logger(self.classname)

        # fixfix777
        self.logger.debug("Instantiating %s" % self.classname)
        self.file_config = None
        self.file_config_loc = None
        self.tempdir = None
        self.resource_tags_keys = [ "name", 
                                    "schedule_id", 
                                    "job_instance_id",
                                    "job_id" ]

    def get_tags(self):
        """
        This function returns a list of tags to be applied to the resource.

        Returns:
            list: A list of tags.
        """

        tags = [ self.aws_default_region, 
                 self.product, 
                 self.provider ]

        for key_eval in self.resource_tags_keys:

            if not self.inputargs.get(key_eval): 
                continue
            
            tags.append(self.inputargs[key_eval])

        return tags

    def set_ondisktmp(self):
        """
        Sets the temporary directory object.

        Returns:
            None
        """
        self.tempdir = OnDiskTmpDir()

    def write_file_config(self):
        """
        Writes the file configuration to a file.

        Args:
            None

        Returns:
            None
        """

        with open(self.file_config_loc, 'w') as _file:
            _file.write(json.dumps(self.file_config,
                                   indent=4))

    def _get_add_tags(self):
        """
        This function attempts to convert the input argument "tags" to JSON. If the conversion is successful, the function returns the JSON object. If the conversion fails, or if the "tags" argument is not provided, the function returns None.

        Returns:
            dict: The JSON object, or None if the conversion fails or if the "tags" argument is not provided.
        """

        try:
            add_tags = to_json(self.inputargs.get("tags"))
        except:
            add_tags = None

        if not add_tags: return 
  
        return add_tags

    def get_resource_tags(self,**kwargs):
        """
        This function returns a list of tags to be applied to the resource.

        Args:
            kwargs (dict): A dictionary of keyword arguments.

        Returns:
            list: A list of tags.
        """

        name = kwargs.get("name")
        if not name: name = self.inputargs.get("name")
        
        tags = "["
        if name: tags = tags + "{"+"Key={},Value={}".format("Name",name)+"}"
        
        for key_eval in self.resource_tags_keys:

            if not self.inputargs.get(key_eval): 
                continue

            tags = tags + ",{"+"Key={},Value={}".format(key_eval,
                                                        self.inputargs[key_eval])+"}"

        add_tags = self._get_add_tags()

        if not add_tags:
            tags = tags + "]"
            return tags

        for _k,_v in add_tags.items():
            tags = tags + ",{"+"Key={},Value={}".format(_k,_v)+"}"

        tags = tags + "]"

        return tags

    def get_cmd_region(self,cmd):

        return "{} --region {}".format(cmd,
                                       self.aws_default_region)

    def get_region(self):
        """
        Sets the AWS region to be used by the AWS CLI.

        The AWS region can be set using the "aws_default_region" input argument. If the input argument is not provided, the default region is set to "us-east-1". If the input argument is set to "None", the default region is set to "us-east-1".

        Args:
            None

        Returns:
            None
        """

        self.aws_default_region = self.inputargs.get("aws_default_region")

        if not self.aws_default_region:
            self.aws_default_region = "us-east-1"

        if self.aws_default_region == "None": 
            self.aws_default_region = "us-east-1"

        self.logger.debug('Region set to "{}"'.format(self.aws_default_region))
