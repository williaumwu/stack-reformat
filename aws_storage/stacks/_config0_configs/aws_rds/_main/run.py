from config0_publisher.terraform import TFConstructor


def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key= "subnet_ids")

    stack.parse.add_required(key= "sg_id",
                             types= "str")

    stack.parse.add_required(key= "rds_name",
                             tags= "resource, runtime_settings, db, tfvar",
                             types= "str")

    stack.parse.add_optional(key= "db_name",
                             default= "_random",
                             tags= "tfvar, db",
                             types= "str")

    stack.parse.add_optional(key= "allocated_storage",
                             default= 10,
                             tags= "tfvar",
                             types= "int")

    stack.parse.add_optional(key= "engine",
                             default= "MySQL",
                             tags= "tfvar",
                             types= "str")

    stack.parse.add_optional(key= "engine_version",
                             default= "5.7",
                             tags= "tfvar",
                             types= "float")

    stack.parse.add_optional(key= "instance_class",
                             default= "db.t2.micro",
                             tags= "tfvar",
                             types= "str")

    stack.parse.add_optional(key= "multi_az",
                             default= "false",
                             tags= "tfvar",
                             types= "bool")

    stack.parse.add_optional(key= "storage_type",
                             default= "gp2",
                             tags= "tfvar",
                             types= "str")

    stack.parse.add_optional(key= "publicly_accessible",
                             default= "false",
                             tags= "tfvar",
                             types= "bool")

    stack.parse.add_optional(key= "storage_encrypted",
                             default= "false",
                             tags= "tfvar",
                             types= "bool")

    stack.parse.add_optional(key= "allow_major_version_upgrade",
                             default= "true",
                             tags= "tfvar",
                             types= "bool")

    stack.parse.add_optional(key= "auto_minor_version_upgrade",
                             default= "true",
                             tags= "tfvar",
                             types= "bool")

    stack.parse.add_optional(key= "skip_final_snapshot",
                             default= "true",
                             tags= "tfvar",
                             types= "bool")

    stack.parse.add_optional(key= "port",
                             default= "3306",
                             tags= "tfvar",
                             types= "int")

    stack.parse.add_optional(key= "backup_retention_period",
                             default= "1",
                             tags= "tfvar",
                             types= "str")

    stack.parse.add_optional(key= "backup_window",
                             default= "10:22-11:22",
                             tags= "tfvar",
                             types= "str")

    stack.parse.add_optional(key= "maintenance_window",
                             default= "Mon:00:00-Mon:03:00",
                             tags= "tfvar",
                             types= "str")

    stack.parse.add_optional(key= "rds_master_username",
                             default= None,
                             tags= "tfvar",
                             types= "str")

    stack.parse.add_optional(key= "rds_master_password",
                             default= None,
                             tags= "tfvar",
                             types= "str")

    stack.parse.add_optional(key= "aws_default_region",
                             default= "eu-west-1",
                             tags= "tfvar, db, resource, runtime_settings",
                             types= "str")

    stack.parse.add_optional(key= "publish_creds",
                             default= None,
                             types= "bool")

    stack.parse.add_optional(key= "publish_to_saas",
                             default= None,
                             types= "bool")

    # add execgroup
    stack.add_execgroup("config0-hub:::aws_storage::rds",
                        "tf_execgroup")

    # add substack
    stack.add_substack("config0-hub:::tf_executor")

    # initialize
    stack.init_variables()
    stack.init_execgroups()
    stack.init_substacks()

    # automatically name the db_subnet_name
    stack.set_variable("security_group_ids", 
                       stack.to_list(stack.sg_id),
                       tags= "tfvar",
                       types= "list")

    stack.set_variable("db_subnet_name", 
                       "{}-subnet".format(stack.rds_name),
                       tags= "tfvar",
                       types= "str")

    stack.set_variable("subnet_ids", 
                       stack.to_list(stack.subnet_ids),
                       tags= "tfvar",
                       types= "list")

    # set username and password
    if not stack.get_attr("rds_master_username") and stack.inputvars.get("DB_MASTER_USERNAME"):

        stack.set_variable("rds_master_username",
                           stack.inputvars["DB_MASTER_USERNAME"],
                           tags= "tfvar",
                           types= "str")

    elif not stack.get_attr("rds_master_username"):

        stack.set_variable("rds_master_username",
                           stack.random_id(size=20),
                           tags= "tfvar",
                           types= "str")

    if not stack.get_attr("rds_master_password") and stack.inputvars.get("DB_MASTER_PASSWORD"):

        stack.set_variable("rds_master_password",
                           stack.inputvars["DB_MASTER_PASSWORD"],
                           tags= "tfvar",
                           types= "str")

    elif not stack.get_attr("rds_master_password"):

        stack.set_variable("rds_master_password",
                           stack.random_id(size=20),
                           tags= "tfvar",
                           types= "str")

    # use the terraform constructor (helper)
    # but this is optional
    tf = TFConstructor(stack= stack,
                       execgroup_name= stack.tf_execgroup.name,
                       provider= "aws",
                       resource_name= stack.rds_name,
                       resource_type= "rds",
                       terraform_type= "aws_db_instance")

    tf.include(maps={"db_id": "arn",
                     "id": "arn"})

    tf.include(keys=["arn",
                     "address",
                     "allocated_storage",
                     "allow_major_version_upgrade",
                     "auto_minor_version_upgrade",
                     "availability_zone",
                     "ca_cert_identifier",
                     "db_name",
                     "db_subnet_group_name",
                     "delete_automated_backups",
                     "endpoint",
                     "engine",
                     "engine_version",
                     "engine_version_actual",
                     "hosted_zone_id",
                     "identifier",
                     "instance_class",
                     "multi_az",
                     "network_type",
                     "performance_insights_enabled",
                     "port",
                     "publicly_accessible",
                     "resource_id",
                     "security_group_names",
                     "skip_final_snapshot",
                     "storage_encrypted",
                     "storage_type"])

    output_keys = ["db_subnet_group_name",
                   "arn",
                   "publicly_accessible",
                   "security_group_names",
                   "availability_zone",
                   "allocated_storage",
                   "instance_class",
                   "port",
                   "performance_insights_enabled",
                   "storage_type",
                   "multi_az",
                   "engine",
                   "engine_version"]

    tf.output(keys= output_keys)

    # finalize the tf_executor
    stack.tf_executor.insert(display= True,
                             **tf.get())

    # put outs onto the saas ui (optional)
    if stack.get_attr("publish_creds") or stack.get_attr("publish_to_saas"):

        _cred_outputs = {f"{stack.engine}_root_user": stack.rds_master_username,
                         f"{stack.engine}_root_password": stack.rds_master_password,
                         f"{stack.engine}_root_password": stack.rds_master_password}

        stack.publish(_cred_outputs)

    return stack.get_results()
