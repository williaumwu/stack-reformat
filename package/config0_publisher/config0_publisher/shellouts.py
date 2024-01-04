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

#import contextlib
import json
import string
import os
import random
import subprocess
import sys

from config0_publisher.loggerly import Config0Logger as set_log

def ensure_str(obj,strip=True):
    """
    Ensure that the input object is a string.

    Parameters
    ----------
    obj : Any
        The input object to be converted to a string.
    strip : bool, optional
        Whether to strip leading and trailing whitespace from the string, by default True.

    Returns
    -------
    str
        The input object converted to a string.

    Raises
    ------
    ValueError
        If the input object cannot be converted to a string.
    """

    if not isinstance(obj,str):
        try:
            new_obj = obj.decode("utf-8")
        except:
            new_obj = obj
            #print("could not decode - may be some encoded data")
    else:
        new_obj = obj

    if strip and isinstance(new_obj, str):
        return new_obj.strip()

    return new_obj

def id_generator(size=6,chars=string.ascii_uppercase+string.digits):

    '''generates id randomly'''

    return ''.join(random.choice(chars) for x in range(size))

def mkdir(directory):
    """
    uses the shell to make a directory.

    Creates a directory using the shell command "mkdir -p".

    Parameters:
        directory (str): The path of the directory to create.

    Returns:
        bool: True if the directory was created, False otherwise.

    Raises:
        OSError: If the directory could not be created.
    """

    try:
        if not os.path.exists(directory):
            os.system("mkdir -p %s" % (directory))
        return True
    except:
        return False

def chkdir(directory):
    """
    Check if a directory exists.

    Parameters:
        directory (str): The path of the directory to check.

    Returns:
        bool: True if the directory exists, False otherwise.

    Raises:
        OSError: If the directory could not be checked.
    """

    if not os.path.exists(directory):
        print("Directory {} does not exists".format(directory))
        return False
    return True

def rm_rf(location):
    """
    uses the shell to forcefully and recursively remove a file/entire directory.

    Parameters:
        location (str): The path of the file or directory to remove.

    Returns:
        bool: True if the file or directory was removed, False otherwise.

    Raises:
        OSError: If the file or directory could not be removed.
    """

    if not location:
        return False

    try:
        os.remove(location)
        status = True
    except:
        status = False

    if status is False and os.path.exists(location):
        try:
            os.system("rm -rf %s > /dev/null 2>&1" % (location))
            return True
        except:
            print("problems with removing %s" % location)
            return False

def execute3(cmd, **kwargs):
    """
    Execute a shell command and return the results as a dictionary.

    Parameters:
        cmd (str): The command to execute.
        unbuffered (bool, optional): Whether to disable buffering of stdout and stderr.
            Defaults to False.
        tmpdir (str, optional): The directory to use for temporary files.
            Defaults to "/tmp".
        output_to_json (bool, optional): Whether to attempt to convert the output to JSON.
            Defaults to True.
        output_queue (multiprocessing.Queue, optional): A queue to place the output into.
        env_vars (dict, optional): A dictionary of environment variables to set.
        unset_envs (str, optional): A comma-separated list of environment variables to unset.
        logfile (str, optional): The path of the log file to write output to.
        write_logfile (bool, optional): Whether to write the output to the log file.
            Defaults to False.
        exit_file (str, optional): The path of the file to write the exit code to.
        print_out (bool, optional): Whether to print the output to stdout.
            Defaults to True.
        exit_error (bool, optional): Whether to exit with the error code if it is non-zero.
            Defaults to True.

    Returns:
        dict: A dictionary containing the results of the execution, including stdout, stderr, and exitcode.

    Raises:
        RuntimeError: If the system command exits with a non-zero exit code.
    """

    shellout_exe = ShellOutExecute(cmd,
                                   unbuffered=None,
                                   **kwargs)

    shellout_exe.execute3()

    if kwargs.get("print_out",True):
        shellout_exe.print_out()

    if kwargs.get("exit_error",True) and int(shellout_exe.results["exitcode"]) != 0:
        exit(shellout_exe.results["exitcode"])

    return shellout_exe.results

def execute2(cmd, **kwargs):
    return execute3(cmd,**kwargs)

