// -- by A_*_A -- //

#include<bits/stdc++.h>
#pragma GCC optimize ("O3")
#pragma GCC target ("sse4")
using namespace std;

#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")
#pragma GCC optimization ("unroll-loops")
#pragma GCC target("avx,avx2,sse,sse2,sse3,sse4,popcnt")

#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define endl "\n"

typedef long long int ll;
typedef vector<ll> vll;
typedef pair<ll, ll> pll;
typedef map<ll, ll> mll;
typedef vll::iterator vlli;
typedef mll::iterator mlli;

const ll one = 1, zer = 0, mod = 1e9 + 7;
const string yes = "Yes", no = "No";

#define mininfi -1000000007   //  10^9 + 7
#define plusinfi 1000000007   //  10^9 + 7
#define all(xx) xx.begin(),xx.end()
#define sum(xx) accumulate(all(xx), 0)
#define max(xx) (ll)*max_element(all(xx))
#define min(xx) (ll)*min_element(all(xx))
#define forr(xx, yy) for (ll i = xx; i < yy; i += 1)

auto sorted = [](vll xx) { vll yy(xx); sort(all(yy)); return yy; };

template <typename tcs>
void inpV (vector<tcs> &vec, ll num1)
{
	vec.resize(num1);
	forr (0, num1) cin >> vec[i];
}

template <typename tcs>
void outV (const vector<tcs> &vec)
{
	forr (0, vec.size()) cout << vec[i] << " " ; cout << "\n";
}

namespace avantika {
string alice = "Alice";
string bob = "Bob";
}

string solve(ll* tc)
{
	ll modd = 1e9 + 7;
	auto greet = []() {
		return "Hello World\n";
	};
	if (tc) {
		vll arr;
		int x = 5, y = 3, z = 1;
		arr.push_back(x);
		arr.push_back(y);
		arr.push_back(z);
		for (auto x : arr)
			cout << x;
		cout << endl;
		for (vlli it = arr.begin(); it != arr.end(); it++)
			cout << *it;
		cout << endl;
		outV(arr);
		return "";
	}
	else {
		return greet();
	}
}

int main()
{
	FAST_IO;
	ll tcs = 1; cin >> tcs;
	string (*fptr)(ll*) = solve;
	while (tcs -- > zer) cout << (*fptr)(&tcs);
	return 0;
}

// -- by A_*_A -- //
