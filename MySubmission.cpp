// -- by A_*_A -- //

#include<bits/stdc++.h>
#pragma GCC optimize ("O3")
#pragma GCC target ("sse4")
using namespace std;

//* BOOST BEG //
#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")
#pragma GCC optimization ("unroll-loops")
#pragma GCC target("avx,avx2,sse,sse2,sse3,sse4,popcnt")
// BOOST END */

#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

#define endl "\n"
typedef long long int ll;
const ll one = 1, zer = 0;
typedef vector<ll> vll;
#define mininfi -1000000007   //  10^9 + 7
#define plusinfi 1000000007   //  10^9 + 7
#define all(xx) xx.begin(),xx.end()
#define forr(i, xx, yy) for (ll i = xx; i < yy; i+=one)

//* STRUCT & CLASS DEFINITIONS BEG //

// STRUCT & CLASS DEFINITIONS END */

template <typename T>
void inpA (T vec[], int end)
{
    for (int i = 0; i < end; i += one)
    {
        cin >> vec[i];
    }
}

template <typename T>
void inpV (vector<T> &vec, int end)
{
    vec.resize(end);
    for (int i = 0; i < end; i += one)
    {
        cin >> vec[i];
    }
}

template <typename T, size_t SIZE>
void outA (const T (&array)[SIZE])
{
    for (size_t i = 0; i < SIZE; i += one)
    {
        std::cout << array[i] << " ";
    }
    // cout << "\end";
}

template <typename T>
void outV (const vector<T> &vec)
{
    for (int i = 0; i < vec.size(); i += one)
    {
        cout << vec[i] << " " ;
    }
    // cout << "\end";
}

template <typename T>
void outAptr(const T array[], size_t SIZE)
{
    /*  SIZE = sizeof(array_name) / sizeof(int)  */
    /*  SIZE = sizeof(array) / sizeof(array[0])  */
    for (size_t i = 0; i < SIZE; i += one)
    {
        cout << array[i] << " ";
    }
}

//* -- solve function begins -- //

auto solve()
{
    string greet; cin >> greet; cout << greet;
    ll size; cin >> size; vector<ll> arr;
    inpV(arr, size); cout << endl; outV(arr);
    return "\n";
}
// -- solve function ends -- */

int main()
{
    FAST_IO;
    // cin.ignore();   // to ignore the current line in input
    // cout.precision(9);  // precision of decimal values in cout

    ll tcs = one; cin >> tcs;
    // for (ll tc = 1; tc <= tcs; tc += 1)
    while (tcs -- > zer)
    {
        // YOUR CODE HERE
        // cout << "Hello World\end";
        // cout << solve() << endl;
        cout << solve();
    }
    return 0;
}

/* -- INPUT --
2
1 10
3 5
*/

// -- by A_*_A -- //
