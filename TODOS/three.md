### parser formating

```
stack.parse.add_required(key="ttl", default="7200", choices=["3600", "7200"])
```

TO

```
stack.parse.add_required(key="ttl", 
                         default="7200", 
                         choices=["3600", "7200"])
```
