import threading
import time

class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out


    def run(self):
        with open(self.out, "a") as f:
            description = "This is test result from user_thread_class.py\n\n"
            f.write(description)
            f.write(self.text + '\n')
        time.sleep(3)
        print "Finished Background file write to %s" % (self.out)

def main():
    message = raw_input("Enter a string to store:")
    background = AsyncWrite(message, 'test_output.txt')
    background.start()
    print "The main thread continue to run while it write in another thread"
    print 100 + 200
    
    # wait until the background thread finished
    background.join() 
    
    print "Finished"

if __name__ == "__main__":
    main()
