| argument | description | var type | default |
| ------------- | -------------------------------------- | -------- | ------------ |
| acl | acl for bucket | private/public | private |
| active | webhook is active or not | true | None |
| allocated_storage | the rds storage size | string | 10 |
| allow_major_version_upgrade | allow_major_version_upgrade for rds | string | true |
| allows_hash | the allows statement as a 64 hash | string | see_below |
| ami | the ami image used for kafka instances | string | None |
| ami | the ami image used for mongodb instances | string | None |
| ami | the ami image used for VM | string | None |
| ami_filter | the AMI filter used for searches | string | Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-\* | 
| ami_filter | the ami filter used to search for an image as a base for kafka instances | string | None |
| ami_filter | the ami filter used to search for an image as a base for mongodb instances | string | None |
| ami_filter | the ami filter used to search for an image as a base for VM | string | None |
| ami_owner | the AMI owner used for searches | string | 099720109477 (canonical) |
| ami_owner | the ami owner used to search for an image as a base for kafka instances | string | None |
| ami_owner | the ami owner used to search for an image as a base for mongodb instances | string | None |
| ami_owner | the ami owner used to search for an image as a base for VM | string | None |
| ansible_docker_exec_env | docker container for ansible execution | string | elasticdev/ansible-run-env |
| ansible_docker_exec_env | overide the default the docker runtime to execute ansible used to install jenkins | string | elasticdev/ansible-run-env |
| ansible_docker_exec_env | the docker container for ansible execution | string | elasticdev/ansible-run-env |
| argument      | description                            | var type | default      |
| arguments_hash | arguments key/value (dict) converted to base64 hash | string |     |
| assume_policy | the overall the assume_policy in a json string serialized in base64 | string | None |
| auto_minor_version_upgrade | auto_minor_version_upgrade for rds | string | true |
| aws_default_region | aws region - must be the same as where the hostname resides | string | us-east-1 |
| aws_default_region | aws region to create the ecr repo | string | us-east-1 |
| aws_default_region | default aws region | string | us-east-1 |
| aws_default_region | default aws region |string | eu-west-1 |
| aws_default_region | default aws region |string | us-west-1 |
| basename | the basename for the mongodb hostname [^1] | string | None |
| bastion_ami | the ami image used for the bastion config host | string | None |
| bastion_ami_filter | the ami filter used to search for an image as a base for the bastion host | string | None |
| bastion_ami_owner | the ami owner used to search for an image as a base for the bastion host | string | None |
| bastion_config_destroy | destroys the bastion configuration host after configuration/build is finished | string | true |
| bastion_hostname | hostname for the bastion used to install and configure kafka on VMs | string | None |
| bastion_hostname | the hostname for the bastion used to install and configure mongodb on VMs | string | None |
| bastion_sg_id | the bastion security group for ec2 instance | string | None |
| bastion_sg_id | the security group id for the bastion host | string | None |
| bastion_sg_id | the security group id used for the bastion config host | string | bastion |
| bastion_subnet_ids | a subnet for the Bastion VM is selected from a list of the provided subnet_ids | string in csv | None |
| bastion_subnet_ids | the subnet id(s) in CSV used for the bastion config host | string | private |
| bastion_subnet_ids | the subnet_ids to select a subnet_id for the bastion host | string in csv | None |
| billing_mode | pay per request | string |  PAY_PER_REQUEST | 
| branch | git branch you are work on |string | master |
| broker_hosts | kafka broker hosts | string | None |
| bucket | bucket in aws | string | random |
| bucket_acl | bucket access control list mode |string | private |
| bucket_expire_days | bucket retention days |int | 1 |
| bucket_expire_days | bucket retention days |int | 7 |
| build_hash | build stage for codebuild as base64 hash | string | None |
| build_image | build image for codebuild project |string | aws/codebuild/standard:5.0 |
| build_timeout | build timeout for codebuild project |int | 444 |
| build_timeout | build_timeout for codebuild project | string |  5 |
| buildspec_hash | buildspec for codebuild as base64 hash | string | None |
| ci_environment | environment name for the project | string | None |
| cloud_tags_hash | tags for the resources in the cloud as base64 | string | None |
| cloud_tags_hash | the tags for the resources in the cloud as base64 |string | None |
| codebuild_env_vars_hash | the environmental variables for codebuild as base64 | string | None |
| codebuild_name | codebuild name for the project | string | None |
| compute_type | compute type for codebuild project |string | BUILD_GENERAL1_SMALL |
| config_env | the environmental where the ami information can be found | choices: public,private | private |
| config_network | the configuration network | choice public/private | private |
| config_network | the network to push configuration to mongodb hosts | private/public | private |
| config0_lambda_execgroup_name | name of lambda of exec group | string | None |
| connect_hosts | kafka connect hosts | string | None |
| content_type | content_type of webhook | json | None |
| control_center_hosts | kafka control center hosts | string | None |
| db_instance_name | name of the RDS instance | string | None |
| db_name | db name | string | None |
| db_name | the db_name to create in rds | string | random |
| db_password | the password of the db | string | None |
| db_root_password | root password RDS | string | None |
| db_root_user | root user for RDS | string | None |
| db_user | the user of the db | string | None |
| denies_hash | the denies statement as a 64 hash | string | see_below |
| description | description for the project | string |     |
| device_name | the device name for the extra data volume for mongodb data | string | /dev/xvdc |
| device_name | the device name for the volume | string | /dev/xvdc |
| disksize | the disksize for the ec2 instance used to get through the workshop| string | 25 |
| disksize | the disksize for the VM | string | None |
| disksize | the instance root disk size | integer | 40 |
| disksize | the instance root disk size | string | 40 |
| do_region | digital ocean region | string | lon1 |
| do_region | digital ocean region | string | NYC1 |
| do_region | the DO region | string | NYC1 |
| docker_exec_env | the docker container for terraform execution | string | elasticdev/terraform-run-env |
| docker_exec_env | the docker container to execute the underlying Terraform templates | string | elasticdev/terraform-run-env |
| docker_host | the docker host | string | None |
| docker_registry | docker registry to upload images |string | ecr |
| docker_registry | docker_registry to upload images | string |  None(ecr) |
| docker_repo | name of the repository with a key "docker_repo | string | None |
| docker_repo_name | docker repository name |string | None |
| docker_repository_uri | docker repository uri |string | None |
| docker_token | docker token |string | null |
| docker_username | docker username |string | None |
| doks_cluster_autoscale_max | digital ocean kubernetes autoscale node max | number | 4 |
| doks_cluster_autoscale_min | digital ocean kubernetes autoscale node min | number | 2 |
| doks_cluster_name | digital ocean kubernetes name | string |     | 
| doks_cluster_pool_node_count | digital ocean kubernetes node count | number | 1 |
| doks_cluster_pool_size | digital ocean kubernetes pool worker | string | s-1vcpu-2gb-amd |
| doks_cluster_version | digital ocean kubernetes version | string | 1.26.3-do.0 |
| dst_exec_group | the execgroup to execute | string |     |
| dynamodb_name | name of the dynamodb table | string |     |
| ecr_repo_name | elastic container registry name |string | None |
| ecr_repository_uri | elastic container registry repository uri |string | None |
| eks_cluster | name given to the eks cluster | string | None |
| eks_cluster | name of the eks | string | None |
| eks_cluster | provide an EKS cluster if vpc requires eks settings | string |     |
| eks_cluster | the name given to the eks cluster | string | None |
| eks_desired_capacity | the desired capacity of the eks cluster | string | 1 |
| eks_instance_type | the instance_type for the ec2 instance used to get through the workshop| string | t3.micro |
| eks_max_capacity | the max capacity of the eks cluster | string | 1 |
| eks_min_capacity | the min capacity of the eks cluster | string | 1 |
| eks_node_ami_type | ami image used for eks instances | CUSTOM | AL2_x86_64 |
| eks_node_capacity_type | pricing type for spinning eks instances | ON_DEMAND <br> SPOT | ON_DEMAND |
| eks_node_desired_capacity | desired capacity of the eks cluster | int | 1 |
| eks_node_desired_capacity | the desired capacity of the eks cluster | string | 1 |
| eks_node_disksize | disksize for the eks instance | int | 25 |
| eks_node_group_name | eks instance group name | string | null |
| eks_node_instance_types | eks instance type | list | t3.medium |
| eks_node_max_capacity | max capacity of the eks cluster | int | 2 |
| eks_node_max_capacity | the max capacity of the eks cluster | string | 1 |
| eks_node_min_capacity | min capacity of the eks cluster | int | 1 |
| eks_node_min_capacity | the min capacity of the eks cluster | string | 1 |
| eks_node_role_arn | eks instance amazon resrouce name | string | None |
| eks_subnet_ids | the subnet ids separated by comma - csv | string | None |
| eks_tf_release | the Terraform EKS release template | string | v17.20.0 |
| enable_dns_hostnames | enable dns hostnames | string |     |
| enable_lifecycle | enable_lifecycle for bucket | string | None |
| enable_nat_gateway | enable nat gateway | string |     |
| engine | the rds engine | string | MySQL |
| engine_version | the rds engine version | string | 5.7 |
| env_vars_hash | environment variables key/value (dict) converted to base64 hash | string |     |
| environment | the environment | string | dev |
| evaluate | whether to evaluate to queries to immediate values | null/True | null |
| events | events of to invoke webhook | push,pull_request | None |
| expire_days | expire_days for bucket assets only if lifecycle is enabled | int | None |
| force_destroy | force_destroy for bucket if destroying| string | None |
| gcloud_region | google region to create the subnets | string | us-west1 |
| git_repo | git repository that you want run codebuild ci on | string | None |
| git_url | git repository link | string | None |
| github_token | github token |string | null |
| gitlab_project_name | the name of the project | string | None |
| group_id | group id of subgroup | string | None |
| group_name | name of the subgroup | string | None |
| group_path | path of the subgroup | string | None |
| handler | lambda function handler | string | app.handler |
| hash_key | the hash key of the dynamodb table | string |  \_id |
| hash_key | the hash_key for the dynamodb table | string |     |
| hostname | hostname of the ec2 server | string | None |
| hostname | hostname to be stopped | string | None |
| hostname | hostname/name for the droplet | string | None |
| hostname | the hostname | string | None |
| hostname | the hostname of the server to bootstrap | string | None |
| hostname | the hostname to install jenkins | string | None |
| hostname | the hostname to mount the volume | string | None |
| hostname_random | generates random hostname base for the VM instances | string | master |
| iam_instance_profile | iam_instance_profile | string | None |
| iam_instance_profile | the iam_instance_profile to attach to ec2 instance | string | None |
| iam_name | iam name | string | None |
| iam_role_policy_name | iam_role_policy_name | string | None |
| image | the ami image | string | None |
| image_filter | the image filter used for searches | string | Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-\* |
| image_owner | the image owner used for searches | string | 099720109477 (canonical) |
| image_type | image type for codebuild project |string | LINUX_CONTAINER |
| insecure_ssl | allowed insecure ssl connection | true | None |
| instance_class | the instance_class for rds instance | string | db.t2.micro |
| instance_type | the instance type | string | t2.micro |
| instance_type | the instance_type for the ec2 instance used to get through the workshop| string | t3.micro |
| instance_type | the instance_type for the VMs | string | t3.micro |
| ip_key | the ip_key from boto used for connection | public_ip/private_ip | public_ip |
| ip_key | the ip_key refers to private or public networks | public_ip/private_ip | public_ip |
| item_hash | json/dictionary item as a base64 | string |     |
| kafka_cluster | name of the kafka cluster | string | None |
| kafka_cluster | the name of the kafka cluster | string | None |
| key | the key used to show on the UI for the contents of the remote file e.g. password | string | None |
| key_name | name of the ssh key | string | None |
| ksql_hosts | kafka KafkaSQL hosts | string | None |
| labels | Config0 resource labels for the vpc | string | None |
| labels | the labels for the kafka cluster in the Config0 resources database | string | None |
| labels | the labels for the mongodb cluster in the Config0 resources database | string | None |
| labels | the labels for the VM | string | None |
| labels | the labels for the vpc.  this is typically needed for EKS | string |     |
| labels_hash | query labels key/value (dict) converted to base64 hash | string |     |
| labels_hash | the json labels dictionary converted to b64 hash | string |     |
| lambda_env_vars_hash | lambda function environment variables as base64 | string | None |
| lambda_layers | lambda amazon resource name |string | arn:aws:lambda:eu-west-1:553035198032:layer:git-lambda2:8 |
| lambda_name | name lambda function | string | None |
| lambda_name | the lambda function to trigger when codebuild completes | string |     |
| lambda_timeout | total time allocated to wait before the function times out | int | 300 |
| main_network_block | the cidr for the main network nat | string | 10.9.0.0/16 |
| map_keys_hash | map keys b64 (dict) is use to change the key name that shows up on the UI (b64) | string |     |
| master_password | the master password for rds | string | random |
| master_username | the master username for rds | string | random |
| match_hash | the json match dictionary converted to b64 hash | string |     |
| memory_size | lambda function allocated memory size | int | 256 |
| mongodb_bind_ip | the bind ip for mongodb to listen | string | 0.0.0.0 |
| mongodb_cluster | the name of the mongodb cluster | string | None |
| mongodb_data_dir | the directory for mongodb data | string | /var/lib/mongodb |
| mongodb_hosts | the hostnames for he mongodb_hosts in the replica set separated by a comma | string (csv) | None |
| mongodb_logpath | the logpath for mongodb | string | /var/log/mongodb/mongod.log |
| mongodb_password | the master mongodb password | string | -random- |
| mongodb_port | the port for mongodb | string | 27017 |
| mongodb_storage_engine | the storage engine for mongodb | string | wiredTiger |
| mongodb_username | the master mongodb username | string | -random- |
| mongodb_version | the mongodb version to install | string | 4.2 |
| mongodb_version | the version for mongodb | string | 4.0.3 |
| multi_az | sets multi placement zone for rds | string | false |
| name | name of the repository | string | None |
| name | name of the ssh key | string | None |
| name | name of the webhook | string | None |
| name | the name resource | string |     |
| nat_gw_tags | AWS tags for the nat gw | string |     |
| noncurrent_version_expiration | noncurrent_version_expiration for bucket assets only if lifecycle is enabled | int | None |
| num_of_broker | the num of brokers for the kafka cluster | string | 1 |
| num_of_connect | the num of connect nodes for kafka cluster | string | 1 |
| num_of_control_center | the num of controls centers for the kafka cluster | string | 1 |
| num_of_ksql | the num of ksql nodes for the  kafka cluster | string | 1 |
| num_of_replicas | the number of replicas in the mongodb cluster | integer | 1 |
| num_of_rest | the num of rest nodes for the kafka cluster | string | 1 |
| num_of_schema_registry | the num of schema registries for the kafka cluster | string | 1 |
| num_of_zookeeper | the num of zookeepers for the kafka cluster | string | 1 |
| one_nat_gateway_per_az | set true if you want one nat gateway per az (more expensive) | string |     |
| parent_id | parent_id of the parent group | string | None |
| policy | the overall the policy in a json string serialized in base64 | string | None |
| policy_name | policy name | string | None |
| policy_template_hash | lambda function policy template as base64 | string | None |
| port | the port for rds instance | string | 3306 |
| postbuild_hash | postbuild stage for codebuild as base64 hash | string | None |
| prebuild_hash | prebuild stage for codebuild as base64 hash | string | None |
| prefix_key | prefix for each key (b64) | string |     |
| private_subnet_tags | AWS tags for the private subnet | string |     |
| privileged_mode | privileged_mode for the docker builds | string |  true |
| privileged_mode | run as root |bool | true |
| project_id | id of your codebuild project | string | None |
| public_key | public_key in base64 | string | None |
| public_subnet_tags | AWS tags for the public subnet | string |     |
| publicly_accessible | makes rds publicly accessible | string | false |
| publish_creds | publish the credentials for mongodb for Config0 output in UI | string | True |
| publish_creds | show credentials on the Config0 dashboard | string | True |
| publish_creds | whether to display credentials on the Config0 dashboard | boolean | True |
| publish_keys_hash | the keys to publish converted to b64 | string |     |
| publish_private_key | if set true, the private key in base64 hash will show on the Config0 UI | string | None |
| publish_to_saas | publish codebuild project to the UI | boolean |  None |
| publish_to_saas | publish info of db to Config0 UI | boolean | True |
| publish_to_saas | publish or print vm info to saas ui | boolean | None |
| publish_to_saas | publish or print vm info to saas ui | boolean | null |
| rds_name | the name given to the rds instance | string | None |
| read_only | read_only (true/false) | boolean | true |
| ref_schedule_id | the reference schedule_id for the query | string |     |
| register_to_db | register the ec2 instance to Config0 | boolean | True |
| remote_file | the fully qualified remote file to get the contents from | string | None |
| repo | github repository | string | None |
| resource_name | the resource name | string |     |
| resource_type | the resource type | string |     |
| rest_hosts | kafka REST proxy hosts | string | None |
| retries | the number of retries to check the status of the ami. if you put -1, retries is infinite | int | 20 |
| reuse_nat_ips | reuse nat ips | string |     |
| role_name | role_name | string | None |
| role_name | the aws role_name to access the eks cluster | string | None |
| run_title | the run title for the Config0 UI |string | codebuild_ci |
| runtime | lambda function runtime language | string | python3.9 |
| runtime | lambda function runtime language |string | python3.9 |
| s3_bucket | s3 bucket for codebuild | string |     |
| s3_bucket | s3_bucket | string | None |
| s3_bucket_cache | s3 bucket for codebuild cache (docker related) | string |     |
| s3_key | s3 bucket key | string | None |
| schema_registry_hosts | kafka schema registry hosts | string | None |
| secret | the secret for the webhook validation |string | _random |
| secret | the secret to verify the webook | [auto-generated-random] | None |
| security_group | the security group names for the ec2 instance | list | None |
| security_group_ids | the security group ids for the ec2 instance | list | None |
| security_group_ids | the security_group_ids to be used | csv (string) | None |
| sg_id | security group id for the VMs | string | None |
| sg_id | the security group for EKS instance | string | None |
| sg_id | the security group id for the rds instance | string | None |
| sg_id | the security group id for the VMs | string | None |
| sg_id | the single security group id for the ec2 instance | string | None |
| shelloutconfig | shelloutconfig for creating ami | string | config0-hub:::aws::ec2_ami |
| single_nat_gateway | single nat gateway | string |     |
| size | droplet size | string | s-1vcpu-1gb |
| size | the instance size | string | t2.micro |
| size | the size of the droplet | string | s-1vcpu-2gb |
| skip_final_snapshot | skip_final_snapshot for rds when destroying | string | true |
| slack_channel | name of the slack channel |string | None |
| slack_webhook_hash | slack channel webhook as base64 |string | null |
| spot | the option to use spot intances. (buyer be aware) | boolean | None |
| spot | the option to use spot VM. (buyer be aware) | boolean | None |
| spot_max_price | the option to set spot max price spot instances | string | None |
| spot_type | the option to set spot type for spot instances | string | persistent |
| ssh_key_id | ssh key id for digital ocean | string | None |
| ssh_key_name | key_name for the ec2 server | string | None |
| ssh_key_name | name of the ssh_key_name to use for the VMs | string | None |
| ssh_key_name | ssh_key_name for the ec2 server | string | None |
| ssh_key_name | the name the ssh_key_name to use for the VMs | string | None |
| ssh_key_name | the ssh key name for the VMs | string | None |
| ssh_key_name | the ssh key name use to authenticate to server | string | None |
| ssh_key_name | the ssh_key_name to log into hostname | string | None |
| ssh_key_name | the ssh_key_name to log into jenkins | string | None |
| ssm_description | ssm description for the parameter store | string | None |
| ssm_key | ssm key for the parameter store | string | random |
| ssm_params_hash | ssm parameters to inserted (already uploaded) as base64 | string | None |
| ssm_type | ssm type for the parameter store | choice | SecureString(default),String |
| ssm_value | ssm value for the parameter store | string | None |
| storage_encrypted | encrypt storage for rds | string | false |
| storage_type | storage type for rds | string | gp2 |
| subnet | the name of subnet to be used | string | None |
| subnet_id | the subnet_id to be used | string | None |
| subnet_ids | a subnet for the VMs is selected from a list of the provided subnet_ids | string in csv | None |
| subnet_ids | the subnet id(s) in CSV used for the mongodb servers | string | private |
| subnet_ids | the subnet_ids separated by comma - csv - for rds instance | string | None |
| subnet_ids | the subnet_ids separated by comma - csv | string | None |
| subnet_ids | the subnet_ids to select from | string (csv) | None |
| suffix_id | suffix_id is added like a random string that makes the s3 buckets unique |string | None |
| suffix_length | the number of characters in suffix_id to use |int | 4 |
| table_name | the dynamodb table | string |     |
| tags | Config0 resource tags for the vpc | string | None |
| tags | the tags for the kafka cluster in the Config0 resources database | string | None |
| tags | the tags for the mongodb cluster in the Config0 resources database | string | None |
| tags | the tags for the VM | string | None |
| tags | the tags for the vpc.  this is typically needed for EKS | string |     |
| terraform_docker_exec_env | docker container for terraform execution | string | elasticdev/terraform-run-env:1.3.7 |
| terraform_docker_exec_env | the docker container for terraform execution | string | elasticdev/terraform-run-env |
| tier_level | "2" or "3" tier for security groups | string |     |
| tier_level | the tier_level | choice 2/3 | None |
| timeout | the total time allocated to wait before considering the ami will never be available | int | 1800 |
| topic_name | the name of the sns topic to trigger lambda function | string |     |
| trigger_id | job trigger id |string | _random |
| url | the designated url for the webook | string | None |
| user | the user to log into the server with | string | ubuntu |
| user_data | the user_data encoding in base64 | string | None |
| vars_set_name | the name of the variables set | string |     |
| versioning | versioning for bucket assets| string | None |
| visibility_level | visibility_level of the subgroup | string | public |
| vm_username | The username for the VM.  e.g. ec2 for AWS linux | string | master |
| vm_username | username for the VM | string | ubuntu |
| volume_fstype | the fileystem of the extra volume | string | None |
| volume_fstype | the fileystem type for volume used for mongodb data | string | xfs |
| volume_fstype | the volume fileystem type for mongodb data | string | xfs |
| volume_mount | the mount point of the extra volume | string | None |
| volume_mountpoint | the volume mountpoint for mongodb data | string | /var/lib/mongodb |
| volume_name | the name of volume to be attached | string | None |
| volume_name | the volume_name to mount on the hostname | string | <hostname>-name |
| volume_size | the size of volume to be created | integer | None |
| volume_size | the volume size for mongodb data | string | 100 |
| vpc_id | id of the vpc | string | None |
| vpc_id | the vpc id | string | None |
| vpc_id | the vpc_id to be used | string | None |
| vpc_name | name of the vpc | string | None |
| vpc_name | the name of vpc to be used | string | None |
| vpc_tags | AWS tags for the vpc | string |     |
| wait_last_run | the time interval to check the status of the ami between retries | int | 60 |
| with_backups | the droplet with backups | boolean | None |
| with_backups | with_backups | string | false |
| with_ipv6 | the droplet with ipv6 | boolean | None |
| with_ipv6 | with_ipv6 | string | false |
| with_monitoring | the droplet with monitoring | boolean | true |
| with_monitoring | with_monitoring | string | false |
| with_private_networking | the droplet with private_networking | boolean | None |
| with_private_networking | with_private_networking | string | false |
| with_resize_disk | the droplet with resize_disk | boolean | None |
| with_resize_disk | with_resize_disk | string | false |
| workshop_name | the name of the workshop | string | None |
| zookeeper_hosts | kafka zookeeper hosts | string | None |