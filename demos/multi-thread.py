from threading import Thread, Lock
import time

tLock = Lock()


def timer(name, delay, repeat):
    print "Timer: {0} Started".format(name)
    while repeat > 0:
        time.sleep(delay)
        print name + ": " + str(time.ctime(time.time()))
        repeat -= 1
    print "Time: {0} Completed".format(name)


def timer_with_lock(name, delay, repeat):
    tLock.acquire()
    print "Timer: {0} Started".format(name)
    while repeat > 0:
        time.sleep(delay)
        print name + ": " + str(time.ctime(time.time()))
        repeat -= 1
    print "Time: {0} Completed".format(name)
    tLock.release()


def test_timer():
    t1 = Thread(target=timer, args=("Timer1", 1, 5))
    t2 = Thread(target=timer, args=("Timer2", 2, 5))
    t1.start()
    t2.start()
    print "Main Complete"


def test_timer_with_lock():
    t1 = Thread(target=timer_with_lock, args=("Timer1", 1, 5))
    t2 = Thread(target=timer_with_lock, args=("Timer2", 2, 5))
    t1.start()
    t2.start()
    tLock.acquire()
    print "Main Complete"
    tLock.release()


if __name__ == "__main__":
    test_timer()
    # test_timer_with_lock()
