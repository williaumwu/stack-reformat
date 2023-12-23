**Description**

  - This stack creates a Kafka cluster using virtual machines (VMs) within a protected private network, utilizing a bastion host for access.

**Infrastructure**

  - Usually, this stack is invoked by an upstream stack like config-publish:::kafka_on_ec2.
  - This stack assumes that the bastion hosts and Kafka VMs have already been created and registered in the user's Config0 resource database.
  - This stack assumes that the specified ssh_key_name has already been inserted into the VMs, typically by the cloud provider.

**Required**

| argument               | description                                                                    | var type | default      |
|------------------------|--------------------------------------------------------------------------------| -------- | ------------ |
| tbd                    | tbd                                              | string   | None         |

**Optional**

| argument               | description                                                                    | var type | default      |
|------------------------|--------------------------------------------------------------------------------| -------- | ------------ |
| tbd                    | tbd                                              | string   | None         |
