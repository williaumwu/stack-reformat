**Description**

The process of bootstrapping a server to the Config0 platform involves setting up the server to execute commands sent to it. This capability becomes particularly useful when utilizing a Bastion host to execute SSH commands on other servers within a private network.

By bootstrapping a server to the Config0 platform, you establish the necessary configuration and environment for it to receive and execute commands. This server acts as a gateway or intermediary, allowing you to securely access and control other servers within a private network.

The bootstrapped server, often referred to as a Bastion host, serves as an entry point through which SSH commands can be directed to other servers in the private network. This setup offers enhanced security by limiting direct external access to the private servers while enabling remote administration and execution of commands.

In summary, bootstrapping a server to the Config0 platform facilitates the establishment of a Bastion host, which acts as a secure intermediary for executing SSH commands on servers within a private network.

  - Example
      - Bastion server executes ssh commands on other servers in a private network
      - Bastion server executes ansible playbooks on other servers in a private network

**Required**

| argument | description                             | var type | default |
|----------|-----------------------------------------|----------|---------|
| hostname | the hostname of the server to bootstrap | string   | None    |

**Optional**

| argument     | description                                                                                      | var type | default   |
|--------------|--------------------------------------------------------------------------------------------------|----------|-----------|
| ssh_key_name | the ssh key name use to authenticate to server                                                   | string   | None      |
| ip_key       | the ip_key refers to private or public networks (public_ip/private_ip)                           | string   | public_ip |
| user         | the user to log into the server with | string   | ubuntu    |
