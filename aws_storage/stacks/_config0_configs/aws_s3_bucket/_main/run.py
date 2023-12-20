from config0_publisher.terraform import TFConstructor


def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key= "bucket",
                             tags= "resource, db, tfvar",
                             types= "str")

    stack.parse.add_required(key= "acl",
                             default= "_random",
                             tags= "tfvar",
                             types= "str")

    stack.parse.add_optional(key= "versioning",
                             tags= "resource, tfvar",
                             default= None,
                             types= "bool")

    stack.parse.add_optional(key= "force_destroy",
                             tags= "resource, tfvar",
                             default= None,
                             types= "bool")

    stack.parse.add_optional(key= "enable_lifecycle",
                             tags= "resource, tfvar",
                             default= None,
                             types= "bool")

    stack.parse.add_optional(key= "noncurrent_version_expiration",
                             tags= "resource, tfvar",
                             default= None,
                             types= "bool")

    stack.parse.add_optional(key= "expire_days",
                             tags= "resource, db, tfvar",
                             types= "int")

    stack.parse.add_optional(key= "aws_default_region",
                             default= "eu-west-1",
                             tags= "tfvar, db, resource, runtime_settings",
                             types= "str")

    # add execgroup
    stack.add_execgroup("config0-hub:::aws_storage::buckets",
                        "tf_execgroup")

    # Add substack
    stack.add_substack("config0-hub:::tf_executor")

    # initialize Variables in stack
    stack.init_variables()
    stack.init_execgroups()
    stack.init_substacks()

    # use the terraform constructor (helper)
    # but this is optional
    tf = TFConstructor(stack= stack,
                       execgroup_name= stack.tf_execgroup.name,
                       provider= "aws",
                       resource_name= stack.bucket,
                       resource_type= "cloud_storage",
                       terraform_type= "aws_s3_bucket")

    tf.include(keys=["server_side_encryption_configuration",
                     "lifecycle_rule",
                     "versioning",
                     "arn",
                     "id"])

    tf.include(maps={"id": "arn"})

    tf.output(keys=["arn",
                    "name",
                    "expire_days",
                    "encryption",
                    "noncurrent_version_expiration",
                    "bucket_versioning",
                    "resource_type"])

    # finalize the tf_executor
    stack.tf_executor.insert(display= True,
                             **tf.get())

    return stack.get_results()
