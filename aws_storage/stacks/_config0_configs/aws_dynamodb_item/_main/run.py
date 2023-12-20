from config0_publisher.terraform import TFConstructor


def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="table_name",
                             tags="tfvar,db",
                             types="str")

    stack.parse.add_required(key="item_hash",
                             tags="tfvar",
                             types="str")

    stack.parse.add_optional(key="hash_key",
                             default="_id",
                             tags="tfvar",
                             types="str")

    stack.parse.add_optional(key="aws_default_region",
                             default="eu-west-1",
                             tags="tfvar,db,resource,runtime_settings",
                             types="str")

    # Add execgroup
    stack.add_execgroup("config0-hub:::aws_storage::dynamodb_item",
                        "tf_execgroup")

    # Add substack
    stack.add_substack("config0-hub:::tf_executor")

    # Initialize Variables in stack
    stack.init_variables()
    stack.init_execgroups()
    stack.init_substacks()

    # use the terraform constructor (helper)
    # but this is optional
    tf = TFConstructor(stack=stack,
                       execgroup_name=stack.tf_execgroup.name,
                       provider="aws",
                       resource_name=stack.table_name,
                       resource_type="db_item",
                       terraform_type="aws_dynamodb_table_item")

    tf.include(keys=["table_name",
                     "id",
                     "timeout"])

    tf.include(maps={"name":"table_name"})

    # finalize the tf_executor
    stack.tf_executor.insert(display=True,
                             **tf.get())

    return stack.get_results()
