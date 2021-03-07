#include<bits/stdc++.h>
#define FIO std::ios::sync_with_stdio(false);
#define ll long long int
#define vi vector<int>
#define vc vector<char>
#define vs vector<string>
#define vvc vector<vc>
#define vll vector<ll>
#define vvi vector<vi>
#define pii pair<int, int>
#define vpii vector<pii>
#define si set<int>
#define sc set<char>
#define ss set<string>
#define sll set<ll>
#define mod 1000000007
using namespace std;

int groups(string A) {
	int count = 0;
	if (A[0] == '1')
		count++;

	for (int i = 1; i < A.length(); ++i) {
		if (A[i] == '1' && A[i - 1] == '0')
			count++;
	}

	return count;
}

int main() {
	FIO;
	int t;
	cin >> t;

	while (t--) {
		string S;
		cin >> S;

		cout << groups(S) << endl;
	}

	return 0;
}
