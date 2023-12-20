from config0_publisher.terraform import TFConstructor


def _get_instance_id(stack):

    # _lookup = {"must_exists": True}
    # _lookup["must_be_one"] = True
    # _lookup["resource_type"] = "server"
    # _lookup["hostname"] = stack.hostname
    # _lookup["region"] = stack.aws_default_region

    _lookup ={ "must_exists": True,
                "must_be_one" : True,
                "resource_type" : "server",
                "hostname" : stack.hostname,
                "region" : stack.aws_default_region}

    _info = list(stack.get_resource(**_lookup))[0]

    return _info["instance_id"]


def _get_volume_id(stack):

    # _lookup = {"must_exists": True}
    # _lookup["must_be_one"] = True
    # _lookup["name"] = stack.volume_name
    # _lookup["resource_type"] = "ebs_volume"
    # _lookup["region"] = stack.aws_default_region

    _lookup = { "must_exists": True,
                "must_be_one" : True,
                "name" : stack.volume_name,
                "resource_type" : "ebs_volume",
                "region" : stack.aws_default_region}

    _info = list(stack.get_resource(**_lookup))[0]

    return _info["volume_id"]


def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="hostname",
                             tags="resource,db",
                             types="str")

    stack.parse.add_optional(key="volume_name",
                             tags="resource,db",
                             default=None,
                             types="str")

    stack.parse.add_optional(key="device_name",
                             tags="tfvars,db,resource",
                             default="/dev/xvdc",
                             types="str")

    stack.parse.add_optional(key="aws_default_region",
                             default="eu-west-1",
                             tags="tfvar,db,resource,runtime_settings",
                             types="str")

    # Add execgroup
    stack.add_execgroup("config0-hub:::aws_storage::attach_volume_to_ec2",
                        "tf_execgroup")

    # Add substack
    stack.add_substack("config0-hub:::tf_executor")

    # Initialize
    stack.init_variables()
    stack.init_execgroups()
    stack.init_substacks()

    if not stack.get_attr("volume_name"):
        stack.set_variable("volume_name",
                           "{}-data".format(stack.hostname),
                           tags="resource")

    stack.set_variable("instance_id",
                       _get_instance_id(stack),
                       tags="resource,tfvar")

    stack.set_variable("volume_id",
                       _get_volume_id(stack),
                       tags="resource,tfvar")

    # use the terraform constructor (helper)
    # but this is optional
    tf = TFConstructor(stack=stack,
                       execgroup_name=stack.tf_execgroup.name,
                       provider="aws",
                       resource_name="attachment_{}".format(stack.volume_name),
                       resource_type="ebs_volume_attach",
                       terraform_type="aws_volume_attachment")

    tf.include(keys=["arn"])

    tf.include(maps= {"id":"arn"})

    # finalize the tf_executor
    stack.tf_executor.insert(display=True,
                             **tf.get())

    return stack.get_results()
