def _insert_volume_params(stack):

    # minimal to create the disk
    # is volume_size and volume_name
    if not stack.get_attr("volume_size"):
        return

    if not stack.get_attr("volume_name"):
        return 

    arguments = {"volume_size": stack.volume_size,
                  "volume_name": stack.volume_name}

    # minimal to create the disk
    # to optionally format and mount volume
    if stack.get_attr("volume_fstype"):
        arguments["volume_fstype"] = stack.volume_fstype

    if stack.get_attr("volume_mountpoint"):
        arguments["volume_mountpoint"] = stack.volume_mountpoint

    return arguments


def run(stackargs):

    import random

    # Do not add cluster and instance
    stackargs["add_cluster"] = False
    stackargs["add_instance"] = False

    # instantiate stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="hostname",
                             tags="server,bootstrap",
                             types="str")

    stack.parse.add_required(key="ssh_key_name",
                             tags="server,bootstrap",
                             types="str")

    stack.parse.add_required(key="aws_default_region",
                             default="us-east-1",
                             tags="server",
                             types="str")

    stack.parse.add_required(key="register_to_db",
                             types="bool",
                             default="true")

    stack.parse.add_optional(key="config_network",
                             choices=["private","public"],
                             tags="server",
                             default="public")

    # vpc info
    stack.parse.add_optional(key="vpc_name",
                             types="str")

    stack.parse.add_optional(key="vpc_id",
                             types="str")

    # security groups
    # expects csv
    stack.parse.add_optional(key="sg_id",
                             types="str")

    # security groups ids
    # expects csv
    stack.parse.add_optional(key="security_group_ids",
                             types="str")

    stack.parse.add_optional(key="security_groups",
                             types="str")

    # subnet_id
    stack.parse.add_optional(key="subnet",
                             types="str")

    stack.parse.add_optional(key="subnet_id",
                             types="str")

    stack.parse.add_optional(key="subnet_ids",
                             types="str")

    # spot request
    stack.parse.add_optional(key="spot",
                             types="bool")

    stack.parse.add_optional(key="spot_max_price",
                             types="float")

    stack.parse.add_optional(key="spot_type",
                             types="str",
                             default="persistent")

    # instance profile
    stack.parse.add_optional(key="iam_instance_profile",
                             tags="server",
                             types="str")

    # ami info
    stack.parse.add_optional(key="ami",
                             tags="server",
                             types="str")

    stack.parse.add_optional(key="ami_filter",
                             tags="server",
                             types="str")

    stack.parse.add_optional(key="ami_owner",
                             tags="server",
                             types="str")

    stack.parse.add_optional(key="instance_type",
                             tags="server",
                             types="str",
                             default="t3.micro")

    stack.parse.add_optional(key="disksize",
                             tags="server",
                             types="int",
                             default="20")

    stack.parse.add_optional(key="ip_key",
                             tags="bootstrap",
                             types="str",
                             default="public_ip")

    # extra disk
    stack.parse.add_optional(key="volume_name",
                             types="str")

    stack.parse.add_optional(key="volume_size",
                             types="str")

    stack.parse.add_optional(key="volume_mountpoint",
                             types="str")

    stack.parse.add_optional(key="volume_fstype",
                             types="str")

    # tags and labels
    stack.parse.add_optional(key="cloud_tags_hash",
                             tags="server,bootstrap",
                             types="str")

    stack.parse.add_optional(key="labels",
                             tags="server,bootstrap")

    stack.parse.add_optional(key="user",
                             tags="bootstrap",
                             default="ubuntu",
                             types="str")

    # Add substacks
    stack.add_substack("config0-hub:::bootstrap_ed")
    stack.add_substack("config0-hub:::ec2_server")

    # init the stack namespace
    stack.init_variables()
    stack.init_substacks()

    # determine specific variables

    # subnet
    if not stack.get_attr("subnet_id") and stack.get_attr("subnet_ids"):
        _subnet_ids = stack.subnet_ids.strip().split(",")
        _subnet_id = random.choice(_subnet_ids)
        stack.set_variable("subnet_id",
                           _subnet_id)

    # security groups
    if not stack.get_attr("security_group_ids") and stack.get_attr("sg_id"):

        stack.set_variable("security_group_ids",
                           stack.sg_id)

    # Main

    # Call to create the server

    arguments = stack.get_tagged_vars(tag="server",
                                      output="dict")

    arguments["timeout"] = 600

    # vpc
    if stack.get_attr("vpc_id"):
        arguments["vpc_id"] = stack.vpc_id
    elif stack.get_attr("vpc_name"):
        arguments["vpc_name"] = stack.vpc_name

    # subnet
    if stack.get_attr("subnet_id"):
        arguments["subnet_id"] = stack.subnet_id
    elif stack.get_attr("subnet"):
        arguments["subnet"] = stack.subnet

    # security groups
    if stack.get_attr("security_group_ids"):
        arguments["security_group_ids"] = stack.security_group_ids

    elif stack.get_attr("security_groups"):
        arguments["security_groups"] = stack.security_groups

    # spot request
    if stack.get_attr("spot"):

        arguments["spot"] = "True"
        arguments["spot_type"] = stack.spot_type

        if stack.get_attr("spot_max_price"):
            arguments["spot_max_price"] = stack.spot_max_price

    # see if extra disk is required
    _arguments = _insert_volume_params(stack)

    if _arguments:
        arguments.update(_arguments)

    human_description = "Instruction: Creates a Server on Ec2"
    inputargs = {"arguments": arguments,
                 "automation_phase":"infrastructure",
                 "human_description": human_description}

    stack.ec2_server.insert(display=None, 
                            **inputargs)

    if stack.get_attr("register_to_db"):

        # Call to bootstrap_ed to config0
        arguments = stack.get_tagged_vars(tag="bootstrap",
                                          output="dict")

        human_description = "Bootstraps host to Jiffy database"
        inputargs = {"arguments": arguments,
                     "automation_phase":"infrastructure",
                     "human_description": human_description}

        stack.bootstrap_ed.insert(display=None, **inputargs)

    return stack.get_results()
