**Description**

  - This stack connects an EKS node group to an existing EKS cluster.

**Infrastructure**

  - This stack assumes the presence of an existing EKS cluster within the Config0 resources table.

**Required**

| argument      | description                            | var type | default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| eks_cluster              | name given to the eks cluster | string | None |
| eks_node_ami_type        | ami image used for eks instances | AL2_x86_64 <br> AL2_x86_64_GPU <br> AL2_ARM_64 <br> CUSTOM | AL2_x86_64 |
| eks_node_capacity_type   | pricing type for spinning eks instances | ON_DEMAND <br> SPOT | ON_DEMAND |
| eks_subnet_ids           | the subnet ids separated by comma - csv | string | None |

**Optional**

| argument           | description                            | var type |  default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| aws_default_region          | default aws region | string| eu-west-1 |
| eks_node_desired_capacity   | desired capacity of the eks cluster | int | 1 |
| eks_node_disksize           | disksize for the eks instance | int | 25 |
| eks_node_group_name         | eks instance group name | string | null |
| eks_node_instance_types     | eks instance type | list | t3.medium |
| eks_node_max_capacity       | max capacity of the eks cluster | int | 2 |
| eks_node_min_capacity       | min capacity of the eks cluster | int | 1 |
| eks_node_role_arn           | eks instance amazon resrouce name | string | None |
| timeout                     | total time allocated to wait before considering the ami will never be available | int | 1800 |