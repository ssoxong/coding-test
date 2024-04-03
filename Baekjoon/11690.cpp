#include <iostream>
using namespace std;
typedef long long ll;

int check[100000001];

void sieve(int n){
    for (int i=2; i<n+1;i++){
        if (check[i]) continue;
        for (int j=i+i; j<n+1;j+=i) check[j] = 1;
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n;
    cin>>n;
    sieve(n);
    ll ans = 1;
    for (int i=2;i<=n;i++){
        if (i%2==0&&i!=2) continue;
        if (!check[i]){
            ll tmp = 1;
            while (tmp*i<=n) tmp*=i;
            ans = (ans*tmp)%4294967296;
        }
    }
    cout<<ans;
}