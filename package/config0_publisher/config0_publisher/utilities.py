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
#Written by Gary Leong  <gary@config0.com, May 11,2019

import string
import random
import datetime
import json
import os
import hashlib

from config0_publisher.loggerly import Config0Logger
from config0_publisher.shellouts import mkdir
from config0_publisher.shellouts import rm_rf

class DateTimeJsonEncoder(json.JSONEncoder):
    """
    Custom JSON encoder that handles datetime objects.

    Parameters
    ----------
    obj : object
        Object to be encoded.

    Returns
    -------
    str
        Encoded object.
    """

    def default(self,obj):
        """
        Encode datetime objects as strings.

        Parameters
        ----------
        obj : object
            Object to be encoded.

        Returns
        -------
        str
            Encoded object.
        """

        if isinstance(obj,datetime.datetime):
            #newobject = str(obj.timetuple())
            newobject = '-'.join([ str(element) for element in list(obj.timetuple())][0:6])
            return newobject

        return json.JSONEncoder.default(self,obj)

def print_json(results):
    print(json.dumps(results,
                     sort_keys=True,
                     cls=DateTimeJsonEncoder,
                     indent=4))

def nice_json(results):
    return json.dumps(results,
                      sort_keys=True,
                      cls=DateTimeJsonEncoder,
                      indent=4)

def convert_str2list(_object,split_char=None,exit_error=None):
    """
    Convert a string to a list.

    Parameters
    ----------
    _object : str
        The string to convert.
    split_char : str, optional
        The character to split the string on, by default None.
    exit_error : bool, optional
        Whether to exit with an error code if the conversion fails, by default None.

    Returns
    -------
    list
        The converted list.

    Raises
    ------
    ValueError
        If the conversion fails and exit_error is True.
    """

    if split_char:
        entries = [ entry.strip() for entry in _object.split(split_char) ]
    else:
        entries = [ entry.strip() for entry in _object.split(" ") ]

    return entries

def convert_str2json(_object,exit_error=None):
    """
    Convert a string to a JSON object.

    Parameters:
    -----------
    _object: str
        The string to convert.
    exit_error: bool, optional
        Whether to exit with an error code if the conversion fails.

    Returns:
    --------
    Any
        The converted JSON object.

    Raises:
    -------
    ValueError
        If the conversion fails and exit_error is True.
    """

    if isinstance(_object,dict):
        return _object

    if isinstance(_object,list):
        return _object

    logger = Config0Logger("convert_str2json")

    try:
        _object = json.loads(_object)
        status = True
        # fixfix777
        #logger.debug("Success: Converting str to a json")
    except:
        # fixfix777
        #logger.debug("Cannot convert str to a json.  Will try to eval")
        status = False

    if not status:
        try:
            _object = eval(_object)
            # fixfix777
            #logger.debug("Success: Evaluating str to a json")
        except:
            status = False
            # fixfix777
            #logger.debug("Cannot eval str to a json.")
            if exit_error:
                exit(13)

            return False

    return _object

def to_list(_object,split_char=None,exit_error=None):
    """
    Convert a string to a list.

    Parameters:
    -----------
    _object: str
        The string to convert.
    split_char: str, optional
        The character to split the string on, by default None.
    exit_error: bool, optional
        Whether to exit with an error code if the conversion fails.

    Returns:
    --------
    list
        The converted list.

    Raises:
    -------
    ValueError
        If the conversion fails and exit_error is True.
    """

    return convert_str2list(_object,
                            split_char=split_char,
                            exit_error=exit_error)

def to_json(_object,exit_error=None):

    return convert_str2json(_object,
                            exit_error=exit_error)

def shellout_hash(string):
    """
    Calculates the md5 hash of a string using the shell command `md5sum`.

    Parameters:
        string (str): The string to hash.

    Returns:
        Optional[str]: The md5 hash of the string, or None if the hash could not be calculated.
    """

    try:
        cmd = os.popen('echo "%s" | md5sum | cut -d " " -f 1' % string, "r")
        ret = cmd.read().rstrip()
    except: 
        if os.environ.get("JIFFY_ENHANCED_LOG"):
            print("Failed to calculate the md5sum of a string %s" % string)
        return False

    return ret

def get_hash(data):
    """
    determines the hash of a data object

    Parameters:
    -----------
    data: bytes
        The data to hash

    Returns:
    --------
    str
        The calculated hash
    """

    logger = Config0Logger("get_hash")

    try:
        calculated_hash = hashlib.md5(data).hexdigest()
    except:
        # fixfix777
        logger.debug("Falling back to shellout md5sum for hash")
        calculated_hash = shellout_hash(data)

    if not calculated_hash:
        logger.error("Could not calculate hash for %s" % data)
        return False

    return calculated_hash

# dup 4523452346
def id_generator(size=6,chars=string.ascii_uppercase+string.digits):

    '''generates id randomly'''

    return ''.join(random.choice(chars) for x in range(size))

def get_dict_frm_file(file_path):

    '''
    looks at the file_path in the format
    key=value

    and parses it and returns a dictionary
    '''

    sparams = {}

    rfile = open(file_path,"r")

    non_blank_lines = (line.strip() for line in rfile.readlines() if line.strip())

    for bline in non_blank_lines:
        key,value = bline.split("=")
        sparams[key] = value

    return sparams

