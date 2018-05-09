```diff
- There exists useless things in this world. This repository is one of them!
```
# KLEE-Symbolic-Execution-Py
Failed attempt at mimicking KLEE in Python

### try.py output

```
a+b-c<b-a+c
a+b-c>a+c-b
a+b-c>b+c-a
a+b-c<a+b+c
a+b-c>c-a-b
a+b-c<c+b+a
```

### try2.py output

```
['a+b-c', '<', 'b-a+c']
['a+b-c', '>', 'a+c-b']
['a+b-c', '>', 'b+c-a']
['a+b-c', '<', 'a+b+c']
['a+b-c', '>', 'c-a-b']
['a+b-c', '<', 'c+b+a']
```

### controlFlow.py && controlFlow_boolHardcoded.py output

```
6
a+b-c>c-a-b
a+b-c<a+b+c
a+b-c<b-a+c
a+b-c<c+b+a
a+b-c>a+c-b
a+b-c>b+c-a

```
