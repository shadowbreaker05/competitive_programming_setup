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

// type names
typedef long long int ll;
typedef vector<ll> vll;
typedef pair<ll, ll> pll;
typedef map<ll, ll> mll;

const ll one = 1, zer = 0;
const ll modd = 1e9 + 7;     //  10^9 + 7
#define mininfi -1000000007   //  10^9 + 7
#define plusinfi 1000000007   //  10^9 + 7

// macros
#define all(xx) xx.begin(),xx.end()
#define allrev(xx) xx.rbegin(), xx.rend()
#define sum(xx) accumulate(all(xx), 0)
#define forr(xx, yy) for (ll i = xx; i < yy; i += 1)
#define setprecisionn(xx) cout << fixed << setprecision(xx)

#define vec_max(xx) (ll)*max_element(all(xx))
#define vec_min(xx) (ll)*min_element(all(xx))

auto maxll = [](ll x, ll y)   { if (x > y) return x; else return y; };
auto minll = [](ll x, ll y)   { if (x < y) return x; else return y; };
auto vec_sorted = [](vll xx) { vll yy(xx); sort(all(yy)); return yy; };
auto vec_sortedrev = [](vll xx) { vll yy(xx); sort(allrev(yy)); return yy; };
// auto vec_sortedrev = [](vll xx) { vll yy(xx); sort(all(yy), greater<int>()); return yy; };
auto roundnum = [](double xx, ll yy) -> double { return (double)((int)(xx * pow(10, yy) + 0.5)) / pow(10, yy); };

template <typename T1>
inline void inpV (vector<T1> &vec, ll num1)
{
	vec.resize(num1);
	forr (0, num1) cin >> vec[i];
}

template <typename T1>
inline void outV (const vector<T1> &vec)
{
	forr (0, vec.size()) cout << vec[i] << " " ; cout << "\n";
}

template<typename T1, size_t N>
inline size_t array_size(const T1(&)[N]) {
	return N;
}

// int solveutil() { }

string solve(ll* tc)
{
	auto greet = []() { return "Hello World!"; };


	if (tc) {
		// Code Begins Here

		cout << greet() << endl;

		// Code Ends here

		return "";
	}
	else {
		return greet();
	}
}

int main()
{
	FAST_IO;
	// freopen("inputf.txt", "r", stdin);
	// freopen("outputf.txt", "w", stdout);
	ll tcs = 1;
	cin >> tcs;
	string (*fptr)(ll*) = solve;
	while (tcs -- > zer) cout << (*fptr)(&tcs);
	return 0;
}

// -- by A_*_A -- //

/*

// ASCII VALUES
'A' -> 65, 'Z' -> 90,
'a' -> 96, 'z' -> 122,
'0' -> 48, '1' -> 49, 9' -> 57

// cycle back of integer values due to overflow
INT_MAX + 1 == INT_MIN
INT_MIN - 1 == INT_MAX

// arithmetic calculations take place in higher datatype
int a = 100000, b = 100000;
long long int c = a * b;		// will give wrong value
long long int c = a * 1LL * b; 	// will give right value

// in a 64 bit system
cout << sizeof(char) << endl;					// 1
cout << sizeof(int) << endl;					// 4
cout << sizeof(const) << endl;					// 4
cout << sizeof(unsigned) << endl;				// 4
cout << sizeof(signed) << endl;					// 4

built in function to countsetbits in x: __builtin_popcount(x)

int - to_string()
char - isalpha(), isdigit()
string - getline(), push_back(), pop_back(), size() or length(), stoi(), reverse(), s.substr()
vector - push_back(), pop_back(), front(), back(), reserve(), size(), empty(), clear(), erase(), begin(), end()
list - push_back(), pop_back(), push_front(), pop_front(), merge(), sort(), reverse(), size()
map, set, multiset, multimap - insert(), erase(), find(), size(), count(), empty(), clear()
bitset - size(), count(), all(), any(), none(), set(), reset(), flip(), test()
deque - push_back(), push_front(), pop_back(), pop_front()
stack - push(), pop(), top(), empty(), size()
queue - push(), pop(), front(), back(), empty(), size()
priority_queue -

// accessing vector pairs using addresses
vector<pair<int, string>> arr
(&arr[0])->first
(*&arr[0]).first

// vector iterator
vector - vector<int>::iterator vptr;

// copy one string to another
char * strcpy ( char * destination, const char * source );

// copies the first num characters of source C string to destination C string
char * strncpy ( char * destination, const char * source, size_t num );

// Sets the first num bytes of the block of memory pointed by ptr to the specified value (interpreted as an unsigned char)
void * memset ( void * ptr, int value, size_t num );

*/