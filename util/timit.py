import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end-start)*1000 )+ " mil seconds")
        return result
    return wrapper

@time_it
def cal_square(numbers):
    result =[]
    for num in numbers:
        result.append(num*num)
    return result
array = range(1,1000)
print(cal_square(array))
