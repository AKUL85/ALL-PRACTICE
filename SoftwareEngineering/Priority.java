import java.util.*;

public class Priority {
    static class Process implements Comparable<Process> {
        int id;
        int arrivalTime;
        int burstTime;
        int priority;
        int completionTime;
        int turnaroundTime;
        int waitingTime;

        Process(int id, int arrivalTime, int burstTime, int priority) {
            this.id = id;
            this.arrivalTime = arrivalTime;
            this.burstTime = burstTime;
            this.priority = priority;
        }

        @Override
        public int compareTo(Process other) {
            
            if (this.priority != other.priority) {
                return this.priority - other.priority;
            }
            return this.arrivalTime - other.arrivalTime;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("=== Priority Scheduling ===");
        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();
        
        List<Process> processes = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            System.out.println("\nProcess " + (i + 1) + ":");
            System.out.print("Arrival Time: ");
            int arrival = sc.nextInt();
            System.out.print("Burst Time: ");
            int burst = sc.nextInt();
            System.out.print("Priority (lower number = higher priority): ");
            int priority = sc.nextInt();
            processes.add(new Process(i + 1, arrival, burst, priority));
        }
        
        // Sort by arrival time initially
        processes.sort((p1, p2) -> p1.arrivalTime - p2.arrivalTime);
        
        PriorityQueue<Process> pq = new PriorityQueue<>();
        int currentTime = 0;
        int completed = 0;
        boolean[] processed = new boolean[n];
        
        while (completed < n) {
            
            for (int i = 0; i < n; i++) {
                if (!processed[i] && processes.get(i).arrivalTime <= currentTime) {
                    pq.add(processes.get(i));
                    processed[i] = true;
                }
            }
            
            if (pq.isEmpty()) {
                if (completed < n) {
                    
                    int nextArrival = Integer.MAX_VALUE;
                    for (Process p : processes) {
                        if (p.completionTime == 0) {
                            nextArrival = Math.min(nextArrival, p.arrivalTime);
                        }
                    }
                    currentTime = nextArrival;
                }
                continue;
            }
            
            Process p = pq.poll();
            currentTime += p.burstTime;
            p.completionTime = currentTime;
            p.turnaroundTime = p.completionTime - p.arrivalTime;
            p.waitingTime = p.turnaroundTime - p.burstTime;
            completed++;
        }
        
        
        System.out.println("\n=== Results ===");
        System.out.printf("%-5s %-12s %-12s %-10s %-15s %-15s %-12s\n", 
                         "ID", "Arrival", "Burst", "Priority", "Completion", "Turnaround", "Waiting");
        System.out.println("--".repeat(50));
        
        double avgTurnaround = 0, avgWaiting = 0;
        for (Process p : processes) {
            System.out.printf("%-5d %-12d %-12d %-10d %-15d %-15d %-12d\n",
                            p.id, p.arrivalTime, p.burstTime, p.priority,
                            p.completionTime, p.turnaroundTime, p.waitingTime);
            avgTurnaround += p.turnaroundTime;
            avgWaiting += p.waitingTime;
        }
        
        avgTurnaround /= n;
        avgWaiting /= n;
        
        System.out.println("\nAverage Turnaround Time: " + avgTurnaround);
        System.out.println("Average Waiting Time: " + avgWaiting);
        
        sc.close();
    }
}
