#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int N;
	cin >> N;
	string s;
	int t;
	int cnt[4] = {0};
	for (int i = 0; i < N; i++) {
		cin >> s >> t;
		switch (s[0]) {
		case 'S':
			cnt[0] += t;
			break;
		case 'B':
			cnt[1] += t;
			break;
		case 'L':
			cnt[2] += t;
			break;
		case 'P':
			cnt[3] += t;
			break;
		default:
			throw "Invalid string input";
		}
	}
	for (int i = 0; i < 4; i++) {
		if (cnt[i] == 5) {
			cout << "YES";
			return 0;
		}
	}
	cout << "NO";
	return 0;
}