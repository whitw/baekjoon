#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


ostream& operator<<(ostream& o, pair<int, int> p) {
	o << '<' << p.first << ',' << p.second << '>';
	return o;
}

template<typename T>
ostream& operator<<(ostream& o, vector<T> v) {
	o << "vector(";
	for (T i : v) {
		o << i << " ";
	}
	o << ")";
	return o;
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int N;

	cin >> N;
	int score = 0;
	int prevFirst = 0;
	int prev = 0;
	for (int i = 0; i < N; i++) {
		int t;
		cin >> t;
		if (t == prev + 1) {
			prev = t;
		}
		else {
			score += prevFirst;
			prevFirst = prev = t;
		}
		if (i == N - 1) {
			score += prevFirst;
		}
	}
	cout << score;
	return 0;
}