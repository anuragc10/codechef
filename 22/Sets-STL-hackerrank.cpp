#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;
int main()
{
    set<int> s;
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        int a,b;
        cin>>a>>b;
        switch(a){
            case 1:
            s.insert(b);
            break;
            case 2:
            s.erase(b);
            break;
            case 3:
            set<int>::iterator itr=s.find(b);
            if (itr == s.end())
                cout<<"No"<<endl;
            else
                cout<<"Yes"<<endl;

        }
    }
}
