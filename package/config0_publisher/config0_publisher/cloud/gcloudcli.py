#!/usr/bin/env python
#
#Project: config0_publisher: Config0 is a SaaS for building and managing
#software and DevOps automation. This particular packages is a python
#helper for publishing stacks, hostgroups, shellouts/scripts and other
#assets used for automation
#
#Examples include cloud infrastructure, CI/CD, and data analytics
#
#Copyright (C) Gary Leong - All Rights Reserved
#Unauthorized copying of this file, via any medium is strictly prohibited
#Proprietary and confidential
#Written by Gary Leong  <gary@config0.com, May 11,2020

import os
import json
from time import sleep

from config0_publisher.loggerly import Config0Logger
from config0_publisher.utilities import OnDiskTmpDir
from config0_publisher.resource_manage import ResourceCmdHelper
from config0_publisher.utilities import id_generator


class GcloudCli(ResourceCmdHelper):
    """
    This class provides a helper for interacting with the gcloud command line interface.

    Args:
        app_name (str): The name of the application.

    Attributes:
        classname (str): The name of the class.
        logger (Config0Logger): A logger for the class.
        file_config (dict): A dictionary of file configuration.
        file_config_loc (str): The location of the file configuration.
        tempdir (OnDiskTmpDir): A temporary directory for the class.
        resource_tags_keys (list): A list of resource tag keys.
        share_dir (str): The shared directory.
        stateful_dir (str): The stateful directory.
        docker_image (str): The docker image.
        output (list): A list of output.
    """

    def __init__(self,**kwargs):

        ResourceCmdHelper.__init__(self,
                                   app_name="gcloudcli")

        self.classname = 'GcloudCli'
        self.logger = Config0Logger(self.classname)
        # fixfix777
        self.logger.debug("Instantiating %s" % self.classname)
        self.file_config = None
        self.file_config_loc = None
        self.tempdir = None
        self.resource_tags_keys = [ "tags", 
                                    "name", 
                                    "schedule_id", 
                                    "job_instance_id",
                                    "job_id" ]

        self.share_dir = os.environ.get("SHARE_DIR",
                                        "/var/tmp/share")

        self.stateful_dir = os.path.join(self.share_dir,
                                         id_generator(8))

        self.docker_image = "google/cloud-sdk"
        self.output = []

    def get_tags(self):
        """
        This function returns a list of tags to be applied to the resource.

        The tags are constructed by concatenating the following values:
            - gcloud_region
            - product
            - provider
            - values of resource_tags_keys if present in the inputargs

        Args:
            None

        Returns:
            list: A list of tags to be applied to the resource.
        """

        tags = [ self.gcloud_region, 
                 self.product, 
                 self.provider ]

        for key_eval in self.resource_tags_keys:
            if not self.inputargs.get(key_eval): continue
            tags.append(self.inputargs[key_eval])

        return tags

    def set_ondisktmp(self):
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

    def parse_set_env_vars(self,env_vars,upper_case=True):
        """
        This function sets the inputargs based on the environment variables.

        Args:
            env_vars (list): A list of environment variables.
            upper_case (bool, optional): A boolean indicating whether the environment variables are in upper case. Defaults to True.

        Returns:
            None
        """

        self.inputargs = {}

        for env_var in env_vars:

            if not os.environ.get(env_var.upper()):
                continue

            if env_var == "gcloud_region":
                self.inputargs["gcloud_region"] = os.environ[env_var.upper()]
            else:
                self.inputargs[env_var] = os.environ[env_var.upper()]

    def get_resource_tags(self,**kwargs):
        """
        This function returns a list of tags to be applied to the resource.

        The tags are constructed by concatenating the following values:
            - gcloud_region
            - product
            - provider
            - values of resource_tags_keys if present in the inputargs

        Args:
            kwargs (dict): A dictionary of keyword arguments.

        Returns:
            list: A list of tags to be applied to the resource.
        """

        name = kwargs.get("name")
        if not name: name = self.inputargs.get("name")
        
        tags = "["

        if name: 
            tags = tags + "{"+"Key={},Value={}".format("Name",
                                                       name)+"}"
        
        for key_eval in self.resource_tags_keys:

            if not self.inputargs.get(key_eval): 
                continue

            tags = tags + ",{"+"Key={},Value={}".format(key_eval,
                                                        self.inputargs[key_eval])+"}"

        tags = tags + "]"

        return tags

    def get_region(self):
        """
        Set the gcloud region based on the inputargs or default to us-west1
        """

        self.gcloud_region = self.inputargs.get("gcloud_region")

        if not self.gcloud_region or self.gcloud_region == "None": 
            self.gcloud_region = "us-west1"

        # fixfix777
        self.logger.debug('Region set to "{}"'.format(self.gcloud_region))

    #################################################################################################################
    # non docker execution

    def _get_init_credentials_cmds(self):
        """
        This function returns a list of commands to initialize the gcloud credentials.

        The commands are:

        1. gcloud auth activate-service-account --key-file=<google_application_credentials>
        2. gcloud config set project <gcloud_project>

        Args:
            None

        Returns:
            list: A list of commands to initialize the gcloud credentials.
        """

        self.set_required()
        cmds = [ "gcloud auth activate-service-account --key-file={}".format(self.google_application_credentials) ]
        cmds.append("gcloud config set project {}".format(self.gcloud_project))

        return cmds

    def set_credentials(self):
        """
        This function sets the gcloud credentials.

        Args:
            None

        Returns:
            None
        """

        cmds = self._get_init_credentials_cmds()

        for cmd in cmds:
            results = self.execute(cmd,
                                   output_to_json=None,
                                   exit_error=True)
            output = results.get("output")
            # fixfix777
            if output: self.logger.debug(output)

            self.add_output(cmd=cmd,
                            remove_empty=True,
                            **results)

    #################################################################################################################
    # docker execution

    def cleanup_docker_run(self):
        """
        This function cleans up any docker resources created during the docker run.

        Args:
            None

        Returns:
            None
        """

        if hasattr(self,"gcloud_container_name") and self.gcloud_container_name:
            cmd = ["docker rm -fv {} 2>&1 > /dev/null".format(self.gcloud_container_name)]
            self.execute(cmd,
                         exit_error=False,
                         output_to_json=None)

        if hasattr(self,"filename") and self.filename:
            os.system("rm -rf {}".format(self.filename))

        if hasattr(self,"tempdir") and self.tempdir: 
            self.tempdir.delete()

    def init_docker_run(self):
        """
        This function initializes the docker run for interacting with gcloud.

        Steps:
        1. Pulls the docker image.
        2. Removes any existing gcloud containers.
        3. Runs the commands to initialize the gcloud credentials.
        4. Sets the gcloud project.

        Args:
            None

        Returns:
            bool: A boolean indicating whether the docker run was successful.
        """

        self.gcloud_container_name = id_generator(8)

        cmds = ["docker pull {}:latest 2>&1 > /dev/null".format(self.docker_image)]
        cmds.append('for i in `docker ps -a|grep gcloud| cut -d " " -f 1`; do echo $i; docker rm -fv $i; done')

        cmds.append("docker run -v {}:{} --name {} {} gcloud auth activate-service-account --key-file {} || exit 4".format(self.google_application_credentials,
                                                                                                                           self.google_application_credentials,
                                                                                                                           self.gcloud_container_name,
                                                                                                                           self.docker_image,
                                                                                                                           self.google_application_credentials))

        cmds.append("docker run --rm --volumes-from {} {} gcloud config set project {}".format(self.gcloud_container_name,
                                                                                               self.docker_image,
                                                                                               self.gcloud_project))

        for cmd in cmds:

            results = self.execute(cmd,
                                   output_to_json=None,
                                   exit_error=False)
            status = results.get("status")
            output = results.get("output")
            # fixfix777
            if output: self.logger.debug(output)
  
            self.add_output(cmd=cmd,
                            remove_empty=True,
                            **results)

            if not status: return False

        return True

    def write_cloud_creds(self):
        """
        This function writes the gcloud credentials to a file.

        Args:
            None

        Returns:
            str: The location of the gcloud credentials file.
        """
    
        project_id = os.environ.get("GCLOUD_PROJECT")
        private_key_id = os.environ.get("GCLOUD_PRIVATE_KEY_ID")
        private_key = os.environ.get("GCLOUD_PRIVATE_KEY")
        client_id = os.environ.get("GCLOUD_CLIENT_ID")
        client_email = os.environ.get("GCLOUD_CLIENT_EMAIL")
        client_x509_cert_url = os.environ.get("GCLOUD_CLIENT_X509_CERT_URL")
    
        if not project_id:
            # fixfix777
            self.logger.debug("GCLOUD_PROJECT is required for write credentials")
            return
    
        if not private_key_id:
            # fixfix777
            self.logger.debug("GCLOUD_PRIVATE_KEY_ID is required for write credentials")
            return
    
        if not private_key:
            # fixfix777
            self.logger.debug("GCLOUD_PRIVATE_KEY is required for write credentials")
            return
    
        if not client_id:
            # fixfix777
            self.logger.debug("GCLOUD_CLIENT_ID is required for write credentials")
            return
    
        if not client_email:
            # fixfix777
            self.logger.debug("GCLOUD_CLIENT_EMAIL is required for write credentials")
            return
    
        if not client_x509_cert_url:
            # fixfix777
            self.logger.debug("GCLOUD_CLIENT_X509_CERT_URL is required for write credentials")
            return
    
        if not hasattr(self,"tempdir") or not self.tempdir:
            self.set_ondisktmp()

        self.google_application_credentials = os.path.join(self.stateful_dir,
                                                           ".creds",
                                                           "gcloud.json")

        creds_dir = os.path.dirname(self.google_application_credentials)
    
        auth_uri = os.environ.get("GCLOUD_AUTH_URI",
                                  "https://accounts.google.com/o/oauth2/auth")
        token_uri = os.environ.get("GCLOUD_TOKEN_URI",
                                   "https://oauth2.googleapis.com/token")
        auth_provider = os.environ.get("GCLOUD_AUTH_PROVIDER",
                                       "https://www.googleapis.com/oauth2/v1/certs")
    
        values = { "type": "service_account",
                   "auth_uri": auth_uri,
                   "token_uri": token_uri,
                   "auth_provider_x509_cert_url": auth_provider,
                   "project_id": project_id,
                   "private_key_id": private_key_id,
                   "private_key": private_key,
                   "client_email": client_email,
                   "client_id": client_id,
                   "client_x509_cert_url": client_x509_cert_url,
                   }
    
        json_object = json.dumps(values,
                                 indent=2).replace('\\\\',
                                                   '\\')
    
        if not os.path.exists(creds_dir):
            os.system("mkdir -p {}".format(creds_dir))

        # fixfix777
        self.logger.debug("gcloud directory {} ...".format(self.google_application_credentials))
    
        # Writing to sample.json 
        with open(self.google_application_credentials, "w") as outfile: 
            outfile.write(json_object) 

        return self.google_application_credentials

    def set_required(self):
        """
        This function sets the required environmental variables.

        Steps:
        1. Writes the gcloud credentials to a file.
        2. Reads the gcloud credentials from the file or the environmental variables.
        3. Reads the gcloud project from the file or the environmental variables.

        Returns:
            bool: A boolean indicating whether the required environmental variables are set.
        """

        self.google_application_credentials = self.write_cloud_creds()

        if not self.google_application_credentials:
            self.google_application_credentials = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

        if not self.google_application_credentials:
            self.logger.error('cannot find environmental variables "GOOGLE_APPLICATION_CREDENTIALS"')
            exit(4)

        self.gcloud_project = os.environ.get("GCLOUD_PROJECT")

        if not self.gcloud_project:
            self.logger.error('cannot find environmental variables "GCLOUD_PROJECT"')
            exit(4)

        return True
