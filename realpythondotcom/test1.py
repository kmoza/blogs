import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)
<<<<<<< HEAD

=======
>>>>>>> ff4d6a8af5e07c72def8836e259a0babcbe22c88

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main:before creating thread")
<<<<<<< HEAD
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main:before running thread")
    x.start()
    logging.info("Main:wait for the thread to finish")
    # x.join()
    logging.info("Main:all done")
=======
    x = threading.Thread(target=thread_function,args=(1,))
    logging.info("Main:before running thread")
    x.start()
    logging.info("Main:wait for the thread to finish")
    #x.join()
    logging.info("Main:all done")
>>>>>>> ff4d6a8af5e07c72def8836e259a0babcbe22c88
