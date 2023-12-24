**Description**

  - Creates python lambda function to AWS.
  - This stack expects as an input the python lambda files as an execution group

  # TODO - cloning lambda files from github

**Required**

| argument      | description                            | var type | default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| config0_lambda_execgroup_name   | name of lambda of exec group  | string   | None         |
| lambda_name                     | name lambda function          | string   | None         |
| s3_bucket                       | s3_bucket                     | string   | None         |

**Optional**

| *argument*           | *description*                            | *var type* |  *default*      |
| -------------------- | ---------------------------------------- | ---------- | --------------- |
| aws_default_region     | default aws region                     | string     | us-east-1       |
| cloud_tags_hash        | tags for the resources in the cloud as base64 | string  | None         |
| debug                  | help-add-description-2023 | TBD| TBD |
| handler                | lambda function handler | string | app.handler |
| lambda_env_vars_hash   | lambda function environment variables as base64 | string | None |
| lambda_layers          | help-add-description-2023 i think the previous lambda_layers has wrong description | TBD | TBD |
| lambda_timeout         | total time allocated to wait before the function times out | int | 900 |
| memory_size            | lambda function allocated memory size | int | 256 |
| policy_template_hash   | lambda function policy template as base64 | string | None |
| runtime                | lambda function runtime language | string | python3.9 |
| s3_key                 | s3 bucket key | string | None |
| stateful_id            | help-add-description-2023 | string | _random |

**Sample entry:**

```
```
