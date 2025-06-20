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
        self.max_priority = 10
        self.aging_interval = 3
        self.expiry_time = 14
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
        waiting_time = 0
        self.data[avail]= [user_id,job_id,priority,waiting_time]
        self.size+=1

    def dequeue(self):
        if self.is_empty():
            print("The queue is empty, can't print anything")
            return None
        output = self.data[self.front]
        self.data[self.front]= [None,None,None,None]
        self.front = (self.front + 1)% self.CAPACITY
        self.size-=1
        print(f"Printing job: User {output[0]}, Job {output[1]}, Priority {output[2]}, Waited {output[3]} ticks")
        return

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
            print("There are no jobs in the queue")
            return
        else:
            print(f"There are {count} job(s) in the queue")
            return

    def _sort_queue(self):
        """
        Sort queue by priority (desc), then waiting_time (desc).
        """
        jobs_only = [job for job in self.data if job[0] is not None]
        jobs_only.sort(key=lambda job: (-job[2], -job[3]))
        self.data = jobs_only + [[None,None,None,None] for _ in range(self.CAPACITY - len(jobs_only))]

    def apply_priority_aging(self):
        """
        Increase priority of jobs that have waited at least aging_interval since last aging.
        """
        if self.is_empty() is not True:
            for job in self.data:
                if job[3] is not None and job[2] is not None:
                    if job[3] % self.aging_interval == 0:
                        if job[2] < self.max_priority:
                            job[2] += 1
            self._sort_queue()

    def tick(self):
        """
        Simulate time passing: increment waiting_time, apply aging.
        """
        for job in self.data:
            if job[0] is not None:
                job[3] += 1
        self.apply_priority_aging()
        cpq.remove_expired_jobs()

    def remove_expired_jobs(self): # self refers to the instance of the class, so this
        #function can access things like self.queue and self.expiry_time

        expired_jobs = [] # temporary list where all jobs that need to be removed will be stored

        i:int = 0
        for i in range(len(self.data)):
            job = self.data[i]
            if job[0] is not None:
                if job[3] > self.expiry_time:
                    expired_jobs.append(job)
                    self.data[i] = [None,None,None,None]
                    self.size-=1
                    print(f"The job ID {job[1]} from user ID {job[0]} expired and was removed from the queue.")


if __name__=="__main__":
    cpq = CircularPrinterQueue()
    cpq.show_status()
    cpq.enqueue("Ivan")
    cpq.show_status()
    cpq.enqueue("Mayabi",6)
    cpq.show_status()
    cpq.enqueue("Albert")
    cpq.enqueue("Muigai")
    cpq.show_status()
    cpq.handle_simultaneous_submissions(["Ivan", "Mayabi", "Albert", "Muigai"])
    cpq.tick()
    cpq.tick()
    cpq.tick()
    cpq.tick()
    cpq.tick()
    cpq.tick()
    cpq.tick()
    cpq.tick()
    cpq.tick()
    cpq.show_status()
    (cpq.dequeue())
    (cpq.dequeue())
    cpq.tick()
    (cpq.dequeue())
    (cpq.dequeue())
    (cpq.dequeue())
    (cpq.dequeue())