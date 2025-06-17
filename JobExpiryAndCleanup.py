class CircularPrinterQueue:

    def __init__(self, expiry_time=5):
        self.queue = []
        self.expiry_time = expiry_time

    def remove_expired_jobs(self): # self refers to the instance of the class, so this
        #function can access things like self.queue and self.expiry_time

        expired_jobs = [] # temporary list where all jobs that need to be removed will be stored

        for job in self.queue:
            if job["waiting_time"] > self.expiry_time:
                expired_jobs.append(job)

        for job in expired_jobs:
            self.queue.remove(job)
            print(f"The job ID {job['job_id']} from user ID {job['user_id']} expired and was removed from the queue.")


pq_manager = CircularPrinterQueue(expiry_time=5)

# Simulate some jobs
pq_manager.queue = [
    {"job_id": "111111", "user_id": "123456", "priority": 1, "waiting_time": 6},  # should expire
]

# Call your module function
pq_manager.remove_expired_jobs()
