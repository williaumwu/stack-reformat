### shorten human description with separate line and new string formating

```
inputargs["human_description"] = f"Parse Terraform for {aws_security_group}"
```
TO:

```
human_description = f"Parse Terraform for {aws_security_group}"

inputargs["human_description"] = human description
```

