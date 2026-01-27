import java.util.*;

public class FCFS {
    static class Process {
        int id;
        int arrivalTime;
        int burstTime;
        int completionTime;
        int turnaroundTime;
        int waitingTime;

        Process(int id, int arrivalTime, int burstTime) {
            this.id = id;
            this.arrivalTime = arrivalTime;
            this.burstTime = burstTime;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("=== FCFS Scheduling ===");
        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();
        
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
        
        
        int currentTime = 0;
        for (Process p : processes) {
            if (currentTime < p.arrivalTime) {
                currentTime = p.arrivalTime;
            }
            currentTime += p.burstTime;
            p.completionTime = currentTime;
            p.turnaroundTime = p.completionTime - p.arrivalTime;
            p.waitingTime = p.turnaroundTime - p.burstTime;
        }
        
        // Display results
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
