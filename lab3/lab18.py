
def read_hour():
    hour = int(input("Enter hour: "))
    return hour
def read_minute():
    minute = int(input("Enter minute: "))
    return minute
def read_second():
    second = int(input("Enter second: "))
    return second

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)


def to_seconds(hour, minute, second):
    return hour*3600 + minute*60 + second


def time_elapsed(start_time, finish_time):
    elapsed_seconds = finish_time - start_time
    
    hours = elapsed_seconds // 3600
    elapsed_seconds %= 3600
    minutes = elapsed_seconds // 60
    seconds = elapsed_seconds % 60
    return f"{hours} hours {minutes} minutes {seconds} seconds."
    
print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))