import java.util.*;

public class RoundRobin {
    static class Process {
        int id;
        int arrivalTime;
        int burstTime;
        int remainingBurst;
        int completionTime;
        int turnaroundTime;
        int waitingTime;

        Process(int id, int arrivalTime, int burstTime) {
            this.id = id;
            this.arrivalTime = arrivalTime;
            this.burstTime = burstTime;
            this.remainingBurst = burstTime;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("=== Round Robin Scheduling ===");
        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();
        System.out.print("Enter time quantum: ");
        int quantum = sc.nextInt();
        
        List<Process> processes = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            System.out.println("\nProcess " + (i + 1) + ":");
            System.out.print("Arrival Time: ");
            int arrival = sc.nextInt();
            System.out.print("Burst Time: ");
            int burst = sc.nextInt();
            processes.add(new Process(i + 1, arrival, burst));
        }
        
        
        processes.sort((p1, p2) -> p1.arrivalTime - p2.arrivalTime);
        
        Queue<Process> queue = new LinkedList<>();
        int currentTime = 0;
        int completed = 0;
        
        while (completed < n) {
            
            for (Process p : processes) {
                if (p.arrivalTime <= currentTime && p.remainingBurst > 0 && !queue.contains(p)) {
                    queue.add(p);
                }
            }
            
            if (queue.isEmpty()) {
                currentTime++;
                continue;
            }
            
            Process p = queue.poll();
            
            if (p.remainingBurst <= quantum) {
                currentTime += p.remainingBurst;
                p.completionTime = currentTime;
                p.remainingBurst = 0;
                p.turnaroundTime = p.completionTime - p.arrivalTime;
                p.waitingTime = p.turnaroundTime - p.burstTime;
                completed++;
            } else {
                currentTime += quantum;
                p.remainingBurst -= quantum;
                queue.add(p);
            }
        }
        

        System.out.println("\n=== Results ===");
        System.out.printf("%-5s %-12s %-12s %-15s %-15s %-12s\n", 
                         "ID", "Arrival", "Burst", "Completion", "Turnaround", "Waiting");
        System.out.println("--".repeat(45));
        
        double avgTurnaround = 0, avgWaiting = 0;
        for (Process p : processes) {
            System.out.printf("%-5d %-12d %-12d %-15d %-15d %-12d\n",
                            p.id, p.arrivalTime, p.burstTime, 
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
