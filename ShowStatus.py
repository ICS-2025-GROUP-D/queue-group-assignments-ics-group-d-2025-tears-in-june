import time as time

class CircularPrinterQueue:
    CAPACITY:int = 10

    def __init__(self):
        self.data = [[None,None,None,None] for _ in range(self.CAPACITY)]
        self.front = 0
        self.size = 0
        self.jobId= 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.CAPACITY

    def enqueue(self, user_id):
        if self.is_full():
            print("The queue is full, wait a short while")
            return
        avail = (self.size + self.front) % self.CAPACITY
        self.jobId += 1
        job_id = self.jobId
        priority = 1
        current_time = time.perf_counter_ns()
        self.data[avail]= [user_id, job_id, priority, current_time]
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("The queue is empty, can't print anything")
            return None
        output = self.data[self.front]
        self.data[self.front] = [None,None,None,None]
        self.front = (self.front + 1) % self.CAPACITY
        self.size -= 1
        return output

    #Module 6:VISUALIZATION
    def show_status(self):
        print("\n Current Queue Status")
        print("=" * 70)
        print(f"{'Pos':<5}{'User ID':<10}{'Job ID':<10}{'Priority':<10}{'Waiting Time (ms)':<20}")
        print("-" * 70)

        count = 0
        for i in range(self.CAPACITY):
            job = self.data[i]
            if job[0] is not None:
                waiting_time_ns = time.perf_counter_ns() - job[3]
                waiting_time_ms = waiting_time_ns // 1_000_000
                print(f"{i+1:<5}{job[0]:<10}{job[1]:<10}{job[2]:<10}{waiting_time_ms:<20}")
                count += 1

        print("=" * 70)
        if count == 0:
            print(" The queue is currently empty.\n")
        else:
            print(f" {count} job(s) currently in the queue.\n")


if __name__ == "__main__":
    cpq = CircularPrinterQueue()
    cpq.enqueue("Ivan")
    cpq.enqueue("Mayabi")
    cpq.enqueue("Albert")
    cpq.enqueue("Muigai")
    cpq.enqueue("Kristie")

    cpq.show_status()

    time.sleep(1.5)  # simulate time passing
    cpq.dequeue()
    cpq.show_status()
    print(cpq.dequeue())
    print(cpq.dequeue())
    print(cpq.dequeue())
    print(cpq.dequeue())
    print(cpq.dequeue())
