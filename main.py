import math
import matplotlib.pyplot as plt

res = 0
n_res = 0
res_arr = []
n_arr = []

for n in range(1000):
    if n != 0:
        t = (n + 1) / 2
        h = 0
        for n_temp in range(n + 1):
            if n_temp != 0:
                h += ((1 / n) * math.log2(1 / n)) * (-1)
        res_temp = h / t
        if res_temp > res:
            res = res_temp
            n_res = n
        res_arr.append(res_temp)
        n_arr.append(n)

plt.plot(n_arr, res_arr)
plt.show()

print(res)
print(n_res)
