**Description**
  - This stack sets up Codebuild for CI
  - It mimics the portable and ease of use like a CircleCI or TravisCI, but running in your AWS account.
  - This does not configure a repository, but just the base to add repositories to build on with stack:
    __config0-publish:::add_codebuild_ci__ .

  - This stacks notably using:
    - api gateway
    - s3 storage
    - lambda functions
    - dynamodb for tracking builds and status
    - AWS system parameter store for sensitive information

**Infrastructure**


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

