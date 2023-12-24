**Description**

  - This stack parses the Terraform tfstate file stored in the Config0 resources database and inserts the parsed data as individual entries in the Config0 resources table.
  - For example, if the tfstate file created a VPC and multiple subnets within it, this stack will extract the subnet IDs from the tfstate file and insert them as separate entries in the Config0 resources database.

**Required**

| argument            | description                            | var type | default      |
| ------------------- | -------------------------------------- | -------- | ------------ |
| dst_resource_type   | destination resource type | string | TBD |
| dst_terraform_type  | TBD | string | TBD |
| src_resource_type   | source resource type | string | TBD |


**Optional**

| argument            | description                            | var type |  default      |
| ------------------- | -------------------------------------- | -------- | ------------- |
| add_values          | TBD | TBD | TBD |
| dst_prefix_name     | destination prefix | string | TBD |
| dst_terraform_mode  | TBD | TBD | TBD |
| id                  | TBD | string | TBD |
| labels              | the labels for the terraform cluster | string | TBD |
| mapping             | TBD | TBD | TBD |
| match               | TBD | TBD | TBD |
| must_exists         | requires to be present | bool | true |
| src_labels          | source labels | string | TBD |
| src_provider        | sour provider | string | TBD |
| src_resource_name   | source resource name | string | TBD |
| tags                | the labels for the terraform cluster | string | TBD |

help-add-description-2023 == the run.py does not look like the others. no type and values. i'm not sure what to add so lots of TBD. and i just guessed the others.