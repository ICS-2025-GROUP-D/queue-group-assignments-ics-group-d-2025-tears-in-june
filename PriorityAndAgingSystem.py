# Priority and Aging System for Print Queue Management
class PrintQueueManager:
    def __init__(self, max_priority=10, aging_interval=3):
        """
            Initialize the print queue manager.
            max_priority: The highest possible priority a job can reach.
            aging_interval: Number of ticks after which a job's priority is increased.
            
        """
        self.queue = []  # List of job dicts
        self.max_priority = max_priority
        self.aging_interval = aging_interval

    def enqueue_job(self, user_id, job_id, priority):
        """
        Add a new job to the queue.
        :param user_id: ID of the user submitting the job.
        :param job_id: Unique job identifier.
        :param priority: Initial priority of the job.
        """
        job = {
            'user_id': user_id,
            'job_id': job_id,
            'priority': priority,
            'waiting_time': 0,
            'last_aged': 0
        }
        self.queue.append(job)
        self._sort_queue()

    def _sort_queue(self):
        """
        Sort queue by priority (desc), then waiting_time (desc).
        """
        self.queue.sort(key=lambda job: (-job['priority'], -job['waiting_time']))

    def apply_priority_aging(self):
        """
        Increase priority of jobs that have waited at least aging_interval since last aging.
        """
        for job in self.queue:
            if job['waiting_time'] - job['last_aged'] >= self.aging_interval:
                if job['priority'] < self.max_priority:
                    job['priority'] += 1
                job['last_aged'] = job['waiting_time']
        self._sort_queue()

    def tick(self):
        """
        Simulate time passing: increment waiting_time, apply aging.
        """
        for job in self.queue:
            job['waiting_time'] += 1
        self.apply_priority_aging()

    def print_job(self):
        """
        Remove and return the highest priority job from the queue.
        """
        if self.queue:
            job = self.queue.pop(0)
            print(f"Printing job: User {job['user_id']}, Job {job['job_id']}, Priority {job['priority']}, Waited {job['waiting_time']} ticks")
            return job
        else:
            print("No jobs to print.")
            return None

    def show_status(self):
        """
        Print the current queue state.
        """
        print("Current Queue:")
        for job in self.queue:
            print(f"User: {job['user_id']}, Job: {job['job_id']}, Priority: {job['priority']}, Waiting: {job['waiting_time']}")

if __name__ == "__main__":
    pq = PrintQueueManager(max_priority=5, aging_interval=2)

    # Enqueue some jobs
    pq.enqueue_job("alice", "job1", 2)
    pq.enqueue_job("bob", "job2", 1)
    pq.enqueue_job("carol", "job3", 3)
    pq.show_status()

    # Simulate time passing
    print("\n--- Tick 1 ---")
    pq.tick()
    pq.show_status()

    print("\n--- Tick 2 ---")
    pq.tick()
    pq.show_status()

    print("\n--- Tick 3 ---")
    pq.tick()
    pq.show_status()

    # Print a job
    print("\n--- Printing a job ---")
    pq.print_job()
    pq.show_status()

