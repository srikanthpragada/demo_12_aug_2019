from threading import Thread
import threading
import math


class PrimeThread(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        for n in range(2, math.floor(math.sqrt(self.num)) + 1):
            if self.num % n == 0:
                print(f"{self.num} is not a prime number!\n")
                break
        else:
            print(f"{self.num} is a prime number!\n")


# Open file
nums = [393939393, 9, 39393939393939393399117, 12121212121, 29292939327, 38433828283, 62551414124111]
for n in nums:
    t = PrimeThread(n)
    t.start()

# wait for all threads to terminate
ct = threading.current_thread()
for t in threading.enumerate():
    if t != ct:
        t.join()  # wait until thread is terminated

# close file
print("\nNo. of threads : ", threading.active_count())
print("\nThe End\n")