def execute3a(cmd, **kwargs):
    """
    Execute a shell command and return the results as a dictionary.

    Parameters:
        cmd (str): The command to execute.
        unbuffered (bool, optional): Whether to disable buffering of stdout and stderr.
            Defaults to False.
        tmpdir (str, optional): The directory to use for temporary files.
            Defaults to "/tmp".
        output_to_json (bool, optional): Whether to attempt to convert the output to JSON.
            Defaults to True.
        output_queue (multiprocessing.Queue, optional): A queue to place the output into.
        env_vars (dict, optional): A dictionary of environment variables to set.
        unset_envs (str, optional): A comma-separated list of environment variables to unset.
        logfile (str, optional): The path of the log file to write output to.
        write_logfile (bool, optional): Whether to write the output to the log file.
            Defaults to False.
        exit_file (str, optional): The path of the file to write the exit code to.
        print_out (bool, optional): Whether to print the output to stdout.
            Defaults to True.
        exit_error (bool, optional): Whether to exit with the error code if it is non-zero.
            Defaults to True.

    Returns:
        dict: A dictionary containing the results of the execution, including stdout, stderr, and exitcode.

    Raises:
        RuntimeError: If the system command exits with a non-zero exit code.
    """

    shellout_exe = ShellOutExecute(cmd,
                                   unbuffered=None,
                                   **kwargs)

    shellout_exe.execute3a()

    if kwargs.get("print_out"):
        shellout_exe.print_out()

    if kwargs.get("exit_error"):
        exit(shellout_exe.results["exitcode"])

    return shellout_exe.results

def execute4(cmd, **kwargs):

    return execute3a(cmd,**kwargs)

def execute5(cmd, **kwargs):
    """
    Execute a shell command and return the results as a dictionary.

    Parameters:
        cmd (str): The command to execute.
        unbuffered (bool, optional): Whether to disable buffering of stdout and stderr.
            Defaults to False.
        tmpdir (str, optional): The directory to use for temporary files.
            Defaults to "/tmp".
        output_to_json (bool, optional): Whether to attempt to convert the output to JSON.
            Defaults to True.
        output_queue (multiprocessing.Queue, optional): A queue to place the output into.
        env_vars (dict, optional): A dictionary of environment variables to set.
        unset_envs (str, optional): A comma-separated list of environment variables to unset.
        logfile (str, optional): The path of the log file to write output to.
        write_logfile (bool, optional): Whether to write the output to the log file.
            Defaults to False.
        exit_file (str, optional): The path of the file to write the exit code to.
        print_out (bool, optional): Whether to print the output to stdout.
            Defaults to True.
        exit_error (bool, optional): Whether to exit with the error code if it is non-zero.
            Defaults to True.

    Returns:
        dict: A dictionary containing the results of the execution, including stdout, stderr, and exitcode.

    Raises:
        RuntimeError: If the system command exits with a non-zero exit code.
    """

    shellout_exe = ShellOutExecute(cmd,
                                   unbuffered=None,
                                   **kwargs)

    shellout_exe.execute5()

    if kwargs.get("exit_error"):
        exit(shellout_exe.results["exitcode"])

    return shellout_exe.results

def execute7(cmd, **kwargs):
    """
    Execute a shell command and return the results as a dictionary.

    Parameters:
        cmd (str): The command to execute.
        unbuffered (bool, optional): Whether to disable buffering of stdout and stderr.
            Defaults to False.
        tmpdir (str, optional): The directory to use for temporary files.
            Defaults to "/tmp".
        output_to_json (bool, optional): Whether to attempt to convert the output to JSON.
            Defaults to True.
        output_queue (multiprocessing.Queue, optional): A queue to place the output into.
        env_vars (dict, optional): A dictionary of environment variables to set.
        unset_envs (str, optional): A comma-separated list of environment variables to unset.
        logfile (str, optional): The path of the log file to write output to.
        write_logfile (bool, optional): Whether to write the output to the log file.
            Defaults to False.
        exit_file (str, optional): The path of the file to write the exit code to.
        print_out (bool, optional): Whether to print the output to stdout.
            Defaults to True.
        exit_error (bool, optional): Whether to exit with the error code if it is non-zero.
            Defaults to True.

    Returns:
        dict: A dictionary containing the results of the execution, including stdout, stderr, and exitcode.

    Raises:
        RuntimeError: If the system command exits with a non-zero exit code.
    """

    shellout_exe = ShellOutExecute(cmd,
                                   unbuffered=None,
                                   **kwargs)

    shellout_exe.execute7()

    if kwargs.get("print_out",True):
        shellout_exe.print_out()

    if kwargs.get("exit_error"):
        exit(shellout_exe.results["exitcode"])

    return shellout_exe.results

