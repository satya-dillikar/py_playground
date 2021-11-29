__author__ = 'bchan'


from queue import Queue
import concurrent.futures
import random
import time
import logging

logging.basicConfig(level=logging.INFO,format='(%(threadName)-10s) %(message)s',)

q = Queue()
fred = [1,2,3,4,5,6,7,8,9,10]

def f(x):
    logging.info("Process Started - input:%d" % x)
    pause = random.randint(5,10)
    time.sleep(pause)
    res = x * x
    data = {}
    data["input"] = x
    data["output"] = res
    logging.info("Process Completed - input:%d, output:%d" % (x, res))
    q.put(data)

def main():
    # “with” statement guarantees that the execution is waiting until all worker threads finish
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for num in fred:
            executor.submit(f, num)
    # all jobs are processed and all the worker threads finished.
    logging.info("All jobs completed!!!")
    while not q.empty():
        print (q.get())

if __name__ == "__main__":
    main()