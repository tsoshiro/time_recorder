# time_recorder
## Description
A simple decorator to measure how long it takes to process a method.

## How to use
```
import time_recorder

@time_recorder.time_recorder
def some_method():
	...
```

### Print looks like:
```
$ python sample.py
Started func: multiple_after_time [2020-05-24 18:06:09]
Finished func: multiple_after_time took 2.005 sec[2020-05-24 18:06:11]
Started func: print_multiple_resule_after_time [2020-05-24 18:06:11]
6
Finished func: print_multiple_resule_after_time took 3.005 sec[2020-05-24 18:06:14]
```
