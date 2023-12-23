**Description**

  - This stack establishes CodeBuild for continuous integration (CI).
  - It offers a similar level of portability and user-friendliness as CircleCI or TravisCI, but operates within your AWS account.

This stack utilizes:

  - API Gateway
  - S3 storage
  - Lambda functions
  - DynamoDB for build and status tracking
  - AWS Systems Manager Parameter Store for managing sensitive information.

**Gotchas**

  - This stack focuses on configuring the foundation for CodeBuild and does not set up specific repositories for building. 
  - To add repositories, use the config0-publish:::add_codebuild_ci stack.

**Required**

| argument      | description                            | var type | default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| TBD   | TBD                 | string   | None         |

**Optional**

| argument           | description                            | var type |  default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| TBD   | TBD                 | string   | None         |

**Sample entry**
```
TBD
```

