#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, choice;
    cout << "Enter number of processes: ";
    cin >> n;

    vector<int> pid(n), at(n), bt(n), ct(n), tat(n), wt(n);

    for (int i = 0; i < n; i++) {
        pid[i] = i + 1;
        cout << "\nProcess " << pid[i] << endl;
        cout << "Arrival Time: ";
        cin >> at[i];
        cout << "Burst Time: ";
        cin >> bt[i];
    }

    cout << "\nSelect Mode:\n";
    cout << "1. Non-Preemptive SJF (SRTF)\n";
    cout << "2. Preemptive SJF\n";
    cout << "Enter choice: ";
    cin >> choice;

    float totalTAT = 0, totalWT = 0;

    //NON-PREEMPTIVE SJF =================
    if (choice == 1) {
        vector<bool> done(n, false);
        int time = 0, completed = 0;

        while (completed < n) {
            int idx = -1;
            int minBT = 1e9;

            for (int i = 0; i < n; i++) {
                if (at[i] <= time && !done[i] && bt[i] < minBT) {
                    minBT = bt[i];
                    idx = i;
                }
            }

            if (idx == -1) {
                time++;
                continue;
            }

            time += bt[idx];
            ct[idx] = time;
            tat[idx] = ct[idx] - at[idx];
            wt[idx] = tat[idx] - bt[idx];

            totalTAT += tat[idx];
            totalWT += wt[idx];

            done[idx] = true;
            completed++;
        }
    }

    // PREEMPTIVE SJF
    else if (choice == 2) {
        vector<int> rt = bt;   
        int time = 0, completed = 0;

        while (completed < n) {
            int idx = -1;
            int minRT = 1e9;

            for (int i = 0; i < n; i++) {
                if (at[i] <= time && rt[i] > 0 && rt[i] < minRT) {
                    minRT = rt[i];
                    idx = i;
                }
            }

            if (idx == -1) {
                time++;
                continue;
            }

            rt[idx]--;
            time++;

            if (rt[idx] == 0) {
                ct[idx] = time;
                tat[idx] = ct[idx] - at[idx];
                wt[idx] = tat[idx] - bt[idx];

                totalTAT += tat[idx];
                totalWT += wt[idx];
                completed++;
            }
        }
    }

    else {
        cout << "Invalid choice!";
        return 0;
    }

    cout << "\nPID\tAT\tBT\tCT\tTAT\tWT\n";
    for (int i = 0; i < n; i++) {
        cout << pid[i] << "\t"
             << at[i] << "\t"
             << bt[i] << "\t"
             << ct[i] << "\t"
             << tat[i] << "\t"
             << wt[i] << endl;
    }

    cout << "\nAverage Turnaround Time = " << totalTAT / n;
    cout << "\nAverage Waiting Time    = " << totalWT / n;

    
}