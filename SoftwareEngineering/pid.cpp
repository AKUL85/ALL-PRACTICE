#include <bits/stdc++.h>
using namespace std;



int main() {
    ios::sync_with_stdio(false);
    cin.tie(&cout);

    int n ;
    cout << "Enter number of processes: ";
    cin>>n;

    vector<int> pid(n), at(n), bt(n), ct(n), tat(n), wt(n);

    for (int i = 0; i < n; i++) {
        pid[i] = i + 1;
        cout << "\nProcess " << pid[i] << endl;
        cout << "Arrival Time: ";
        cin >> at[i];
        cout << "Burst Time: ";
        cin >> bt[i];
    }
    // akul

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (at[i] > at[j]) {
                swap(at[i], at[j]);
                swap(bt[i], bt[j]);
                swap(pid[i], pid[j]);
            }
        }
    }

    int time = 0;
    float totalTAT = 0, totalWT = 0;

    for (int i = 0; i < n; i++) {
        if (time < at[i]){
            time = at[i];
        }
        ct[i] = time + bt[i];
        wt[i]=ct[i]-(at[i]+bt[i]);
        tat[i]=ct[i]-at[i];

        time = ct[i];

        totalTAT += tat[i];
        totalWT += wt[i];
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