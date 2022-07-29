#include <iostream>
#include <queue>
#define INF 1e9
using namespace std;

int main() {
    int N = 0;
    int W[16][16];
    int** C;
    int result = INF;

    cin >> N;
    C = new int*[(1 << N)];

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> W[i][j];
            if (W[i][j] == 0) {
                W[i][j] = INF;
            }
        }
    }
    for (int i = 0; i < (1 << N); i++) {
        C[i] = new int[N];
        for (int j = 0; j < N; j++) {
            C[i][j] = INF;
        }
    }
    queue<pair<int, int>> q; //(state, position)
    q.push(make_pair(1, 0));
    C[1][0] = 0;
    while (!q.empty()) {
        pair<int, int> p = q.front();
        //cout << "p=(" << p.first << ", " << p.second << ")\n";
        q.pop();
        if (p.first == (1 << N) - 1) {
            int t = C[p.first][p.second] + W[p.second][0];
            if (result > t) result = t;
            continue;
        }
        for (int i = 0; i < N; i++) {
            if ((~p.first) & (1 << i)) { //not visited here,
                if (W[p.second][i] != INF) { //and can go there
                    int t = C[p.first][p.second] + W[p.second][i];
                    int newState = p.first | (1 << i);
                    int newPosition = i;
                    if (C[newState][newPosition] == INF) {
                        C[newState][newPosition] = t;
                        q.push(make_pair(newState, newPosition));
                    }
                    else {
                        if (C[newState][newPosition] > t) {
                            C[newState][newPosition] = t;
                            q.push(make_pair(newState, newPosition));
                        }
                    }
                }
            }
        }
    }
    cout << result;
    for (int i = 0; i < (1 << N); i++) {
        delete[] C[i];
    }
    delete[] C;
    return 0;
}