#include <iostream>
using namespace std;

int main()
{
    int t, n, a, b;
    cin >> t;
    while (t--)
    {
        cin >> n >> a >> b;
        int mn = 1000000000;
        for (int i = 1; i <= n; ++i)
        {
            mn = min(mn, ((a * i * i) + (b * (n - i) * (n - i))));
        }
        cout << mn;
    }
}