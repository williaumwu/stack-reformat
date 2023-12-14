**Description**

  - This stack wrappers around Ec2 creation of Ubuntu instance
  - Optionally, we can bootstrap the Ubuntu instance to Config0 (Config0)

**Required**

| argument      | description                            | var type | default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| hostname   | hostname of the ec2 server                 | string   | None         |
| ssh_key_name   | ssh_key_name for the ec2 server                 | string   | None         |
| aws_default_region   | default aws region               | string   | us-east-1         |

**Optional**

| argument           | description                            | var type |  default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| config_network   | the configuration network                | choice public/private   | private |
| register_to_db   | register the ec2 instance to Config0               | boolean   | True |
| sg_id   | the single security group id for the ec2 instance               | string   | None |
| security_group_ids   | the security group ids for the ec2 instance               | list   | None |
| security_group   | the security group names for the ec2 instance               | list   | None |
| subnet   | the name of subnet to be used        | string    | None |
| subnet_id   | the subnet_id to be used        | string    | None |
| subnet_ids   | the subnet_ids to select from        | string (csv)    | None |
| image   | the ami image               | string   | None |
| image_filter   | the image filter used for searches      | string       | Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-\*  | 
| image_owner   | the image owner used for searches        | string    | 099720109477 (canonical) |
| size   | the instance size        | string    | t2.micro |
| disksize   | the instance root disk size        | string    | 40 |
| ip_key   | the ip_key from boto used for connection       | public_ip/private_ip    | public_ip |
| vpc_id   | the vpc_id to be used        | string    | None |
| vpc_name   | the name of vpc to be used        | string    | None |
| volume_name   | the name of volume to be attached        | string    | None |
| volume_size   | the size of volume to be created        | string    | None |
| volume_mount   | the mount point of the extra volume        | string    | None |
| volume_fstype   | the fileystem of the extra volume        | string    | None |

**Sample entry:**

```
infrastructure:
   ec2_instance:
       stack_name: config0-hub:::ec2_ubuntu
       arguments:
          hostname: test-instance
          size: t3.micro
          ssh_key_name: mongodb_ssh
          security_groups: web,bastion
          subnet: public
          disksize: 25
          ip_key: public_ip
          volume_size: 100
          volume_mount: /var/lib/mongodb
          volume_fstype: xfs
          mongodb_username: admin123
          mongodb_password: admin123
       credentials:
           - reference: aws_2
             orchestration: true
```
