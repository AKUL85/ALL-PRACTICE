# CPU Scheduling Algorithms

This document explains three fundamental CPU scheduling algorithms used in operating systems to manage process execution.

## Overview

CPU scheduling is the process of deciding which process runs at any given time. It's critical for:
- Maximizing CPU utilization
- Minimizing average waiting time
- Minimizing average turnaround time
- Ensuring fairness among processes

### Key Terms

- **Arrival Time**: When a process enters the ready queue
- **Burst Time**: How long a process needs the CPU
- **Completion Time**: When a process finishes execution
- **Turnaround Time**: Completion Time - Arrival Time (total time from arrival to completion)
- **Waiting Time**: Turnaround Time - Burst Time (time spent waiting in the queue)

---

## 1. FCFS (First Come First Served)

### Description
FCFS is the simplest CPU scheduling algorithm. Processes are executed in the order they arrive, like a queue at a checkout counter.

### Algorithm Logic
1. Sort all processes by their arrival time
2. Execute processes sequentially in order
3. Each process runs to completion before the next process starts
4. Calculate metrics (completion, turnaround, and waiting time)

### Implementation Flow

```
Process 1 arrives → Execute P1 (complete)
Process 2 arrives → Execute P2 (complete)
Process 3 arrives → Execute P3 (complete)
```

### Characteristics

| Aspect | Details |
|--------|---------|
| **Preemption** | Non-preemptive (no interruption) |
| **Average Waiting Time** | May be high |
| **Starvation** | No starvation |
| **Complexity** | Simple to implement |
| **Fairness** | Fair but inefficient |

### Advantages
- ✅ Simple to understand and implement
- ✅ No starvation (every process will eventually run)
- ✅ Minimal overhead

### Disadvantages
- ❌ High average waiting time
- ❌ Poor performance with variable burst times
- ❌ **Convoy Effect**: Short processes wait behind long ones

### Example

```
Processes: P1(Burst=8), P2(Burst=4), P3(Burst=2)

Timeline:
|----P1----|----P2----|--P3--|
0          8          12     14

Results:
P1: Completion=8,  Turnaround=8,  Waiting=0
P2: Completion=12, Turnaround=12, Waiting=8
P3: Completion=14, Turnaround=14, Waiting=12
```

---

## 2. Round Robin (RR)

### Description
Round Robin is a preemptive algorithm that gives each process a fixed time slice (quantum) to execute. If a process doesn't complete within its quantum, it goes to the back of the queue.

### Algorithm Logic
1. Each process gets a **time quantum** (e.g., 4 milliseconds)
2. Process runs for up to the quantum duration
3. If process needs more time, it's moved to the back of the queue
4. If process completes, it exits; next process runs
5. Continue until all processes complete

### Implementation Flow

```
Time Quantum = 4

Process enters queue:
Queue: [P1, P2, P3]
P1 runs for 4 units (remaining burst = 4)
P1 goes to back: [P2, P3, P1]
P2 runs for 4 units (remaining burst = 2)
P2 completes: [P3, P1]
P3 runs for 2 units (completes): [P1]
P1 runs for 4 units (completes): []
```

### Characteristics

| Aspect | Details |
|--------|---------|
| **Preemption** | Preemptive (time quantum interrupts) |
| **Average Waiting Time** | Depends on quantum size |
| **Starvation** | No starvation |
| **Context Switches** | Many (increases overhead) |
| **Fairness** | Fair and balanced |

### Time Quantum Impact
- **Small quantum**: More fairness, but high context switching overhead
- **Large quantum**: Behaves like FCFS
- **Optimal**: Typically 10-100 milliseconds

### Advantages
- ✅ Fair to all processes
- ✅ No starvation
- ✅ Good for time-sharing systems
- ✅ Responsive (each process gets CPU time regularly)

### Disadvantages
- ❌ Increased context switching overhead
- ❌ Average turnaround time can be longer than SJF
- ❌ Performance depends on quantum size selection

### Example

```
Processes: P1(Burst=8), P2(Burst=4), P3(Burst=2)
Time Quantum = 4

Timeline:
|--P1--|--P2--|--P3--|--P1--|--P2--|--P1--|
0  4   8  12  16  18  22  26  30  34

Results:
P1: Completion=34, Turnaround=34, Waiting=26 (runs 3 times)
P2: Completion=30, Turnaround=30, Waiting=26 (runs 2 times)
P3: Completion=18, Turnaround=18, Waiting=16 (runs 1 time)
```

---

