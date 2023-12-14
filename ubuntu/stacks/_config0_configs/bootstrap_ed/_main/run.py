def run(stackargs):

    stackargs["add_cluster"] = False
    stackargs["add_instance"] = False

    # instantiate stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="hostname",
                             tags="host,bootstrap",
                             types="str")

    stack.parse.add_optional(key="ssh_key_name",
                             tags="host,bootstrap",
                             default="null",
                             types="str")

    stack.parse.add_optional(key="ip_key",
                             tags="bootstrap",
                             default="public_ip",
                             types="str")

    stack.parse.add_optional(key="user",
                             tags="bootstrap",
                             default="ubuntu",
                             types="str")

    # Initialize Variables in stack
    stack.init_variables()

    # Add host to the config0 engine
    cmd = "host add"
    order_type = "add-host::api"
    role = "host/add"

    arguments = stack.get_tagged_vars(tag="host",
                                      output="dict")

    human_description = "Adding/Recording host = {}".format(stack.hostname)
    long_description = "Adds host = {} to Jiffy".format(stack.hostname)

    stack.insert_builtin_cmd(cmd,
                             order_type=order_type,
                             role=role,
                             human_description=human_description,
                             long_description=long_description,
                             display=None,
                             arguments=arguments)

    # Bootstrap host to the config0 engine
    cmd = "host bootstrap"
    order_type = "bootstrap-host::api"
    role = "host/bootstrap"

    arguments = stack.get_tagged_vars(tag="bootstrap",
                                      output="dict")

    human_description = "Bootstrapping host = {}".format(stack.hostname)
    long_description = "Bootstraps host = {} to Jiffy".format(stack.hostname)

    stack.insert_builtin_cmd(cmd,
                             order_type=order_type,
                             role=role,
                             human_description=human_description,
                             long_description=long_description,
                             display=None,
                             arguments=arguments)

    return stack.get_results()
