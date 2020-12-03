#include <bits/stdc++.h>
using namespace std;
using namespace std::chrono;

#define ll long long

ll russianPeasant(ll n, ll m) {
  ll ans = 0;
  while(m > 0) {
    if(m % 2 != 0) 
      ans = ans + n;
    n = n * 2;
    m = m / 2;
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
  auto start = high_resolution_clock::now();
  cout << russianPeasant(n, m) << endl;
  auto end = high_resolution_clock::now();
  auto duration = duration_cast<microseconds>(end - start);
  cout << "Tiempo de ejecucion: " << duration.count() << endl;
}
