**Description**

  - This stack creates a Kafka cluster using virtual machines (VMs) within a protected private network, utilizing a bastion host for access.

**Infrastructure**

  - Usually, this stack is invoked by an upstream stack like config-publish:::kafka_on_ec2.
  - This stack assumes that the bastion hosts and Kafka VMs have already been created and registered in the user's Config0 resource database.
  - This stack assumes that the specified ssh_key_name has already been inserted into the VMs, typically by the cloud provider.

**Required**

| argument               | description                                                                    | var type | default      |
|------------------------|--------------------------------------------------------------------------------| -------- | ------------ |
| bastion_hostname       | hostname for the bastion used to install and configure kafka on VMs    | string   | None         |
| kafka_cluster          | name of the kafka cluster                                              | string   | None         |
| ssh_key_name           | name of the ssh_key_name to use for the VMs                            | string   | None         |
| aws_default_region     | default aws region                                                     | string   | help-add-description-2023         |
| zookeeper_hosts        | name of the zookeeper host                                             | string   | None         |
| broker_hosts           | name of the kafka broker                                               | string   | None         |
| schema_registry_hosts  | name of the schema registry host                                       | string   | None         |
| connect_hosts          | help-add-description-2023                                              | string   | None         |
| rest_hosts             | name of the REST proxy host                                            | string   | None         |
| ksql_hosts             | name of the KafkaSQL host                                              | string   | None         |
| control_center_hosts   | name of the kafka control center                                       | string   | None         |

**Optional**

| argument               | description                                                                    | var type | default      |
|------------------------|--------------------------------------------------------------------------------| -------- | ------------ |
| vm_username                 | username for the VM.  e.g. ec2 for AWS linux        | string  | ubuntu                                |
| publish_to_saas             | publish or print vm info to saas ui                 | boolean | null                                  |
| terraform_docker_exec_env   | docker container for terraform execution            | string  | elasticdev/terraform-run-env:1.3.7    |
| ansible_docker_exec_env     | docker container for ansible execution              | string  | elasticdev/ansible-run-env            |
