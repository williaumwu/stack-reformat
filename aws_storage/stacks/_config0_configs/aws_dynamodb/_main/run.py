from config0_publisher.terraform import TFConstructor


def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="dynamodb_name",
                             tags="resource,runtime_settings,db,tfvar",
                             types="str")

    stack.parse.add_optional(key="hash_key",
                             default="_id",
                             tags="resource,db,tfvar",
                             types="str")

    stack.parse.add_optional(key="billing_mode",
                             default="PAY_PER_REQUEST",
                             tags="resource,db,tfvar",
                             types="str")

    stack.parse.add_optional(key="aws_default_region",
                             default="eu-west-1",
                             tags="tfvar,db,resource,runtime_settings",
                             types="str")

    # Add execgroup
    stack.add_execgroup("config0-hub:::aws_storage::dynamodb",
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
                       resource_name=stack.dynamodb_name,
                       resource_type="aws_dynamodb",
                       terraform_type="aws_dynamodb_table")

    tf.include(keys=["billing_mode",
                     "arn",
                     "hash_key",
                     "name",
                     "ttl"])

    tf.include(maps={"id":"arn"})

    tf.output(keys=["billing_mode",
                    "arn",
                    "hash_key",
                    "name",
                    "ttl",
                    "resource_type"])

    # finalize the tf_executor
    stack.tf_executor.insert(display=True,
                             **tf.get())

    return stack.get_results()
