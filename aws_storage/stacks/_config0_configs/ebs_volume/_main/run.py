from config0_publisher.terraform import TFConstructor


def _determine_avail_zone(stack):

    if stack.get_attr("availability_zone"):
        return

    # we lookup instance_id or hostname
    # and use the available zone from the instance

    _lookup = {"must_be_one": True}
    _lookup["resource_type"] = "server"

    if stack.get_attr("aws_default_region"):
        _lookup["region"] = stack.aws_default_region

    if stack.get_attr("instance_id"):
        _lookup["instance_id"] = stack.instance_id
    elif stack.get_attr("hostname"):
        _lookup["hostname"] = stack.hostname
    else:
        raise Exception(
            "need to provide availability_zone/hostname/instance_id")

    server_info = list(stack.get_resource(**_lookup))[0]

    stack.set_variable("availability_zone",
                       server_info["availability_zone"],
                       tags="tfvar",
                       types="str")

    return


def run(stackargs):

    stackargs["add_cluster"] = False
    stackargs["add_instance"] = False

    # instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="volume_name",
                             tags="tfvar,db",
                             types="str")

    stack.parse.add_required(key="volume_size",
                             default=10,
                             tags="tfvar,db",
                             types="int")

    stack.parse.add_optional(key="availability_zone",
                             default="null",
                             tags="tfvar,db",
                             types="str")

    stack.parse.add_optional(key="hostname",
                             default="null",
                             types="str,db")

    stack.parse.add_optional(key="instance_id",
                             default="null",
                             types="str,db")

    stack.parse.add_optional(key="aws_default_region",
                             default="eu-west-1",
                             tags="tfvar,db,resource,runtime_settings",
                             types="str")

    # Add execgroup
    stack.add_execgroup("config0-hub:::aws_storage::ebs_volume", "tf_execgroup")

    # Add substack
    stack.add_substack('config0-hub:::tf_executor')

    # Initialize Variables in stack
    stack.init_variables()
    stack.init_execgroups()
    stack.init_substacks()

    _determine_avail_zone(stack)

    if not stack.get_attr("availability_zone"):
        raise Exception("cannot determine availability zone")

    # use the terraform constructor (helper)
    # but this is optional
    tf = TFConstructor(stack=stack,
                       execgroup_name=stack.tf_execgroup.name,
                       provider="aws",
                       resource_name=stack.volume_name,
                       resource_type="ebs_volume",
                       terraform_type="aws_ebs_volume")

    tf.include(keys=["availability_zone",
                     "arn",
                     "id"])

    tf.include(maps={"volume_id": "id"})

    # finalize the tf_executor
    stack.tf_executor.insert(display=True,
                             **tf.get())

    return stack.get_results()
