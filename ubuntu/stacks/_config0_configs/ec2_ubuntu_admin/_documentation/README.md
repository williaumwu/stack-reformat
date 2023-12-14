**Description**

  - Creates an ec2 VM for managing AWS with Ubuntu

**Infrastructure**

  - expects ssh_key_name to be uploaded to Ec2

**Required**

| argument      | description                            | var type | default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| hostname   | the hostname       | string   | None         |
| ssh_key_name   | the ssh key name for the VMs       | string   | None         |
| vpc_id | the vpc id | string   | None       |
| subnet_ids   | a subnet for the VMs is selected from a list of the provided subnet_ids  | string in csv   | None         |
| sg_id   | the security group id for the VMs       | string   | None         |

**Optional**

| argument           | description                            | var type |  default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| spot   | the option to use spot VM. (buyer be aware)    | boolean   | None        |
| ami   | the ami image used for VM      | string   | None        |
| ami_filter   | the ami filter used to search for an image as a base for VM      | string   | None        |
| ami_owner   | the ami owner used to search for an image as a base for VM      | string   | None        |
| aws_default_region   | the aws region                | string   | us-east-1         |
| instance_type | the instance_type for the VMs | string   | t3.micro       |
| disksize | the disksize for the VM | string   | None       |
| tags | the tags for the VM | string   | None       |
| labels | the labels for the VM | string   | None       |
| publish_to_saas | publish or print vm info to saas ui | boolean   | None       |

**Sample in substack:**

```

class Main(newSchedStack):

    def __init__(self,stackargs):

        newSchedStack.__init__(self,stackargs)

        self.stack.parse.add_required(key="hostname")
        self.stack.parse.add_required(key="ssh_key_name")
        self.stack.parse.add_required(key="iam_instance_profile")
        self.stack.parse.add_required(key="vpc_name")
        self.stack.parse.add_required(key="vpc_id")
        self.stack.parse.add_required(key="subnet_ids")
        self.stack.parse.add_required(key="instance_type")
        self.stack.parse.add_required(key="disksize")
        self.stack.parse.add_required(key="aws_default_region")
        self.stack.parse.add_required(key="sg_id")

        ....

    ....

    def run_vm_admin(self):

        self.stack.init_variables()

        user_data_hash = 'echo "machine name is "{}"'.format(self.stack.hostname)

        arguments = { "hostname":self.stack.hostname,
                      "spot": True,
                      "ip_key": "public_ip",
                      "user_data_hash": user_data_hash,
                      "ssh_key_name": self.stack.ssh_key_name,
                      "iam_instance_profile":self.stack.iam_instance_profile,
                      "publish_to_saas":True,
                      "vpc_name":self.stack.vpc_name,
                      "vpc_id":self.stack.vpc_id,
                      "subnet_ids":self.stack.subnet_ids,
                      "instance_type": self.stack.admin_instance_type,
                      "disksize": self.stack.disksize,
                      "aws_default_region":self.stack.aws_default_region,
                      "sg_id":self.stack.bastion_sg_id,
                      }

        kwargs = {arguments":arguments}
        kwargs["automation_phase"] = "infrastructure"
        kwargs["human_description"] = 'Create EC2 admin {}'.format(self.stack.hostname)

        return self.stack.ec2_ubuntu_admin.insert(display=True,**kwargs)

```