class OnDiskTmpDir(object):
    """
    A class for creating and managing temporary directories on disk.

    Parameters:
    -----------
    tmpdir: str, optional
        The base directory for temporary directories. Defaults to "/tmp".
    subdir: str, optional
        A subdirectory within the base directory for temporary directories.
        Defaults to "ondisktmp".
    createdir: bool, optional
        Whether to create the temporary directory if it does not exist.
        Defaults to True.

    Attributes:
    -----------
    tmpdir: str
        The base directory for temporary directories.
    subdir: str
        A subdirectory within the base directory for temporary directories.
    basedir: str
        The full path to the base directory for temporary directories.
    classname: str
        The class name.
    fqn_dir: str
        The full path to the temporary directory.
    dir: str
        The name of the temporary directory.
    logger: Config0Logger
        A logger for the class.

    Methods:
    --------
    set_dir(**kwargs)
        Create a temporary directory.
    get(**kwargs)
        Get the full path to the temporary directory.
    delete(**kwargs)
        Delete the temporary directory.
    """

    def __init__(self,**kwargs):
        """
        Initialize the class.
        """

        self.tmpdir = kwargs.get("tmpdir")

        if not self.tmpdir:
            self.tmpdir = "/tmp"

        self.subdir = kwargs.get("subdir",
                                 "ondisktmp")

        if self.subdir:
            self.basedir = "{}/{}".format(self.tmpdir,
                                          self.subdir)
        else:
            self.basedir = self.tmpdir

        self.classname = "OnDiskTmpDir"

        mkdir("/tmp/ondisktmpdir/log")

        self.logger = Config0Logger(self.classname)

        if kwargs.get("init",True):
            self.set_dir(**kwargs)

    def set_dir(self,**kwargs):
        """
        Create a temporary directory.

        Parameters:
        -----------
        createdir: bool, optional
            Whether to create the temporary directory if it does not exist.
            Defaults to True.

        Returns:
        --------
        str: The full path to the temporary directory.
        """

        createdir = kwargs.get("createdir",
                               True)

        self.fqn_dir,self.dir = generate_random_path(self.basedir,
                                                     folder_depth=1,
                                                     folder_length=16,
                                                     createdir=createdir,
                                                     string_only=True)

        return self.fqn_dir

    def get(self,**kwargs):
        """
        Get the full path to the temporary directory.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            str: The full path to the temporary directory.

        Raises:
            Exception: If the temporary directory has not been set.
        """

        if not self.fqn_dir:
            msg = "fqn_dir has not be set"
            raise Exception(msg)

        # fixfix777
        self.logger.debug('Returning fqn_dir "{}"'.format(self.fqn_dir))

        return self.fqn_dir

    def delete(self,**kwargs):
        """
        Delete the temporary directory.

        Parameters:
        -----------
        **kwargs: dict
            Additional keyword arguments.

        Returns:
        --------
        bool
            Whether the directory was deleted successfully.
        """

        # fixfix777
        self.logger.debug('Deleting fqn_dir "{}"'.format(self.fqn_dir))

        return rm_rf(self.fqn_dir)

def generate_random_path(basedir,folder_depth=1,folder_length=16,createdir=False,string_only=None):
    """
    Generates a random folder path with the specified parameters.

    Args:
        basedir (str): The base directory for the random folder path.
        folder_depth (int, optional): The number of subdirectories to create.
            Defaults to 1.
        folder_length (int, optional): The length of the random directory names.
            Defaults to 16.
        createdir (bool, optional): Whether to create the directories if they do
            not exist. Defaults to False.
        string_only (bool, optional): Whether to generate random directory names
            that are strings only. If False, the directory names will contain
            alphanumeric characters and underscores. Defaults to None, which
            means that the value of string_only will be determined based on the
            value of folder_length.

    Returns:
        tuple[str, str]: A tuple containing the full path to the random folder,
            and the name of the random folder.

    Raises:
        ValueError: If the base directory does not exist and createdir is False.
    """

    cwd = basedir

    for _ in range(folder_depth):

        if string_only:
            random_dir = id_generator(folder_length,
                                      chars=string.ascii_lowercase)
        else:
            random_dir = id_generator(folder_length)

        cwd = cwd+"/"+random_dir

    if createdir:
        mkdir(cwd)

    return cwd,random_dir

# dup 34523532452t33t
def get_values_frm_json(json_file=None):
    """
    Retrieve values from a JSON file.

    Args:
        json_file (str): The path to the JSON file.

    Returns:
        Union[dict, None]: The values from the JSON file, or None if the file
            does not exist or could not be read.
    """

    if not json_file:
        return

    if not os.path.exists(json_file):
        print("WARN: json {} does not exists".format(json_file))
        return

    try:
        with open(json_file) as json_file:
            values = json.load(json_file)
        print("retrieved values from {}".format(json_file))
    except:
        values = None
        print("ERROR: could not retrieved from json file {}".format(json_file))

    return values
