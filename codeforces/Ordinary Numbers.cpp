#include <bits/stdc++.h>
using namespace std;
 
int count_same_digit(int L, int R)
{
	long long int tmp = 0, ans = 0;
 
	long long int n = log10(R) + 1;
 
	for (long long int i = 0; i < n; i++) {
 
		tmp = tmp * 10 + 1;
 
		for (long long int j = 1; j <= 9; j++) {
 
			if (L <= (tmp * j)&& (tmp * j) <= R) {
				ans++;
			}
		}
	}
	return ans;
}
 
 
int main()
{
	long long int t;
	cin>>t;
	while(t--){
    long long int R;
	cin>>R;
	cout << count_same_digit(1, R)<< endl;
}
 
	return 0;
}
