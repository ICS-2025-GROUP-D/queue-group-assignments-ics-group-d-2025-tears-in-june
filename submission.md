# Group Submission - Print Queue Simulator

## Group Name
ICS 2D, Group Tears in June

## Members & Modules

| Name    | Reg. No. | Module                              | Description |
|---------|----------|-------------------------------------|-------------|
| Ivan    | 180954   | Core Queue Management               | Implemented a circular queue with enqueue/dequeue logic and job metadata tracking. |
| Kevin   | 122787   | Priority & Aging                    | Implemented job priority rules and aging mechanism for long-waiting jobs. |
| Manvin  | 189925   | Job Expiry                          | Developed expiry cleanup system to auto-remove stale jobs. |
| Albert  | 189990   | Concurrent Submission               | Implemented handle_simultaneous_submissions using threads and locks. |
| Aisha   | 190497   | Event simulation &  Time Management | Wrote the tick system to simulate time, update priorities, and check expiry. |
| Kristie | 192565   | Visualization                       | Displayed job snapshots clearly after every event in the queue. |


---

## How to Run the Program

1. Make sure you have *Python 3.9+* installed
2. Open a terminal in the project root directory
3. Run the main file named final.py:

```bash
python final.py