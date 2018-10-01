
class Solution:
    def reverse(self, x):
        num = str(x)
        #print(f'input number: {num}')
        if x < 0:
            rez = -int(num[1:][::-1])
        else:
            rez = int(num[::-1])
        if (-2**31) < rez < (2**31) - 1:
            return rez
        else:
            return 0

if __name__ == '__main__':
    integers = [123, 3456, -132455, 1534236469]
    r = Solution()
    for i in integers:
        print(i, '-->', r.reverse(i))  