def execute(cmd,unbuffered=False,logfile=None,print_out=True):
    """
    executes a shell command, returning status of execution,
    standard out, and standard error

    Parameters:
        cmd (str): the command to execute
        unbuffered (bool, optional): whether to disable buffering of stdout and stderr. Defaults to False.
        logfile (str, optional): the path of the log file to write output to. Defaults to None.
        print_out (bool, optional): whether to print the output to stdout. Defaults to True.

    Returns:
        tuple[int, str, str]: a tuple containing the exit code, stdout, and stderr of the executed command.
    """

    inputargs = {"unbuffered":unbuffered}

    if logfile:
        inputargs["logfile"] = logfile
        inputargs["write_logfile"] = True

    shellout_exe = ShellOutExecute(cmd,
                                   **inputargs)

    shellout_exe.popen2()

    if print_out and unbuffered:
        shellout_exe.print_out()

    return shellout_exe.results["exitcode"],shellout_exe.results["stdout"],shellout_exe.results["stderr"]

class ShellOutExecute(object):
    """
    Execute a shell command and return the results as a dictionary.

    Parameters:
        cmd (str): The command to execute.
        unbuffered (bool, optional): Whether to disable buffering of stdout and stderr.
            Defaults to False.
        tmpdir (str, optional): The directory to use for temporary files.
            Defaults to "/tmp".
        output_to_json (bool, optional): Whether to attempt to convert the output to JSON.
            Defaults to True.
        output_queue (multiprocessing.Queue, optional): A queue to place the output into.
        env_vars (dict, optional): A dictionary of environment variables to set.
        unset_envs (str, optional): A comma-separated list of environment variables to unset.
        logfile (str, optional): The path of the log file to write output to.
        write_logfile (bool, optional): Whether to write the output to the log file.
            Defaults to False.
        exit_file (str, optional): The path of the file to write the exit code to.
        print_out (bool, optional): Whether to print the output to stdout.
            Defaults to True.
        exit_error (bool, optional): Whether to exit with the error code if it is non-zero.
            Defaults to True.

    Attributes:
        cwd (str): The current working directory.
        tmpdir (str): The directory to use for temporary files.
        unbuffered (bool): Whether to disable buffering of stdout and stderr.
        cmd (str): The command to execute.
        output_to_json (bool): Whether to attempt to convert the output to JSON.
        output_queue (multiprocessing.Queue): A queue to place the output into.
        env_vars (dict): A dictionary of environment variables to set.
        unset_envs (str): A comma-separated list of environment variables to unset.
        logfile (str): The path of the log file to write output to.
        logfile_handle (file): The file handle for the log file.
        results (dict): A dictionary containing the results of the execution, including stdout, stderr, and exitcode.

    Raises:
        RuntimeError: If the system command exits with a non-zero exit code.
    """

    def __init__(self, cmd, unbuffered=None, **kwargs):
        """
        Initialize the ShellOutExecute class.

        Parameters:
            cmd (str): The command to execute.
            unbuffered (bool, optional): Whether to disable buffering of stdout and stderr.
                Defaults to False.
            tmpdir (str, optional): The directory to use for temporary files.
                Defaults to "/tmp".
            output_to_json (bool, optional): Whether to attempt to convert the output to JSON.
                Defaults to True.
            output_queue (multiprocessing.Queue, optional): A queue to place the output into.
            env_vars (dict, optional): A dictionary of environment variables to set.
            unset_envs (str, optional): A comma-separated list of environment variables to unset.
            logfile (str, optional): The path of the log file to write output to.
            write_logfile (bool, optional): Whether to write the output to the log file.
                Defaults to False.
            exit_file (str, optional): The path of the file to write the exit code to.
            print_out (bool, optional): Whether to print the output to stdout.
                Defaults to True.
            exit_error (bool, optional): Whether to exit with the error code if it is non-zero.
                Defaults to True.
        """

        self.logger = set_log("ShellOutExecute")

        self._set_cwd()
        self.tmpdir = kwargs.get("tmpdir", "/tmp")

        self.unbuffered = unbuffered
        self.cmd = cmd

        self.output_to_json = kwargs.get("output_to_json", True)
        self.output_queue = kwargs.get("output_queue")

        self.env_vars = kwargs.get("env_vars")
        self.unset_envs = kwargs.get("unset_envs")

        self.logfile = kwargs.get("logfile")
        self.env_vars_set = {}

        self.exit_file = kwargs.get("exit_file")

        if not self.exit_file:
            self.exit_file = os.path.join(self.tmpdir,
                                          id_generator(10, chars=string.ascii_lowercase))

        if not self.logfile:
            self.logfile = os.path.join(self.tmpdir,
                                        id_generator(10, chars=string.ascii_lowercase))

        self.logfile_handle = None

        if kwargs.get("write_logfile"):
            self.logfile_handle = open(self.logfile, "w")

        self.results = {"status": None,
                        "failed_message": None,
                        "output": None,
                        "exitcode": None}

    def _set_cwd(self):
        """
        Set the current working directory.

        Returns:
            str: The current working directory.

        Raises:
            OSError: If the current working directory could not be set.
        """

        try:
            self.cwd = os.getcwd()
        except:
            self.logger.warn("Cannot determine current directory - setting cwd to /tmp")
            self.cwd = "/tmp"
            os.chdir(self.cwd)

        return self.cwd

    def _get_system_cmd(self):
        """
        Get the system command to execute.

        Returns:
            str: The system command to execute.
        """

        cmd = '({} 2>&1 ; echo $? > {}) | tee -a {}; exit `cat {}`'.format(self.cmd,
                                                                           self.exit_file,
                                                                           self.logfile,
                                                                           self.exit_file)

        return cmd

    def _cleanup_system_exe(self):
        """
        Clean up the system executable.

        :return: None
        """

        os.remove(self.exit_file)
        os.remove(self.logfile)

    def add_unset_envs_to_cmd(self):
        """
        Add any unset environment variables to the command.
        """

        if not self.unset_envs:
            return

        unset_envs = [ _element.strip() for _element in self.unset_envs.split(",") ]

        for _env in unset_envs:
            self.cmd = "unset {}; {}".format(_env,self.cmd)

    def set_env_vars(self):
        """
        Set the environment variables.

        Returns:
            dict: The environment variables that were set.

        Raises:
            OSError: If the environment variables could not be set.
        """

        if not self.env_vars:
            return

        _env_vars = self.env_vars.get()

        for ek, ev in _env_vars.items():
            if ev is None:
                ev = "None"
            elif isinstance(ev,bytes):
                ev = ev.decode("utf-8")
            elif not isinstance(ev,str):
                ev = str(ev)

            if os.environ.get("JIFFY_ENHANCED_LOG") or os.environ.get("DEBUG_STATEFUL"):
                self.logger.debug("key -> {} value -> {} type -> {}".format(ek,ev,type(ev)))
            else:
                self.logger.debug("Setting environment variable {}, type {}".format(ek,type(ev)))

            self.env_vars_set[ek] = ev
            os.environ[ek] = ev

        if os.environ.get("JIFFY_ENHANCED_LOG"):

            self.logger.debug("#" * 32)
            self.logger.debug("# env vars set are")

            print((json.dumps(self.env_vars_set,
                              sort_keys=True,
                              indent=4)))

            self.logger.debug("#" * 32)

        return _env_vars

    def print_out(self):
        """
        print the output of the executed command
        """
        try:
            self.logger.debug(self.results["output"])
        except:
            print(self.results["output"])

    def _convert_output_to_json(self):
        """
        Convert the output of the executed command to JSON if possible.

        Returns:
            bool: True if the output could be converted to JSON, False otherwise.
        """

        if not self.output_to_json:
            return

        if isinstance(self.results["output"], dict):
            return

        try:
            output = json.loads(self.results["output"])
        except:
            self.logger.debug("Could not convert output to json")
            return

        self.logger.debug("output to json/dict")

        self.results["output"] = output

        return True

    def _eval_execute(self):
        """
        Evaluate the results of the executed command.

        This method sets the status of the results based on the exit code and sets the
        failed_message based on the output. It also converts the output to JSON if
        possible and places the results in the output_queue if provided.

        """

        if self.results["exitcode"] != 0:
            self.results["status"] = False
            self.results["failed_message"] = self.results["output"]

        else:
            self.results["status"] = True
            self._convert_output_to_json()

        if self.output_queue:
            self.logger.debug("attempting to place results in the output_queue")
            try:
                self.output_queue.put(self.results)
            except:
                self.logger.error("Could not append the results to the output_queue")

    def set_popen_kwargs(self):
        """
        Set the popen_kwargs attribute of the ShellOutExecute instance.

        The popen_kwargs attribute is a dictionary that is used to set the arguments
        for the subprocess.Popen constructor. The dictionary contains the following
        keys:

        shell (bool): Whether to execute the command in a shell.
        universal_newlines (bool): Whether to use universal newlines mode.
        stdout (file-like object): The file-like object to use for stdout.
        stderr (file-like object): The file-like object to use for stderr.

        This method sets the popen_kwargs attribute to a dictionary with the above
        keys and values.
        """

        self.popen_kwargs = {"shell":True,
                             "universal_newlines": True,
                             "stdout":subprocess.PIPE,
                             "stderr": subprocess.STDOUT}
    def run(self):
        """
        Runs the command and returns the results.

        Returns:
            dict: A dictionary containing the results of the execution, including stdout, stderr, and exitcode.
        """

        self.logger.debug_highlight("ShellOutExecute:::method: run")

        self.set_env_vars()
        self.set_popen_kwargs()

        process = subprocess.run(self.cmd,
                                 **self.popen_kwargs)

        self.results["output"] = process.stdout

        self._add_log_file(self.results["output"])

        self.results["exitcode"] = self._eval_exitcode(process.returncode)

        self._eval_execute()

        return self.results

    def _init_popen(self):

        return subprocess.Popen(self.cmd,
                                **self.popen_kwargs)

    def _add_log_file(self,line):
        """
        Add a line to the log file.

        Args:
            line (str): The line to add to the log file.

        Returns:
            None
        """

        if not self.logfile_handle:
            return

        self.logfile_handle.write(line)
        self.logfile_handle.write("\n")

    def _eval_log_line(self, readline, lines):
        """
        Add a line to the log file and optionally print it to stdout.

        Args:
            readline (bytes): The line to add to the log file.
            lines (list): A list of lines.

        Returns:
            bool: Whether to continue reading from the process.
        """

        line = ensure_str(readline, strip=True)

        if not line:
            return

        lines.append(line)

        if self.unbuffered:
            print(line)

        self._add_log_file(line)

        return True

    def _eval_popen_exe(self,process):
        """
        Evaluate the results of the executed command.

        This method sets the status of the results based on the exit code and sets the
        failed_message based on the output. It also converts the output to JSON if
        possible and places the results in the output_queue if provided.

        Args:
            process (subprocess.Popen): The process that was executed.

        Returns:
            None
        """

        lines = []

        while True:

            readline = process.stdout.readline()
            self._eval_log_line(readline,lines)

            exitcode = process.poll()

            if exitcode is None:
                continue

            _last_lines = process.stdout.readlines()

            if _last_lines:
                for _last_line in _last_lines:
                    self._eval_log_line(_last_line,lines)
            break

        if self.logfile_handle:
            self.logfile_handle.close()

        if lines:
            self.results["output"] = "\n".join(lines)

        self.results["exitcode"] = self._eval_exitcode(exitcode)

        if exitcode != 0:
            self.results["status"] = False
        else:
            self.results["status"] = True

        self._eval_execute()
    def _popen_communicate(self,process):
        """
        Communicate with a subprocess.Popen instance.

        Args:
            process (subprocess.Popen): The subprocess to communicate with.

        Returns:
            dict: A dictionary containing the stdout, stderr, and exitcode of the process.
        """

        out, err = process.communicate()

        self.results["stdout"] = out
        self.results["stderr"] = err
        self.results["exitcode"] = self._eval_exitcode(process.returncode)

        return self.results

    def popen(self):
        """
        Runs the command and returns the results.

        Returns:
            dict: A dictionary containing the results of the execution, including stdout, stderr, and exitcode.
        """

        self.logger.debug_highlight("ShellOutExecute:::method: popen")

        self.set_popen_kwargs()
        self.popen_kwargs["bufsize"] = 0

        process = self._init_popen()

        self._eval_popen_exe(process)

        return self.results

    def popen2(self):
        """
        Runs the command and returns the results.

        Returns:
            dict: A dictionary containing the results of the execution, including stdout, stderr, and exitcode.
        """

        self.logger.debug_highlight("ShellOutExecute:::method: popen2")

        process = subprocess.Popen(self.cmd,
                                   shell=True,
                                   universal_newlines=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

        self._popen_communicate(process)

        return self.results

    def execute6(self):
        """
        Runs the command and returns the results.

        Returns:
            dict: A dictionary containing the results of the execution, including stdout, stderr, and exitcode.
        """

        self.logger.debug_highlight("ShellOutExecute:::method: execute6")

        self.logger.debug("from directory {} - command {}".format(os.getcwd(),
                                                                  self.cmd))

        self.set_env_vars()
        self.add_unset_envs_to_cmd()

        return self.popen()

    def execute3(self):
        """
        Runs the command and returns the results.

        Returns:
            dict: A dictionary containing the results of the execution, including stdout, stderr, and exitcode.
        """

        self.logger.debug_highlight("ShellOutExecute:::method: execute3")

        self.logger.debug("from directory {} - command {}".format(os.getcwd(),
                                                                  self.cmd))

        self.set_env_vars()

        self.popen()

        return self.results

    def system(self, direct_return=True):
        """
        Runs the command in a subshell and returns the exit code.

        Parameters:
            direct_return (bool, optional): Whether to return the exit code directly or to calculate the return value code.
                Defaults to True.

        Returns:
            int: The exit code of the executed command.

        Raises:
            RuntimeError: If the system command exits with a non-zero exit code.
        """

        self.logger.debug_highlight("ShellOutExecute:::method: system")

        cmd = self._get_system_cmd()
        _return_code = os.system(cmd)

        if direct_return:
            return self._eval_exitcode(_return_code)

        # calculate the return value code
        return int(bin(_return_code).replace("0b", "").rjust(16, '0')[:8], 2)

    def _eval_exitcode(self,exitcode):
        """
        Convert the exitcode to an integer if possible, otherwise return the original exitcode.

        Parameters:
            exitcode (object): The exitcode to convert to an integer.

        Returns:
            int: The converted exitcode.
        """

        try:
            return int(exitcode)
        except:
            return exitcode

    def execute3a(self):
        """
        Runs the command and returns the results.

        Returns:
            dict: A dictionary containing the results of the execution, including stdout, stderr, and exitcode.
        """

        self.logger.debug_highlight("ShellOutExecute:::method: execute3a")

        self.results["exitcode"] = self.system(direct_return=True)
        self.results["output"] = open(self.logfile, "r").read()
        self._eval_execute()
        self._cleanup_system_exe()

        return self.results

    def execute5(self):
        """
        Runs the command and returns the results.

        Returns:
            dict: A dictionary containing the results of the execution, including stdout, stderr, and exitcode.
        """

        self.logger.debug_highlight("ShellOutExecute:::method: execute5")

        exitcode = self.system(direct_return=True)

        if exitcode != 0:
            raise RuntimeError('system command\n{}\nexitcode {}'.format(self.cmd,
                                                                        exitcode))

        self.results["exitcode"] = exitcode
        self.results["output"] = open(self.logfile, "r").read()
        self._eval_execute()
        self._cleanup_system_exe()

        return self.results

    def execute7(self):
        """
        Runs the command and returns the results.

        Returns:
            dict: A dictionary containing the results of the execution, including stdout, stderr, and exitcode.
        """

        self.logger.debug_highlight("ShellOutExecute:::method: execute7")
        self.run()

        return self.results
