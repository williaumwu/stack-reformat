def _get_user_data(stack):

    contents = '''#!/bin/bash
apt-get update && apt-get install htop jq gettext bash-completion moreutils -y
'''

    return contents

def run(stackargs):

    import random

    # instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="hostname",types="str")
    stack.parse.add_required(key="ssh_key_name",types="str")

    stack.parse.add_optional(key="iam_instance_profile",default=None,types="str")
    stack.parse.add_optional(key="ami",default=None,types="str")
    stack.parse.add_optional(key="ami_filter",default=None,types="str")
    stack.parse.add_optional(key="ami_owner",default=None,types="str")

    # spot request
    stack.parse.add_optional(key="spot",default=None,types="bool")
    stack.parse.add_optional(key="spot_max_price",default=None,types="int")
    stack.parse.add_optional(key="spot_type",default="persistent",types="str")

    stack.parse.add_required(key="sg_id",default=None,types="str")
    stack.parse.add_required(key="vpc_id",default=None,types="str")

    stack.parse.add_optional(key="aws_default_region",default="us-east-1",types="str")
    stack.parse.add_optional(key="subnet_ids",default=None,types="str")
    stack.parse.add_optional(key="subnet_id",default=None,types="str")

    stack.parse.add_optional(key="instance_type",default="t3.micro",types="str")
    stack.parse.add_optional(key="disksize",default="20",types="str")

    stack.parse.add_optional(key="user_data_hash",default=None,types="str")
    stack.parse.add_optional(key="publish_to_saas",default=None,types="str")
    stack.parse.add_optional(key="cloud_tags_hash",default=None,types="str")

    # Add substack
    stack.add_substack("config0-hub:::ec2_server")
    stack.add_substack("config0-hub:::config0-core::publish_resource")

    # Initialize 
    stack.init_variables()
    stack.init_substacks()

    stack.set_variable("resource_type","server")

    # subnet
    if not stack.get_attr("subnet_id") and stack.get_attr("subnet_ids"):
        _subnet_ids = stack.subnet_ids.strip().split(",")
        _subnet_id = random.choice(_subnet_ids)
        stack.set_variable("subnet_id",_subnet_id)

    # security groups
    # arguments = {"vpc_id":stack.vpc_id}
    # arguments["ssh_key_name"] = stack.ssh_key_name
    # arguments["aws_default_region"] = stack.aws_default_region
    # arguments["instance_type"] = stack.instance_type
    # arguments["disksize"] = stack.disksize
    # arguments["hostname"] = stack.hostname
    # arguments["register_to_db"] = False
    # arguments["subnet_id"] = stack.subnet_id
    # arguments["security_group_ids"] = stack.sg_id

    arguments = {"vpc_id": stack.vpc_id,
                 "ssh_key_name": stack.ssh_key_name,
                 "aws_default_region": stack.aws_default_region,
                 "instance_type": stack.instance_type,
                 "disksize": stack.disksize,
                 "hostname": stack.hostname,
                 "register_to_db": False,
                 "subnet_id": stack.subnet_id,
                 "security_group_ids": stack.sg_id}



    if stack.get_attr("ami"):
        arguments["ami"] = stack.ami
    elif stack.get_attr("ami_filter") and stack.get_attr("ami_owner"):
        arguments["ami_filter"] = stack.ami_filter
        arguments["ami_owner"] = stack.ami_owner

    # attaching instance profile to the VM
    if stack.get_attr("iam_instance_profile"):
        arguments["iam_instance_profile"] = stack.iam_instance_profile

    if stack.get_attr("user_data_hash"):
        # testtest777
        stack.logger.debug("5"*32)
        stack.logger.debug(stack.user_data_hash)
        arguments["user_data"] = stack.b64_encode(stack.b64_decode(stack.user_data_hash))
        stack.logger.debug("6"*32)
    else:
        arguments["user_data"] = stack.b64_encode(_get_user_data(stack))

    # spot request
    if stack.get_attr("spot"):

        arguments["spot"] = "True"
        arguments["spot_type"] = stack.spot_type

        if stack.get_attr("spot_max_price"):
            arguments["spot_max_price"] = stack.spot_max_price

    if stack.get_attr("cloud_tags_hash"):
        arguments["cloud_tags_hash"] = stack.cloud_tags_hash

    human_description = "Creating config hostname {} on ec2".format(stack.hostname)

    inputargs = {"arguments":arguments,
                 "automation_phase" : "infrastructure",
                 "human_description" : human_description}

    stack.ec2_server.insert(display=True,**inputargs)

    if not stack.get_attr("publish_to_saas"):
        return stack.get_results()

    # publish the info
    keys_to_publish = [ "region",
                        "resource_type",
                        "spot_req_id",
                        "subnet_id",
                        "vpc_id",
                        "name",
                        "private_dns_name",
                        "private_ip",
                        "provider",
                        "public_dns_name",
                        "public_ip",
                        "instance_id",
                        "key_name",
                        "ami",
                        "availability_zone",
                        "aws_default_region" ] 

    arguments = {"resource_type": stack.resource_type,
                 "name": stack.hostname,
                 "publish_keys_hash": stack.b64_encode(keys_to_publish),
                 "prefix_key": "ec2-ubuntu-admin"}

    human_description = "Publish resource info for {}".format(stack.resource_type)

    inputargs = {"arguments": arguments,
                 "automation_phase": "infrastructure",
                 "human_description": human_description}

    stack.publish_resource.insert(display=True,**inputargs)

    return stack.get_results()
