#include<bits/stdc++.h>
using namespace std;



int main(){
    long long t;
    cin>>t;
    while(t--){
        long long n,x;
        cin>>n>>x;
        map<long long,long long> m1;
        map<long long,long long> m2;
        vector<long long> v;
        for(long long i=0;i<n;i++)
        {
            long long temp;
            cin>>temp;
            m1[temp]++;
            m2[temp^x]++;
            v.push_back(temp);
        }
        long long m=0;
        long long int mi=1e18;
        for(long long int j=0;j<n;j++)
        {
            if(m1[v[j]]+m2[v[j]]>m  &&  mi>m2[v[j]]){
                m=m1[v[j]]+m2[v[j]];
                mi=m2[v[j]];
            }
        }
        cout<<m<<" "<<mi<<endl;


    }
}