## 3. Priority Scheduling

### Description
Priority scheduling assigns a priority level to each process. The CPU always executes the process with the highest priority (lowest priority number). It can be preemptive or non-preemptive.

### Algorithm Logic
1. Assign a priority to each process (lower number = higher priority)
2. Use a priority queue to manage processes
3. Always execute the process with highest priority
4. If a process's priority is high, other processes must wait
5. Calculate metrics after all processes complete

### Priority Rules
- **Priority 0**: Highest priority (runs first)
- **Priority N**: Lower priority (may wait longer)
- **Tie-breaking**: If priorities are equal, use FCFS or arrival time

### Implementation Flow

```
Processes arriving with priorities:
P1(Priority=2), P2(Priority=1), P3(Priority=3)

Execution order:
P2 runs first (priority=1)
P1 runs next (priority=2)
P3 runs last (priority=3)
```

### Characteristics

| Aspect | Details |
|--------|---------|
| **Preemption** | Can be preemptive or non-preemptive |
| **Average Waiting Time** | Depends on priority distribution |
| **Starvation** | Possible (low priority processes may starve) |
| **Fairness** | Unfair to low-priority processes |
| **Real-world Use** | Very common in modern OS |

### Advantages
- ✅ Flexible for different workload types
- ✅ Critical processes run first
- ✅ Good for real-time systems
- ✅ Simple to understand

### Disadvantages
- ❌ **Starvation**: Low-priority processes may never run
- ❌ Unfair to low-priority processes
- ❌ Requires careful priority assignment
- ❌ Can lead to priority inversion

### Starvation Prevention
Techniques to prevent starvation:
- **Aging**: Increase priority of waiting processes over time
- **Priority Boost**: Periodically boost low-priority processes
- **Fair Share**: Guarantee minimum CPU time to all processes

### Example

```
Processes: P1(Burst=8, Pri=2), P2(Burst=4, Pri=1), P3(Burst=2, Pri=3)

Execution order (lower priority number runs first):
P2 (Pri=1) → P1 (Pri=2) → P3 (Pri=3)

Timeline:
|----P2----|----P1----|--P3--|
0          4          12     14

Results:
P2: Completion=4,  Turnaround=4,  Waiting=0
P1: Completion=12, Turnaround=12, Waiting=4
P3: Completion=14, Turnaround=14, Waiting=12
```

---

## Comparison Table

| Property | FCFS | Round Robin | Priority |
|----------|------|-------------|----------|
| **Preemption** | No | Yes | Can vary |
| **Complexity** | Low | Medium | Medium |
| **Average Waiting** | High | Medium | Varies |
| **Starvation** | No | No | Yes |
| **Context Switches** | Low | High | Medium |
| **Fair** | No | Yes | No |
| **Real-time Ready** | No | Moderate | Yes |
| **Best Use Case** | Batch jobs | Time-sharing | Real-time systems |

---

## Performance Metrics

### Average Turnaround Time
Lower is better. Represents how quickly processes complete.

$$\text{Avg Turnaround} = \frac{\sum \text{Turnaround Time}}{n}$$

### Average Waiting Time
Lower is better. Represents how long processes wait in queue.

$$\text{Avg Waiting} = \frac{\sum \text{Waiting Time}}{n}$$

---

## When to Use Each Algorithm

### FCFS
- Simple batch processing systems
- When processes have similar burst times
- When fairness in arrival order is important
- Legacy systems with minimal overhead requirements

### Round Robin
- Time-sharing multi-user systems
- General-purpose operating systems
- When fairness and responsiveness are priorities
- Modern desktop and server OS

### Priority Scheduling
- Real-time operating systems
- Critical process management
- Systems with varied process importance
- I/O heavy systems (different priorities for I/O and CPU tasks)

---

## Key Takeaways

1. **FCFS** is simple but inefficient for mixed workloads
2. **Round Robin** provides fairness at the cost of overhead
3. **Priority Scheduling** is powerful but requires careful management
4. No single algorithm is optimal for all scenarios
5. Modern OS often use hybrid approaches combining multiple algorithms
6. The choice depends on system requirements and workload characteristics

---

## Code Implementation Notes

All three algorithms are implemented in Java with:
- User input for process details
- Calculation of all timing metrics
- Formatted output tables
- Average waiting and turnaround time computation

Files:
- `FCFS.java` - First Come First Served
- `RoundRobin.java` - Round Robin with configurable quantum
- `Priority.java` - Priority-based scheduling (non-preemptive)
