# tick simulator

import time

class TickSimulator:
    def __init__(self, queue, aging_interval=3, expiry_time=14, max_priority=10):
        # Reference to the main queue object (CircularPrinterQueue)
        self.queue = queue

        # Aging: how many ticks before a job's priority increases
        self.aging_interval = aging_interval

        # Expiry: how many ticks a job can wait before it is removed
        self.expiry_time = expiry_time

        # Maximum allowed priority for any job
        self.max_priority = max_priority

        # Keeps track of how many ticks have passed
        self.time_tick = 0

    def tick(self):
        # Simulate onr unit of time passing in the system
        print(f"\n[Tick {self.time_tick + 1} Simulating time passing...\n")
        self.time_tick += 1

        for job in self.queue.data:
            if job[0] is not None:# if the job slot is not empty

                # 1. Increase the job's waiting time by 1 tick
                job[3] +=1

                # 2. Check if this job should age
                if job[3] % self.aging_interval == 0 and job[2] < self.max_priority:
                    job[2] += 1 # Increase priority
                    print(f" - Job {job[1]}(User {[0]}) aged -> New Priority: {job[2]}")

                # 3. Remove the job if it has waited too long
                if job[3] > self.expiry_time:
                    print(f" - Job {job[1]}(User {[0]}) expired after {job[3]} ticks.")
                    job[:] = [None, None, None, None] #Clear the job slot
                    self.queue.size -= 1

        # Resort the queue by priority and waiting time
        self._sort_queue()

        # Show updated queue state in the terminal
        self.queue.show_status()

    def _sort_queue(self):
        # Geet only non-empty job entries
        jobs = [job for job in self.queue.data if job[0] is not None]

        # Sort them by priority (high to low), then waiting time (high to low)
        jobs.sort(key=lambda j: (-j[2], -j[3]))

        # Fill remaining slots with empty placeholders
        empty_slots = [[None, None, None] for i in range(self.queue.CAPACITY - len(jobs))]

        # Overwrite the queue's data with sorted jobs + empty slots
        self.queue.data = jobs + empty_slots

