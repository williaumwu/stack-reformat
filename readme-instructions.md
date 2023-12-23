# General Instructions

- Adding variables in __run.py__ into __README.md

  - required variables will have __add_required__
  - optional variables will have __add_optional

- If you do not know the "description" of the variable
  - put down __"help-add-description-2023"__

- Try to use vscode/pycharm or some editor that will render mark down files in real time

- Push files to designated branch with done and let me know.  Pull request isn't really necessary.

# Example files

## links

- https://github.com/williaumwu/stack-reformat/blob/main/mongodb/stacks/_config0_configs/mongodb_replica_on_ec2/_main/run.py
- https://github.com/williaumwu/stack-reformat/tree/main/mongodb/stacks/_config0_configs/mongodb_replica_on_ec2/_documentation

## path in repository

- ./mongodb/stacks/_config0_configs/mongodb_replica_on_ec2/_documentation/README.md
- ./mongodb/stacks/_config0_configs/mongodb_replica_on_ec2/_main/run.py

## suggestions:

for variables that are already used in the repository, you can do a grep search

for example: 

if you see the variable __aws_default_region__ you can use grep to see if is already in another README file:

```
grep -r aws_default_region -A 2 -B 2
```
