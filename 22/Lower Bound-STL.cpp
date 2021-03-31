#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,t;
    cin>>n;
    vector<int> a(n);
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    sort(a.begin(), a.end());
    vector<int>::iterator lower;
    
    cin>>t;
    while(t--)
    {
        int p=0;
        cin>>p;
        lower = lower_bound(a.begin(), a.end(), p);
        for(int i=0;i<n;i++){
            if(a[i]==p){
                
                cout<<"Yes "<<i+1<<endl;
                break;
            }
            else
            {
                if(i==n-1){
                cout<<"No "<<(lower - a.begin() + 1)<<endl;}
            }
        }
    }
    return 0;
}
