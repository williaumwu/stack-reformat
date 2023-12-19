### find code where a bunch of comments are found and has debug symbols and put # fixfix777 on top of it

```
# this is left over code
# a = { "b":"c"}
```

```
# fixfix777
# this is left over code
# a = { "b":"c"}
```

```
self.logger.debug("a"*32)
self.logger.debug("this is left over code")
self.logger.debug("a"*32)
```

```
# fixfix777
self.logger.debug("a"*32)
self.logger.debug("this is left over code")
self.logger.debug("a"*32)
```
