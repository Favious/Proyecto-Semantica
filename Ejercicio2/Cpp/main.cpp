#include <bits/stdc++.h>
using namespace std;

#define ll long long

ll russianPeasant(ll n, ll m) {
  ll ans = 0;
  while(m > 0) {
    if(m & 1) 
      ans = ans + n;
    n = n << 1;
    m = m >> 1;
  }
  return ans;
}

int main() {
  ll n, m;
  cout << "MULTIPLICACION RUSA" << endl;
  cout << "-------------------" << endl;
  cout << "Ingrese el primer numero:" << endl;
  cin >> n;
  cout << "Ingrese el segundo numero:" << endl;
  cin >> m;
  cout << russianPeasant(n, m) << endl;
}
