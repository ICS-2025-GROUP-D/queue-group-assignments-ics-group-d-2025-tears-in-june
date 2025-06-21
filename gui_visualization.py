import tkinter as tk
from tkinter import ttk
import time

class CircularPrinterQueue:
    CAPACITY =10

    def __init__(self):
        self.data =[[None,None,None,None] for _ in range(self.CAPACITY)]
        self.front=0
        self.size=0
        self.jobId=0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.CAPACITY

    def enqueue(self,user_id):
        if self.is_full():
            return False

        avail=(self.size+self.front) %self.CAPACITY
        self.jobId +=1
        job_id=self.jobId
        priority =1
        current_time=time.perf_counter_ns()
        self.data[avail]=[user_id,job_id,priority,current_time]
        self.size +=1
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        output =self.data[self.front]
        self.data[self.front]=[None,None,None,None]
        self.front=(self.front+1) % self.CAPACITY
        self.size -=1
        return output

    def get_jobs(self):
        jobs = []
        for i in range(self.CAPACITY):
            job = self.data[i]
            if job[0] is not None:
                waiting_time = (time.perf_counter_ns() - job[3]) // 1_000_000
                jobs.append([job[0], job[1], job[2], waiting_time])
        return jobs
class QueueGUI:
    def __init__(self,root,queue):
        self.queue =queue
        self.root=root
        self.root.title("Print Queue Visualizer")

        self.table=ttk.Treeview(root,columns=("User ID","Job ID","Priority","Waiting Time"), show='headings')
        for col in self.table["columns"]:
            self.table.heading(col,text=col)
            self.table.column(col,width=100)
        self.table.pack(pady =10)

        entry_frame=tk.Frame(root)
        entry_frame.pack()

        tk.Label(entry_frame, text="User ID:").pack(side=tk.LEFT)
        self.user_entry=tk.Entry(entry_frame)
        self.user_entry.pack(side=tk.LEFT)

        tk.Button(root, text="Enqueue", command=self.add_job).pack(pady=5)
        tk.Button(root, text="Dequeue", command=self.remove_job).pack(pady=5)
        tk.Button(root, text="Refresh View", command=self.refresh_table).pack(pady=5)

        self.refresh_table()

    def add_job(self):
        user_id = self.user_entry.get()
        if user_id:
            if not self.queue.enqueue(user_id):
                tk.messagebox.showerror("Queue Full", "The queue is full.")
            self.user_entry.delete(0, tk.END)
            self.refresh_table()

    def remove_job(self):
        self.queue.dequeue()
        self.refresh_table()

    def refresh_table(self):
        for row in self.table.get_children():
            self.table.delete(row)
        for job in self.queue.get_jobs():
            self.table.insert('',tk.END,values=job)

if __name__ == "__main__":
    root = tk.Tk()
    cpq =CircularPrinterQueue()
    app = QueueGUI(root,cpq)
    root.mainloop()









