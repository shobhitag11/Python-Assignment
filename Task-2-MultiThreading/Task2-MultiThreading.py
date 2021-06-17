# Import required packages
import time
import threading

def task(thread_no, timer):
    '''Function to check and print which thread is running at every 5 second'''
    if timer % 5 == 0:
        print(f"Thread {thread_no} is running at {timer}")

def main():
    '''this is the main function to run the threads as per the requirement.
    It should be able to launch 3 different thread
    ○ Each thread should print this every 5 second:
        ■ Thread <thread number> is running at <time elapsed>
    ○ Initially start thread 1 and 3
    ○ After 20 second stop thread 1 start thread 2
    ○ Again after 18 second stop thread 3 and start thread 1
    '''
    timer = 0
    while True:
        # Creating 3 threads using for loop and storing in a list.
        threads = []
        for i in range(1, 4):
            t = threading.Thread(target=task, args=(i, timer))
            threads.append(t)

        # Thread1 = threads[0]
        # Thread2 = threads[1]
        # Thread3 = threads[2]

        # For first 20 seconds: Starting Thread1 and Thread3.
        if timer < 20:
            threads[0].start()
            threads[2].start()
            threads[0].join()
            threads[2].join()
        # for next 18 seconds:
        # Stop Thread1 and Start Thread2
        elif 20 <= timer < 38:
            threads[1].start()#Second thread
            threads[2].start()#Third thread
            threads[1].join()
            threads[2].join()
        # again after 18 seconds i.e. after first 38 seconds
        # Stop Thread3 and start Thread1
        elif timer >= 38:
            threads[0].start()
            threads[1].start()
            threads[0].join()
            threads[1].join()

        time.sleep(1)
        timer += 1

# Running the code directly
if __name__ == "__main__":
    main()