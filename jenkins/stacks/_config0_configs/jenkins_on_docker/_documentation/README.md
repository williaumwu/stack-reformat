**Description**

  - The stack installs jenkins on docker to the hostname provided

**Infrastructure**

  - The hostname needs to have been created and registered to Config0
  - The ssh_key_name needs to have been already uploaded and registered to Config0

**Required**

| argument      | description                            | var type | default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| hostname   | the hostname to install jenkins       | string   | None         |
| ssh_key_name   | the ssh_key_name to log into jenkins       | string   | None         |

**Optional**

| argument           | description                            | var type |  default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| publish_private_key   | if set true, the private key in base64 hash will show on the Config0 UI      | string   | None         |
