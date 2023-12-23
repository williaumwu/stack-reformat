**Description**

  - This stack sets up Jenkins with Docker on the specified hostname.

**Infrastructure**

To proceed with the setup, please ensure that 
  - the hostname has been created and registered with Config0. 
  - the SSH key name has been uploaded and registered in Config0 beforehand.

**Required**

| argument      | description                           | var type | default      |
| ------------- |---------------------------------------| -------- | ------------ |
| hostname   | the hostname to install jenkins       | string   | None         |
| ssh_key_name   | the ssh_key_name to log into hostname | string   | None         |

**Optional**

| argument           | description                                                                       | var type | default |
| ------------- |-----------------------------------------------------------------------------------| -------- |---------|
| publish_private_key   | if set true, the private key in base64 hash will show on the Config0 UI           | string   | None    |
| ansible_docker_exec_env   | overide the default the docker runtime to execute ansible used to install jenkins | string   | elasticdev/ansible-run-env        |
