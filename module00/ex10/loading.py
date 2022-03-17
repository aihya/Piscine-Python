import time

def ft_progress(it):
    start = time.time()
    t1 = 0.0
    t2 = 0.0
    for c in it:
        eta = (t2 - t1) * (it[-1] - c)
        per = ((c * 100) // it[-1])
        prg = "{}>".format('=' * ((int(per) // 5) - 1))
        div = "{}/{}".format(c+1, it[-1]+1)
        et = time.time() - start

        print("ETA: {:.2f}s [{:3.0f}%] [{:20}] {} | elapsed time {:.2f}s".format(eta, per, prg, div, et))

        t1 = time.time()
        yield c
        t2 = time.time()

if __name__ == "__main__":
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        time.sleep(0.005)
    print()
    print(ret)

