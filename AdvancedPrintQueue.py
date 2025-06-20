#Import the time class to allow timers
import time as time

#Import threading
import threading

#Specify the class
class CircularPrinterQueue:
    #Constant
    CAPACITY:int = 10

    #Constructor
    def __init__(self):
        self.data = [[None,None,None,None] for _ in range(self.CAPACITY)]
        self.front = 0
        self.size = 0
        self.jobId= 0
        self.lock = threading.Lock()#New module 4 code

    #Method for empty check
    def is_empty(self):
        if self.size==0:
            return True
        else:
            return False

    #Method to check what is on top
    def top(self):
        return self.data[self.front]

    #Method to check if full
    def is_full(self):
        if self.size == self.CAPACITY:
            return True
        else:
            return False

    #Method to add to queue
    """"When taking data in, insert a list of[user_id,job_id,priority,waiting_time]:
                -  Only User_Id needed
                -  Job_Id will be dynamic 
                -  Priority will be default 1
                -  Waiting time will be obtained from the value on time.perf_counter()
                        * time.perf_counter()[Python] is similar to System.nanoTime[Java]"""
    def enqueue(self,user_id,priority = 1):
        if self.is_full():
            print("The queue is full, wait a short while")
            return
        avail = (self.size + self.front) % self.CAPACITY
        self.jobId +=1
        job_id = self.jobId
        current_time = time.perf_counter_ns()
        self.data[avail]= [user_id,job_id,priority,current_time]
        self.size+=1

    def dequeue(self):
        if self.is_empty():
            print("The queue is empty, can't print anything")
            return None
        output = self.data[self.front]
        self.data[self.front]= [None,None,None,None]
        self.front = (self.front + 1)% self.CAPACITY
        self.size-=1
        return output

        # New module 4 method= handle_simultaneous_submissions
    def handle_simultaneous_submissions(self, user_ids):
        threads = []

        def submit_job(user_id):
            with self.lock:  # Ensure only one thread enqueues at a time
                self.enqueue(user_id)

        for user_id in user_ids:
            t = threading.Thread(target=submit_job, args=(user_id,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()  # Wait for all threads to finish before continuing

    def show_status(self):
        count:int = 0
        i:int = 0
        while i <= self.CAPACITY-1:
            if self.data[i][2] is not None:
                count+=1
            i+=1
        if count==0:
            return "There are no jobs in the queue"
        else:
            return f"There are {count} job(s) in the queue"

if __name__=="__main__":
    cpq = CircularPrinterQueue()
    cpq.show_status()
    cpq.enqueue("Ivan")
    cpq.show_status()
    cpq.enqueue("Mayabi")
    cpq.show_status()
    cpq.enqueue("Albert")
    cpq.enqueue("Muigai")
    cpq.show_status()
    cpq.handle_simultaneous_submissions(["Ivan", "Mayabi", "Albert", "Muigai"])
    print(cpq.show_status())
    print(cpq.dequeue())
    print(cpq.dequeue())
    print(cpq.dequeue())
    print(cpq.dequeue())
    print(cpq.dequeue())
    print(cpq.dequeue())