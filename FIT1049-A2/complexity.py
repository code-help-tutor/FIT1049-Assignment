WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
def local_peak(lst):
    low = 0
    high = len(lst)-1
    while low < high:
        if low == 0 and high == len(lst)-1:
            if lst[low] > lst[low+1]:
                return low
            if lst[high] > lst[high-1]:
                return high
        else:
            if lst[low-1] < lst[low] and lst[low+1] < lst[low]:
                return low
            if lst[high-1] < lst[high] and lst[high+1] < lst[high]:
                return high
        low += 1
        high -= 1


def power(n, p):
    times = 1
    if p == 0:
        outcome = 1
    elif p == 1:
        outcome = n
    else:
        while p != 1:
            shang = p // 2
            yushu = p % 2
            times += shang + yushu
            p = p//2
        outcome = n**times
    return outcome


print(local_peak([0, 2, 4, 6, 5, 2]))
print(local_peak([-7, -6, -2, -10, -5, -11]))
print(local_peak([8.8, 8.6, 8.1, 8.2, 8.1, 8.01]))
print(power(2, 8))
