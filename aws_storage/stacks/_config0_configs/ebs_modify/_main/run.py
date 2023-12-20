from config0_publisher.terraform import TFConstructor


def _determine_instance_id(stack):

    if stack.get_attr("instance_id") and stack.get_attr("aws_default_region"):
        return

    _lookup = {"must_exists":True,
               "must_be_one":True,
               "resource_type":"server"}

    if stack.get_attr("aws_default_region"):
        _lookup["region"] = stack.aws_default_region

    if stack.get_attr("hostname"):
        _lookup["hostname"] = stack.hostname

    if stack.get_attr("instance_id"):
        _lookup["instance_id"] = stack.instance_id

    _lookup["search_keys"] = "instance_id"

    server_info = list(stack.get_resource(**_lookup))[0]

    if not stack.get_attr("instance_id"):
        stack.set_variable("instance_id",
                           server_info["instance_id"],
                           types="str",
                           tags="tfvar")

    return


def _determine_volume_id(stack):

    if stack.get_attr("volume_id"):
        return

    if not stack.get_attr("volume_name"):
        return

    _lookup = {"must_exists":True,
               "must_be_one":True,
               "name":stack.volume_name,
               "resource_type":"ebs_volume"}

    if stack.get_attr("aws_default_region"):
        _lookup["region"]=stack.aws_default_region

    _info = list(stack.get_resource(**_lookup))[0]

    stack.set_variable("volume_id",
                       _info["volume_id"],
                       types="str",
                       tags="tfvar")

    return


def _get_private_key(stack):

    # get ssh_key
    _lookup = {"must_be_one":True,
               "resource_type":"ssh_key_pair",
               "name":stack.ssh_key_name,
               "serialize":True,
               "serialize_fields":["private_key"]}

    return stack.get_resource(decrypt=True, **_lookup)["private_key"]


def _get_host_info(stack):

    # get server info
    _lookup = {"must_be_one":True,
               "resource_type":"server",
               "hostname":stack.hostname}

    return list(stack.get_resource(**_lookup))[0]


def run(stackargs):

    import json

    stackargs["add_cluster"] = False
    stackargs["add_instance"] = False

    # instantiate authoring stack
    stack = newStack(stackargs)

    stack.parse.add_optional(key="aws_default_region",
                             default="eu-west-1",
                             tags="tfvar,db,resource,runtime_settings",
                             types="str")

    # Add default variables
    stack.parse.add_optional(key="volume_id",
                             default=None,
                             tags="tfvar",
                             types="str")

    stack.parse.add_optional(key="instance_id",
                             default=None,
                             tags="tfvar",
                             types="str")

    stack.parse.add_optional(key="device_name",
                             default="/dev/xvdc",
                             tags="tfvar",
                             types="str")

    stack.parse.add_optional(key="terraform_docker_runtime",
                             default="elasticdev/terraform-run-env:1.3.7",
                             types="str")

    stack.parse.add_optional(key="ansible_docker_runtime",
                             default="elasticdev/ansible-run-env",
                             types="str")

    stack.parse.add_optional(key="volume_name",
                             default=None,
                             types="str")

    stack.parse.add_optional(key="hostname",
                             default=None,
                             types="str")

    stack.parse.add_optional(key="volume_mountpoint",
                             default=None,
                             types="str")

    stack.parse.add_optional(key="volume_fstype",
                             default=None,
                             types="str")

    # this is needed for ansible when you need to ssh into the machine
    # and format and mount the volume
    stack.parse.add_optional(key="ssh_key_name",
                             default=None,
                             types="str")

    stack.parse.add_optional(key="config_network",
                             choices=["private","public"],
                             default="private",
                             types="str")

    # add execgroup
    stack.add_execgroup("config0-hub:::aws_storage::attach_volume_to_ec2", 
                        "tf_execgroup")

    stack.add_execgroup("config0-hub:::aws_storage::config_vol")

    # Add substack
    stack.add_substack("config0-hub:::tf_executor")

    # Initialize Variables in stack
    stack.init_variables()
    stack.init_execgroups()
    stack.init_substacks()

    _determine_instance_id(stack)
    _determine_volume_id(stack)

    if not stack.get_attr("volume_id"):
        msg = "Cannot determine volume_id to attach to instance"
        stack.ehandle.NeedRtInput(message=msg)

    if not stack.get_attr("instance_id"):
        msg = "Cannot determine instance_id to mount volume"
        stack.ehandle.NeedRtInput(message=msg)

    # use the terraform constructor (helper)
    # but this is optional
    tf = TFConstructor(stack=stack,
                       execgroup_name=stack.tf_execgroup.name,
                       resource_name=stack.volume_name,
                       provider="aws",
                       resource_type="attach_volume",
                       terraform_type="aws_volume_attachment",
                       docker_runtime=stack.terraform_docker_runtime)

    tf.include(maps={"ec2_instance_id":"instance_id"})

    tf.include(keys=["instance_id",
                     "id"])

    tf.output(keys=["instance_id",
                    "id"])

    # finalize the tf_executor
    stack.tf_executor.insert(display=True,
                             **tf.get())

    if not stack.volume_fstype or not stack.volume_mountpoint:
        return stack.get_results()

    #######################
    # using ansible to format and mount volume
    #######################

    private_key = _get_private_key(stack)
    host_info = _get_host_info(stack)

    env_vars = { "STATEFUL_ID": stack.random_id(size=10),
        "DOCKER_EXEC_ENV" : stack.ansible_docker_runtime,
        "ANS_VAR_volume_fstype" : stack.volume_fstype,
        "ANS_VAR_volume_mountpoint" : stack.volume_mountpoint,
        "ANS_VAR_private_key" : private_key,
        "METHOD" : "create",
        "ANS_VAR_exec_ymls": "entry_point/20-format.yml,entry_point/30-mount.yml"}

    if stack.get_attr("config_network") == "private":
        env_vars["ANS_VAR_host_ips"] = host_info["private_ip"]
    else:
        env_vars["ANS_VAR_host_ips"] = host_info["public_ip"]

    human_description = 'format/mount vol on instance_id "{}" fstype {} mountpoint {}'.format(stack.instance_id,stack.volume_fstype,stack.volume_mountpoint)

    inputargs = { "display": True,
                  "human_description" : human_description,
                  "env_vars" : json.dumps(env_vars),
                  "stateful_id" : env_vars["STATEFUL_ID"],
                  "automation_phase" : "infrastructure"}

    stack.config_vol.insert(**inputargs)

    return stack.get_results()
