import time_recorder
import time

@time_recorder.time_recorder
def multiple_after_time(a, b, sec):
    time.sleep(sec)
    return a * b

@time_recorder.time_recorder
def print_multiple_resule_after_time(a, b, sec):
    time.sleep(sec)
    print(a * b)

if __name__ == '__main__':
    multiple_after_time(2, 3, 2)
    print_multiple_resule_after_time(2, 3, 3)