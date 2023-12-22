**Description**
  - The Codebuild CI is expected to be built with stack: 
     - __config0-publish:::setup_codebuild_ci__
    
  - This stack connects a repository for Codebuild CI to be triggered to build on

**Required**

| argument       | description                                                                  | var type | default      |
|----------------|------------------------------------------------------------------------------| -------- | ------------ |
| codebuild_name | the name of the codebuild project                                            | string   | None         |
| git_repo       | the git repository that you want run codebuild ci on | string   | None         |

**Optional**

| argument           | description                            | var type |  default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| TBD   | TBD                 | string   | None         |
