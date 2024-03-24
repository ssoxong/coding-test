#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long long ll;

ll mid[999] = {0, };
ll *arr[999];

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ll n, m;
    cin>>n>>m;
    
    for(ll i=0; i<n; i++)
        arr[i] = new ll[999];

    for(ll i=0; i<m; i++)
        for(ll j=0; j<n; j++)
            cin>>arr[j][i];
   
    for(ll j=0; j<n; j++)
        sort(arr[j], arr[j]+m);

    for(ll i=0; i<n; i++)
    {
        if(m%2 == 1)
            mid[i] = arr[i][m/2];
        else
            mid[i] = (arr[i][m/2] + arr[i][m/2-1])/2; 
    }

    ll sum = 0;

    for(ll i=0; i<m; i++)
        for(ll j=0; j<n; j++)
            sum += abs(mid[j] - arr[j][i]);

    cout<<sum<<"\n";
    
    for(ll i=0; i<n-1; i++)
        cout<<mid[i]<<' ';

    cout<<mid[n-1]<<"\n";

    return 0;
}