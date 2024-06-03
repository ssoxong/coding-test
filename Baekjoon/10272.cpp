#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

double dist(int x1, int y1, int x2, int y2) {
    return hypot(x1-x2, y1-y2);
}

double func(int i, int j, int n, vector<vector<double>>& d, vector<int>& x, vector<int>& y) {
    double& res = d[i][j];
    if (res >= 0) return res;
    if (i == n) return dist(x[j], y[j], x[n], y[n]);
    if (j == n) return dist(x[i], y[i], x[n], y[n]);
    int k = max(i, j) + 1;
    res = min(func(k, j, n, d, x, y) + dist(x[i], y[i], x[k], y[k]),
              func(i, k, n, d, x, y) + dist(x[j], y[j], x[k], y[k]));
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        vector<int> x(n + 1), y(n + 1);
        vector<vector<double>> d(n + 1, vector<double>(n + 1, -1));

        for (int i = 1; i <= n; i++) {
            cin >> x[i] >> y[i];
        }
        cout << fixed << func(1, 1, n, d, x, y) << '\n';
    }
    return 0;
}
