#include <bits/stdc++.h>
using namespace std;

#define ll long long

ll ackermann(ll m, ll n) {
  if (m == 0)
    return n + 1;
  if (n == 0)
    return ackermann(m - 1, 1);
  return ackermann(m - 1, ackermann(m, n - 1));
}

int main() {
  ll m, n;
  cout << "FUNCION DE ACKERMANN" << endl;
  cout << "--------------------" << endl;
  cout << "Ingrese el valor para m:" << endl;
  cin >> m;
  cout << "Ingrese el valor para n:" << endl;
  cin >> n;
  cout << "A(" << m << ", " << n << ") = " << ackermann(m, n) << endl;
}
