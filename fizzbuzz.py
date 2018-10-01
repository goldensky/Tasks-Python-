import time
import functools


def count_time(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        t = time.time()
        result = func(*args, **kwargs)
        print(time.time() - t)
        return result
    return inner


class Solution:
    @count_time
    def FizzBuzz(self, n):
        FB = {3:'Fizz', 5: 'Buzz'}
        for i in range(n+1):
            if i % 3 == 0 and i % 5 == 0:
                print(i, f'{FB[3]}{FB[5]}')
            elif i % 3 == 0:
                print(i, f'{FB[3]}')
            elif i % 5 ==0:
                print(i, f'{FB[5]}')
            else:
                print(i)


@count_time
def fizzbuzz():
    FB = {3:'Fizz', 5: 'Buzz'}
    while True:
        if i % 3 == 0 and i % 5 == 0:
            yield (i, f'{FB[3]}{FB[5]}')
        elif i % 3 == 0:
            yield(i, f'{FB[3]}')
        elif i % 5 ==0:
            yield(i, f'{FB[5]}')
        else:
            yield(i, )


if __name__ == '__main__':
    c = Solution()
    c.FizzBuzz(100)
    print()
    
    c = fizzbuzz()
    for i in range(100):
        print(next(c))
    
    














    
