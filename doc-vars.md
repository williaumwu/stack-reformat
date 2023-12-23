| hostname   | the hostname to install jenkins       | string   | None         |
| ssh_key_name   | the ssh_key_name to log into jenkins       | string   | None         |
| remote_file   | the fully qualified remote file to get the contents from      | string   | None         |
| key   | the key used to show on the UI for the contents of the remote file e.g. password    | string   | None         |
| resource_type   | the resource type       | string   |    |
| resource_name   | the resource name       | string   |    |
| dst_exec_group   | the execgroup to execute       | string   |    |
| cloud_tags_hash | the tags for the resources in the cloud as base64 | string  | None         |
| name   | name of the ssh key                 | string   | None         |
| vars_set_name   | the name of the variables set       | string   |    |
| env_vars_hash   | environment variables key/value (dict) converted to base64 hash      | string   |    |
| labels_hash   | query labels key/value (dict) converted to base64 hash      | string   |    |
| arguments_hash   | arguments key/value (dict) converted to base64 hash      | string   |    |
| env_vars_hash   | key/value (dict) that is converted to base64 hash      | string   |    |
| evaluate   | whether to evaluate to queries to immediate values      | null/True   | null    |
| resource_type   | the resource type       | string   |    |
| name   | the name resource | string   |    |
| match_hash   | the json match dictionary converted to b64 hash | string   |    |
| labels_hash   | the json labels dictionary converted to b64 hash | string   |    |
| ref_schedule_id   | the reference schedule_id for the query | string   |    |
| publish_keys_hash   | the keys to publish converted to b64  | string   |    |
| map_keys_hash   | map keys b64 (dict) is use to change the key name that shows up on the UI (b64) | string   |    |
| prefix_key   | prefix for each key (b64) | string   |    |
| hostname   | the hostname to install jenkins       | string   | None         |
| ssh_key_name   | the ssh_key_name to log into hostname | string   | None         |
| publish_private_key   | if set true, the private key in base64 hash will show on the Config0 UI           | string   | None    |
| ansible_docker_exec_env   | overide the default the docker runtime to execute ansible used to install jenkins | string   | elasticdev/ansible-run-env        |
| hostname   | the hostname       | string   | None         |
| ssh_key_name   | the ssh key name for the VMs       | string   | None         |
| vpc_id | the vpc id | string   | None       |
| subnet_ids   | a subnet for the VMs is selected from a list of the provided subnet_ids  | string in csv   | None         |
| sg_id   | the security group id for the VMs       | string   | None         |
| spot   | the option to use spot VM. (buyer be aware)    | boolean   | None        |
| ami   | the ami image used for VM      | string   | None        |
| ami_filter   | the ami filter used to search for an image as a base for VM      | string   | None        |
| ami_owner   | the ami owner used to search for an image as a base for VM      | string   | None        |
| aws_default_region   | the aws region                | string   | us-east-1         |
| instance_type | the instance_type for the VMs | string   | t3.micro       |
| disksize | the disksize for the VM | string   | None       |
| tags | the tags for the VM | string   | None       |
| labels | the labels for the VM | string   | None       |
| publish_to_saas | publish or print vm info to saas ui | boolean   | None       |
| hostname | the hostname of the server to bootstrap | string   | None    |
| ssh_key_name | the ssh key name use to authenticate to server                                                   | string               | None      |
| ip_key       | the ip_key refers to private or public networks                           | public_ip/private_ip | public_ip |
| user         | the user to log into the server with | string               | ubuntu    |
| hostname   | hostname of the ec2 server                 | string   | None         |
| ssh_key_name   | ssh_key_name for the ec2 server                 | string   | None         |
| aws_default_region   | default aws region               | string   | us-east-1         |
| config_network   | the configuration network                | choice public/private   | private |
| register_to_db   | register the ec2 instance to Config0               | boolean   | True |
| sg_id   | the single security group id for the ec2 instance               | string   | None |
| security_group_ids   | the security group ids for the ec2 instance               | list   | None |
| security_group   | the security group names for the ec2 instance               | list   | None |
| subnet   | the name of subnet to be used        | string    | None |
| subnet_id   | the subnet_id to be used        | string    | None |
| subnet_ids   | the subnet_ids to select from        | string (csv)    | None |
| image   | the ami image               | string   | None |
| image_filter   | the image filter used for searches      | string       | Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-\*  | 
| image_owner   | the image owner used for searches        | string    | 099720109477 (canonical) |
| size   | the instance size        | string    | t2.micro |
| disksize   | the instance root disk size        | string    | 40 |
| ip_key   | the ip_key from boto used for connection       | public_ip/private_ip    | public_ip |
| vpc_id   | the vpc_id to be used        | string    | None |
| vpc_name   | the name of vpc to be used        | string    | None |
| volume_name   | the name of volume to be attached        | string    | None |
| volume_size   | the size of volume to be created        | string    | None |
| volume_mount   | the mount point of the extra volume        | string    | None |
| volume_fstype   | the fileystem of the extra volume        | string    | None |
| key_name   | name of the ssh key                 | string   | None         |
| repo   | github repository | string   | None         |
| key_name   | name of the ssh key                 | string   | None         |
| name   | name of the ssh key                 | string   | None         |
| public_key   | public_key in base64                | string   | None         |
| read_only   | read_only (true/false)               | boolean   | true         |
| name   | name of the webhook | string   | None         |
| repo   | github repository | string   | None         |
| url   | the designated url for the webook | string   | None         |
| secret   | the secret to verify the webook | [auto-generated-random]   | None         |
| insecure_ssl   | allowed insecure ssl connection | true   | None         |
| active   | webhook is active or not | true   | None         |
| content_type   | content_type of webhook | json   | None         |
| events   | events of to invoke webhook | push,pull_request   | None         |
| db_instance_name   | name of the RDS instance                | string   | None         |
| db_root_user   | root user for RDS                 | string   | None         |
| db_root_password   | root password RDS                 | string   | None         |
| db_name   | db name                  | string   | None         |
| db_user   | the user of the db                 | string   | None         |
| db_password   | the password of the db                 | string   | None         |
| publish_creds   | whether to display credentials on the Config0 dashboard                 | boolean   | True         |
| bucket   | bucket in aws | string   | random         |
| acl   | acl for bucket | private/public   | private         |
| aws_default_region   | default aws region               | string   | us-east-1         |
| force_destroy   | force_destroy for bucket if destroying| string   | None         |
| versioning   | versioning for bucket assets| string   | None         |
| enable_lifecycle   | enable_lifecycle for bucket                 | string   | None         |
| expire_days   | expire_days for bucket assets only if lifecycle is enabled                | int   | None         |
| noncurrent_version_expiration   | noncurrent_version_expiration for bucket assets only if lifecycle is enabled | int   | None         |
| cloud_tags_hash | the tags for the resources in the cloud as base64 | string  | None         |
| hostname   | the hostname to mount the volume       | string   | None         |
| aws_default_region   | aws region to create the ecr repo                | string   | us-east-1         |
| device_name | the device name for the volume | string   | /dev/xvdc       |
| docker_exec_env | the docker container for terraform execution | string   | elasticdev/terraform-run-env       |
| volume_name   | the volume_name to mount on the hostname       | string   | <hostname>-name         |
| name   | name of the repository                 | string   | None         |
| docker_repo   | name of the repository with a key "docker_repo"                | string   | None         |
| aws_default_region   | default aws region               | string   | us-east-1         |
| dynamodb_name   | name of the dynamodb table | string   |        |
| aws_default_region   | default aws region               | string   | us-east-1         |
| hash_key   | the hash key of the dynamodb table | string   |  \_id      |
| billing_mode   | pay per request | string   |  PAY_PER_REQUEST | 
| cloud_tags_hash | the tags for the resources in the cloud as base64 | string  | None         |
| ssm_key   | ssm key for the parameter store                 | string   | random         |
| ssm_value   | ssm value for the parameter store                 | string   | None         |
| aws_default_region   | default aws region               | string   | us-east-1         |
| ssm_description   | ssm description for the parameter store                 | string   | None         |
| ssm_type   | ssm type for the parameter store                 | choice   | SecureString(default),String         |
| vpc_name   | name of the vpc                 | string   | None         |
| rds_name   | the name given to the rds instance | string   | None         |
| sg_id   | the security group id for the rds instance | string   | None         |
| subnet_ids   | the subnet_ids separated by comma - csv - for rds instance | string   | None         |
| aws_default_region   | the default aws region               | string   | us-west-1         |
| master_username   | the master username for rds               | string   | random        |
| master_password   | the master password for rds               | string   | random        |
| engine | the rds engine | string | MySQL   |
| engine_version | the rds engine version | string | 5.7   |
| allocated_storage | the rds storage size | string | 10   |
| db_name | the db_name to create in rds | string | random   |
| instance_class | the instance_class for rds instance | string | db.t2.micro   |
| port | the port for rds instance | string | 3306   |
| multi_az | sets multi placement zone for rds | string | false   |
| storage_type | storage type for rds | string | gp2   |
| storage_encrypted | encrypt storage for rds | string | false   |
| publicly_accessible | makes rds publicly accessible | string | false   |
| allow_major_version_upgrade | allow_major_version_upgrade for rds | string | true   |
| auto_minor_version_upgrade | auto_minor_version_upgrade for rds | string | true   |
| skip_final_snapshot | skip_final_snapshot for rds when destroying | string | true   |
| publish_creds | show credentials on the Config0 dashboard | string | True   |
| cloud_tags_hash | the tags for the resources in the cloud as base64 | string  | None         |
| item_hash    | json/dictionary item as a base64 | string   |        |
| table_name    | the dynamodb table | string   |        |
| hash_key    | the hash_key for the dynamodb table | string   |      |
| aws_default_region   | default aws region               | string   | us-east-1         |
| tier_level   | the tier_level                | choice 2/3   | None |
| cloud_tags_hash | the tags for the resources in the cloud as base64 | string  | None         |
| environment   | the environment                | string   | dev |
| main_network_block   | the cidr for the main network nat                | string   | 10.9.0.0/16 |
| enable_nat_gateway   | enable nat gateway                | string   | |
| single_nat_gateway   | single nat gateway                | string   | |
| enable_dns_hostnames   | enable dns hostnames                | string   | |
| reuse_nat_ips   | reuse nat ips                | string   | |
| one_nat_gateway_per_az   | set true if you want one nat gateway per az (more expensive)                | string   | |
| eks_cluster   | provide an EKS cluster if vpc requires eks settings                | string   | |
| labels   | the labels for the vpc.  this is typically needed for EKS                | string   | |
| tags   | the tags for the vpc.  this is typically needed for EKS                | string   | |
| aws_default_region   | default aws region               | string   | us-east-1         |
| docker_exec_env   | the docker container to execute the underlying Terraform templates               | string   | elasticdev/terraform-run-env         |
| aws_default_region   | default aws region               | string   | us-east-1         |
| tier_level   | "2" or "3" tier for security groups                | string   |  |
| vpc_tags   | AWS tags for the vpc                | string   | |
| nat_gw_tags   | AWS tags for the nat gw                | string   | |
| public_subnet_tags   | AWS tags for the public subnet                | string   | |
| private_subnet_tags   | AWS tags for the private subnet                | string   | |
| enable_nat_gateway   | enable nat gateway                | string   | |
| single_nat_gateway   | single nat gateway                | string   | |
| enable_dns_hostnames   | enable dns hostnames                | string   | |
| reuse_nat_ips   | reuse nat ips                | string   | |
| one_nat_gateway_per_az   | set true if you want one nat gateway per az (more expensive)                | string   | |
| environment   | the environment                | string   | dev |
| main_network_block   | the cidr for the main network nat                | string   | 10.9.0.0/16 |
| labels   | Config0 resource labels for the vpc                 | string   | None |
| tags   | Config0 resource tags for the vpc                 | string   | None |
| environment   | the environment                | string   | dev |
| enable_dns_hostnames   | enable dns hostnames                | string   | |
| eks_cluster   | provide an EKS cluster if vpc requires eks settings                | string   | |
| labels   | the labels for the vpc.  this is typically needed for EKS                | string   | |
| tags   | the tags for the vpc.  this is typically needed for EKS                | string   | |
| aws_default_region   | default aws region               | string   | us-east-1         |
| docker_exec_env   | the docker container to execute the underlying Terraform templates               | string   | elasticdev/terraform-run-env         |
| cloud_tags_hash | the tags for the resources in the cloud as base64 | string  | None         |
| vpc_name   | name of the vpc                 | string   | None         |
| bastion_hostname   | the hostname for the bastion used to install and configure mongodb on VMs       | string   | None         |
| mongodb_hosts   | the hostnames for he mongodb_hosts in the replica set separated by a comma       | string (csv)   | None         |
| mongodb_cluster   | the name of the mongodb cluster       | string   | None         |
| ssh_key_name   | the name the ssh_key_name to use for the VMs       | string   | None         |
| aws_default_region   | aws region to create the ecr repo                | string   | us-east-1         |
| num_of_replicas   | the number of replicas in the mongodb cluster       | string   | 1         |
| bastion_sg_id   | the security group id used for the bastion config host      | string   | bastion         |
| bastion_subnet_ids   | the subnet id(s) in CSV used for the bastion config host      | string   | private         |
| subnet_ids   | the subnet id(s) in CSV used for the mongodb servers     | string   | private         |
| vpc_id | the vpc id | string   | None       |
| sg_id | security group id for the VMs | string   | None       |
| mongodb_username | the master mongodb username    | string   | <random>       |
| mongodb_password | the master mongodb password    | string   | <random>       |
| vm_username | The username for the VM.  e.g. ec2 for AWS linux     | string   | master       |
| mongodb_data_dir | the directory for mongodb data | string   | /var/lib/mongodb       |
| mongodb_storage_engine | the storage engine for mongodb | string   | wiredTiger       |
| mongodb_version | the version for mongodb | string   | 4.0.3       |
| mongodb_port | the port for mongodb | string   | 27017       |
| mongodb_bind_ip | the bind ip for mongodb to listen | string   | 0.0.0.0       |
| mongodb_logpath | the logpath for mongodb | string   | /var/log/mongodb/mongod.log      |
| publish_creds | publish the credentials for mongodb for Config0 output in UI | string   | True     |
| volume_fstype | the fileystem type for volume used for mongodb data | string   | xfs       |
| device_name | the device name for the extra data volume for mongodb data | string   | /dev/xvdc       |
| volume_mountpoint | the volume mountpoint for mongodb data | string   | /var/lib/mongodb       |
| terraform_docker_exec_env | the docker container for terraform execution | string   | elasticdev/terraform-run-env       |
| ansible_docker_exec_env | the docker container for ansible execution | string   | elasticdev/ansible-run-env       |
| basename   | the basename for the mongodb hostname [^1] | string   | None         |
| mongodb_cluster   | the name of the mongodb cluster       | string        | None         |
| num_of_replicas   | the number of replicas in the mongodb cluster       | integer       | 1         |
| vpc_id | the vpc id | string        | None       |
| subnet_ids   | a subnet for the VMs is selected from a list of the provided subnet_ids  | string in csv | None         |
| sg_id   | the security group id for the VMs       | string        | None         |
| bastion_subnet_ids   | the subnet_ids to select a subnet_id for the bastion host       | string in csv | None         |
| bastion_sg_id   | the security group id for the bastion host       | string        | None         |
| mongodb_version        | the mongodb version to install                                                | string   | 4.2              |
| config_network         | the network to push configuration to mongodb hosts                            | private/public  | private          |
| spot                   | the option to use spot intances. (buyer be aware)                             | boolean  | None             |
| spot_type              | the option to set spot type for spot instances                                | string   | persistent       |
| spot_max_price         | the option to set spot max price spot instances                               | string   | None             |
| ami                    | the ami image used for mongodb instances                                      | string   | None             |
| ami_filter             | the ami filter used to search for an image as a base for mongodb instances    | string   | None             |
| ami_owner              | the ami owner used to search for an image as a base for mongodb instances     | string   | None             |
| bastion_ami            | the ami image used for the bastion config host                                | string   | None             |
| bastion_ami_filter     | the ami filter used to search for an image as a base for the bastion host     | string   | None             |
| bastion_ami_owner      | the ami owner used to search for an image as a base for the bastion host      | string   | None             |
| aws_default_region     | the aws region                                                                | string   | us-east-1        |
| hostname_random        | generates random hostname base for the VM instances                           | string   | master           |
| bastion_config_destroy | destroys the bastion configuration host after configuration/build is finished | string   | true             |
| instance_type          | the instance_type for the VMs                                                 | string   | t3.micro         |
| disksize               | the disksize for the VM                                                       | string   | None             |
| mongodb_username       | the master mongodb username                                                   | string   | -random-         |
| mongodb_password       | the master mongodb password                                                   | string   | -random-         |
| volume_size            | the volume size for mongodb data                                              | string   | 100              |
| volume_mountpoint      | the volume mountpoint for mongodb data                                        | string   | /var/lib/mongodb |
| volume_fstype          | the volume fileystem type for mongodb data                                    | string   | xfs              |
| tags                   | the tags for the mongodb cluster in the Config0 resources database            | string   | None             |
| labels                 | the labels for the mongodb cluster in the Config0 resources database          | string   | None             |
| cloud_tags_hash | the tags for the resources in the cloud as base64                             | string  | None             |
| publish_to_saas   | publish info of db to Config0 UI                                              | boolean   | True             |
| do_region   | digital ocean region                 | string   | lon1         |
| doks_cluster_name            | digital ocean kubernetes name  | string |     | 
| doks_cluster_version         | digital ocean kubernetes version | string | 1.26.3-do.0
| doks_cluster_pool_size       | digital ocean kubernetes pool worker | string | s-1vcpu-2gb-amd
| doks_cluster_pool_node_count | digital ocean kubernetes node count  | number | 1
| doks_cluster_autoscale_max   | digital ocean kubernetes autoscale node max | number | 4
| doks_cluster_autoscale_min   | digital ocean kubernetes autoscale node min | number | 2
| ssh_key_id   | ssh key id for digital ocean            | string   | None         |
| hostname   | hostname/name for the droplet             | string   | None         |
| do_region   | digital ocean region             | string   | NYC1         |
| size   | droplet size             | string   | s-1vcpu-1gb         |
| with_backups   | with_backups        | string   | false         |
| with_monitoring   | with_monitoring        | string   | false         |
| with_ipv6   | with_ipv6        | string   | false         |
| with_private_networking   | with_private_networking        | string   | false         |
| with_resize_disk   | with_resize_disk        | string   | false         |
| key_name      | name of the ssh key                    | string   | None         |
| public_key    | public_key in base64                   | string   | None         |
| do_region   | the DO region | string   | NYC1         |
| size   | the size of the droplet | string   | s-1vcpu-2gb         |
| with_monitoring | the droplet with monitoring        | boolean   | true       |
| with_backups | the droplet with backups        | boolean   | None       |
| with_ipv6 | the droplet with ipv6        | boolean   | None       |
| with_private_networking | the droplet with private_networking        | boolean   | None       |
| with_resize_disk | the droplet with resize_disk        | boolean   | None       |
| vpc_name   | name of the vpc                 | string   | None         |
| vpc_id   | id of the vpc                 | string   | None         |
| subnet_ids   | the subnet_ids separated by comma - csv | string   | None         |
| sg_id   | the security group for EKS instance | string   | None         |
| bastion_sg_id   | the bastion security group for ec2 instance | string   | None         |
| workshop_name   | the name of the workshop | string   | None         |
| aws_default_region   | the default aws region               | string   | us-west-1         |
| eks_node_min_capacity   | the min capacity of the eks cluster               | string   | 1         |
| eks_node_max_capacity   | the max capacity of the eks cluster               | string   | 1         |
| eks_node_desired_capacity   | the desired capacity of the eks cluster               | string   | 1         |
| eks_instance_type   | the instance_type for the ec2 instance used to get through the workshop| string   | t3.micro         |
| disksize   | the disksize for the ec2 instance used to get through the workshop| string   | 25         |
| vpc_name   | name of the vpc                 | string   | None         |
| vpc_id   | id of the vpc                 | string   | None         |
| eks_cluster   | the name given to the eks cluster | string   | None         |
| role_name   | the aws role_name to access the eks cluster | string   | None         |
| subnet_ids   | the subnet_ids separated by comma - csv | string   | None         |
| aws_default_region   | the default aws region               | string   | us-west-1         |
| eks_min_capacity   | the min capacity of the eks cluster               | string   | 1         |
| eks_max_capacity   | the max capacity of the eks cluster               | string   | 1         |
| eks_desired_capacity   | the desired capacity of the eks cluster               | string   | 1         |
| eks_tf_release   | the Terraform EKS release template               | string   | v17.20.0         |
| cloud_tags_hash | the tags for the resources in the cloud as base64 | string  | None         |
| vpc_name   | name of the vpc                 | string   | None         |
| vpc_id   | id of the vpc                 | string   | None         |
| eks_cluster   | the name given to the eks cluster | string   | None         |
| role_name   | the aws role_name to access the eks cluster | string   | None         |
| subnet_ids   | the subnet_ids separated by comma - csv | string   | None         |
| aws_default_region   | the default aws region               | string   | us-west-1         |
| eks_min_capacity   | the min capacity of the eks cluster               | string   | 1         |
| eks_max_capacity   | the max capacity of the eks cluster               | string   | 1         |
| eks_desired_capacity   | the desired capacity of the eks cluster               | string   | 1         |
| eks_tf_release   | the Terraform EKS release template               | string   | v17.20.0         |
| cloud_tags_hash | the tags for the resources in the cloud as base64 | string  | None         |
| eks_cluster   | name of the eks                 | string   | None         |
| ci_environment | environment name for the project   | string   | None         |
| aws_default_region  | default aws region                                 |string    | eu-west-1 |
| bucket_acl          | bucket access control list mode                    |string    | private |
| bucket_expire_days  | bucket retention days                              |int       | 7 |
| cloud_tags_hash     | the tags for the resources in the cloud as base64  |string    | None |
| lambda_layers       | lambda amazon resource name                        |string    | arn:aws:lambda:eu-west-1:553035198032:layer:git-lambda2:8 |
| runtime             | lambda function runtime language                   |string    | python3.9 |
| suffix_id                  | suffix_id is added like a random string that makes the s3 buckets unique                          |string    | None |
| suffix_length              | the number of characters in suffix_id to use        |int       | 4 |
| ci_environment    | environment name for the project                                          | string   | None         |
| codebuild_name    | codebuild name for the project                                            | string   | None         |
| git_repo          | git repository that you want run codebuild ci on                          | string   | None         |
| git_url           | git repository link                                                       | string   | None         |
| project_id        | id of your codebuild project                                              | string   | None         |
| aws_default_region         | default aws region                                 |string    | us-west-1 |
| branch                     | git branch you are work on                         |string    | master |
| bucket_acl                 | bucket access control list mode                    |string    | private |
| bucket_expire_days         | bucket retention days                              |int       | 1 |
| build_image                | build image for codebuild project                  |string    | aws/codebuild/standard:5.0 |
| build_timeout              | build timeout for codebuild project                |int       | 444 |
| cloud_tags_hash            | the tags for the resources in the cloud as base64  |string    | None |
| compute_type               | compute type for codebuild project                 |string    | BUILD_GENERAL1_SMALL |
| docker_registry            | docker registry to upload images                   |string    | ecr |
| docker_repo_name           | docker repository name                             |string    | None |
| docker_repository_uri      | docker repository uri                              |string    | None |
| docker_token               | docker token                                       |string    | null |
| docker_username            | docker username                                    |string    | None |
| ecr_repo_name              | elastic container registry name                    |string    | None |
| ecr_repository_uri         | elastic container registry repository uri          |string    | None |
| github_token               | github token                                       |string    | null |
| image_type                 | image type for codebuild project                   |string    | LINUX_CONTAINER |
| privileged_mode            | run as root                                        |bool      | true |
| run_title                  | the run title for the Config0 UI                   |string    | codebuild_ci |
| secret                     | the secret for the webhook validation              |string    | _random |
| slack_channel              | name of the slack channel                          |string    | None |
| slack_webhook_hash         | slack channel webhook as base64                    |string    | null |
| suffix_id                  | suffix_id is added like a random string that makes the s3 buckets unique                          |string    | None |
| suffix_length              | the number of characters in suffix_id to use        |int       | 4 |
| trigger_id                 | job trigger id                                     |string    | _random |
| kafka_cluster   | the name of the kafka cluster       | string   | None         |
| num_of_zookeeper   | the num of zookeepers for the kafka cluster       | string   | 1         |
| num_of_broker   | the num of brokers for the kafka cluster       | string   | 1         |
| num_of_schema_registry   | the num of schema registries for the kafka cluster       | string   | 1         |
| num_of_connect   | the num of connect nodes for kafka cluster       | string   | 1         |
| num_of_rest   | the num of rest nodes for the kafka cluster       | string   | 1         |
| num_of_ksql   | the num of ksql nodes for the  kafka cluster       | string   | 1         |
| num_of_control_center   | the num of controls centers for the kafka cluster       | string   | 1         |
| vpc_id | the vpc id | string   | None       |
| subnet_ids   | a subnet for the VMs is selected from a list of the provided subnet_ids  | string in csv   | None         |
| sg_id   | the security group id for the VMs       | string   | None         |
| bastion_subnet_ids   | a subnet for the Bastion VM is selected from a list of the provided subnet_ids  | string in csv   | None         |
| bastion_sg_id   | the security group id for the bastion host       | string   | None         |
| spot   | the option to use spot intances. (buyer be aware)    | boolean   | None        |
| ami   | the ami image used for kafka instances      | string   | None        |
| ami_filter   | the ami filter used to search for an image as a base for kafka instances      | string   | None        |
| ami_owner   | the ami owner used to search for an image as a base for kafka instances      | string   | None        |
| bastion_ami   | the ami image used for the bastion config host      | string   | None          |
| bastion_ami_filter   | the ami filter used to search for an image as a base for the bastion host     | string   | None        |
| bastion_ami_owner   | the ami owner used to search for an image as a base for the bastion host      | string   | None        |
| aws_default_region   | the aws region                | string   | us-east-1         |
| instance_type | the instance_type for the VMs | string   | t3.micro       |
| disksize | the disksize for the VM | string   | None       |
| tags | the tags for the kafka cluster in the Config0 resources database | string   | None       |
| labels | the labels for the kafka cluster in the Config0 resources database | string   | None       |
| bastion_hostname       | hostname for the bastion used to install and configure kafka on VMs    | string   | None         |
| kafka_cluster          | name of the kafka cluster                                              | string   | None         |
| ssh_key_name           | name of the ssh_key_name to use for the VMs                            | string   | None         |
| aws_default_region     | default aws region                                                     | string   | us-east-1 |
| zookeeper_hosts        | kafka zookeeper hosts                                             | string   | None         |
| broker_hosts           | kafka broker hosts                                              | string   | None         |
| schema_registry_hosts  | kafka schema registry hosts                                       | string   | None         |
| connect_hosts          | kafka connect hosts                                              | string   | None         |
| rest_hosts             | kafka REST proxy hosts                                            | string   | None         |
| ksql_hosts             | kafka KafkaSQL hosts                                             | string   | None         |
| control_center_hosts   | kafka control center hosts                                      | string   | None         |
| vm_username                 | username for the VM        | string  | ubuntu                                |
| publish_to_saas             | publish or print vm info to saas ui                 | boolean | null                                  |
| terraform_docker_exec_env   | docker container for terraform execution            | string  | elasticdev/terraform-run-env:1.3.7    |
| ansible_docker_exec_env     | docker container for ansible execution              | string  | elasticdev/ansible-run-env            |
| gitlab_project_name   | the name of the project | string   | None         |
| group_id   | group id of subgroup | string   | None         |
| visibility_level   | visibility_level of the subgroup | string   | public         |
| group_name   | name of the subgroup | string   | None         |
| parent_id   | parent_id of the parent group | string   | None         |
| visibility_level   | visibility_level of the subgroup | string   | public         |
| group_path   | path of the subgroup | string   | None         |
| topic_name   | the name of the sns topic to trigger lambda function             | string   |        |
| lambda_name   | the lambda function to trigger when codebuild completes               | string   |        |
| aws_default_region   | default aws region               | string   | us-east-1         |
| cloud_tags_hash | the tags for the resources in the cloud as base64 | string  | None         |
| hostname  | hostname to be stopped  | string   | None     |
| aws_default_region   | default aws region               | string   | us-east-1         |
| key_name   | name of the ssh key                 | string   | None         |
| name   | name of the ssh key                 | string   | None         |
| public_key   | public_key in base64                | string   | None         |
| config0_lambda_execgroup_name   | name of lambda of exec group | string   | None         |
| lambda_name   | name lambda function                 | string   | None         |
| s3_bucket   | s3_bucket | string   | None         |
| aws_default_region   | default aws region               | string   | us-east-1         |
| cloud_tags_hash | the tags for the resources in the cloud as base64 | string  | None         |
| vpc_name   | name of the vpc                 | string   | None         |
| gcloud_region        | google region to create the subnets          | string    | us-west1       |
| cloud_tags_hash | the tags for the resources in the cloud as base64 | string  | None         |
| config_env      | the environmental where the ami information can be found     | choices: public,private   | private    |
| aws_default_region      | aws region - must be the same as where the hostname resides      | string   | us-east-1         |
| shelloutconfig      | shelloutconfig for creating ami      | string   | config0-hub:::aws::ec2_ami         |
| wait_last_run      | the time interval to check the status of the ami between retries    | int   | 60 |
| retries      | the number of retries to check the status of the ami. if you put -1, retries is infinite.    | int   | 20 |
| timeout      | the total time allocated to wait before considering the ami will never be available. | int   | 1800 |
| config_env      | the environmental where the ami information can be found     | choices: public,private   | private    |
| aws_default_region      | aws region - must be the same as where the hostname resides      | string   | us-east-1         |
| shelloutconfig      | shelloutconfig for creating ami      | string   | config0-hub:::aws::ec2_ami         |
| role_name   | role_name                  | string   | None         |
| iam_instance_profile   | iam_instance_profile                  | string   | None         |
| iam_role_policy_name   | iam_role_policy_name                  | string   | None         |
| aws_default_region   | aws_default_region   | string   | us-east-1         |
| assume_policy   | the overall the assume_policy in a json string serialized in base64    | string   | None         |
| policy   | the overall the policy in a json string serialized in base64    | string   | None         |
| key_name   | name of the ssh key                 | string   | None         |
| hostname   | hostname of the ec2 server                 | string   | None         |
| ssh_key_name   | key_name for the ec2 server                 | string   | None         |
| aws_default_region   | default aws region               | string   | us-east-1         |
| vpc_id   | the vpc_id to be used        | string    | None |
| subnet_id   | the subnet_id to be used        | string    | None |
| security_group_ids   | the security_group_ids to be used        | csv (string)    | None |
| config_network   | the configuration network                | choice public/private   | private |
| register_to_db   | register the ec2 instance to Config0               | boolean   | True |
| ami   | the ami ami               | string   | None |
| ami_filter   | the AMI filter used for searches      | string       | Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-\*  | 
| ami_owner   | the AMI owner used for searches        | string    | 099720109477 (canonical) |
| instance_type   | the instance type        | string    | t2.micro |
| disksize   | the instance root disk size        | integer    | 40 |
| volume_name   | the name of volume to be attached        | string    | None |
| volume_size   | the size of volume to be created        | integer    | None |
| volume_mount   | the mount point of the extra volume        | string    | None |
| volume_fstype   | the fileystem of the extra volume        | string    | None |
| iam_instance_profile   | the iam_instance_profile to attach to ec2 instance        | string    | None |
| user_data   | the user_data encoding in base64        | string    | None |
| cloud_tags_hash | the tags for the resources in the cloud as base64 | string  | None         |
| vpc_name   | name of the vpc                 | string   | None         |
| gcloud_region        | google region to create the subnets          | string    | us-west1       |
| cloud_tags_hash | the tags for the resources in the cloud as base64 | string  | None         |
| s3_bucket   | s3 bucket for codebuild               | string   |        |
| s3_bucket_cache   | s3 bucket for codebuild cache (docker related)               | string   |        |
| codebuild_name   | codebuild name for the project               | string   |        |
| aws_default_region   | default aws region               | string   | us-east-1         |
| buildspec_hash | buildspec for codebuild as base64 hash | string   | None         |
| prebuild_hash | prebuild stage for codebuild as base64 hash | string   | None         |
| build_hash | build stage for codebuild as base64 hash | string   | None         |
| postbuild_hash | postbuild stage for codebuild as base64 hash | string   | None         |
| codebuild_env_vars_hash | the environmental variables for codebuild as base64 | string  | None         |
| cloud_tags_hash | the tags for the resources in the cloud as base64 | string  | None         |
| ssm_params_hash | ssm parameters to inserted (already uploaded) as base64 | string  | None         |
| description   | description for the project               | string   |        |
| privileged_mode   | privileged_mode for the docker builds               | string   |  true      |
| image_type   | image_type for codebuild project               | string   |  LINUX_CONTAINER      |
| build_image   | build_image for codebuild project               | string   |  aws/codebuild/standard:5.0      |
| build_timeout   | build_timeout for codebuild project               | string   |  5  |
| compute_type   | compute_type for codebuild project               | string   |  BUILD_GENERAL1_SMALL  |
| docker_registry   | docker_registry to upload images | string   |  None(ecr)  |
| publish_to_saas   | publish codebuild project to the UI | boolean   |  None  |
| policy_name   | policy name                 | string   | None         |
| iam_name   | iam name                 | string   | None         |
| allows_hash   | the allows statement as a 64 hash | string   | see_below |
| denies_hash   | the denies statement as a 64 hash | string   | see_below |
| hostname   | hostname of the ec2 server                 | string   | None         |
| ssh_key_name   | key_name for the ec2 server                 | string   | None         |
| aws_default_region   | default aws region               | string   | us-east-1         |
| vpc_id   | the vpc_id to be used        | string    | None |
| subnet_id   | the subnet_id to be used        | string    | None |
| security_group_ids   | the security_group_ids to be used        | csv (string)    | None |
| config_network   | the configuration network                | choice public/private   | private |
| register_to_db   | register the ec2 instance to Config0               | boolean   | True |
| ami   | the ami ami               | string   | None |
| ami_filter   | the AMI filter used for searches      | string       | Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-\*  | 
| ami_owner   | the AMI owner used for searches        | string    | 099720109477 (canonical) |
| instance_type   | the instance type        | string    | t2.micro |
| disksize   | the instance root disk size        | string    | 40 |
| volume_name   | the name of volume to be attached        | string    | None |
| volume_size   | the size of volume to be created        | string    | None |
| volume_mount   | the mount point of the extra volume        | string    | None |
| volume_fstype   | the fileystem of the extra volume        | string    | None |
| iam_instance_profile   | the iam_instance_profile to attach to ec2 instance        | string    | None |
| user_data   | the user_data encoding in base64        | string    | None |
| cloud_tags_hash | the tags for the resources in the cloud as base64 | string  | None         |
| vpc_name   | name of the vpc                 | string   | None         |
| vpc_id   | id of the vpc                 | string   | None         |
| subnet_ids   | the subnet_ids separated by comma - csv | string   | None         |
| sg_id   | the security group for EKS instance | string   | None         |
| bastion_sg_id   | the bastion security group for ec2 instance | string   | None         |
| docker_host   | the docker host | string   | None         |
| aws_default_region   | the default aws region               | string   | us-west-1         |
| instance_type   | the instance_type for the ec2 instance used to get through the workshop| string   | t3.micro         |
| disksize   | the disksize for the ec2 instance used to get through the workshop| string   | 25         |
| resource_type   | the resource type       | string   |    |
| name   | the name resource | string   |    |
| match_hash   | the json match dictionary converted to b64 hash | string   |    |
| ref_schedule_id   | the reference schedule_id for the query | string   |    |
| publish_keys_hash   | the keys to publish converted to b64  | string   |    |
| map_keys_hash   | map keys b64 (dict) is use to change the key name that shows up on the UI (b64) | string   |    |
| prefix_key   | prefix for each key (b64) | string   |    |
