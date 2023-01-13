#include <iostream>
#include <queue>
#include <cassert>
#include <queue>
using namespace std;

class comp {
public:
    bool operator()(pair<int, int> a, pair<int, int> b) {
        return a.first > b.first;
    }
};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int N, L;
    int t;
    cin >> N >> L;
    int* arr = new int[N];
    for (int i = 0; i < N; i++) {
        cin >> t;
        arr[i] = t;
    }
    priority_queue<pair<int,int>, vector<pair<int,int>>, comp> pq;
    //pair<int,int>: <value, index>
    int leftmostIdx = 0;//보다 작으면 무효
    bool firstOut = true;
    pair<int, int> top;
    for (int i = 0; i < N; i++) {
        leftmostIdx = i - L + 1;
        pq.push(make_pair(arr[i], i));
        while(true) {
            top = pq.top();
            if (top.second < leftmostIdx) {
                pq.pop();
            }
            else {
                break;
            }
        }
        if (firstOut) {
            firstOut = false;
        }
        else {
            cout << ' ';
        }
        cout << top.first;
    }
    delete[] arr;
    return 0;
}