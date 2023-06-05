from joblib import Parallel, delayed
import time, math


def my_fun(i):
    time.sleep(1)
    t = math.sqrt(i ** 2)
    print(t)
    return t


num = 4
start = time.time()

Parallel(n_jobs=4)(delayed(my_fun)(i) for i in range(num))

end = time.time()

print('{:.4f} s'.format(end - start))