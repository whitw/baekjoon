#include <iostream>
#include <algorithm>
using namespace std;

void p2096() {
	int(*map)[3];
	int(*MDP)[3];
	int(*mDP)[3];
	int N, t;
	cin >> N;
	map = new int[N][3];
	MDP = new int[2][3];//MDP[i][j] := i번째에 j를 밟았을 때 얻을 수 있는 최댓값
	mDP = new int[2][3];//mDP[i][j] := i번째에 j를 밟았을 때 얻을 수 있는 최솟값
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 3; j++) {
			cin >> t;
			map[i][j] = t;
		}
	}
	for (int j = 0; j < 3; j++) {
		mDP[1][j] = MDP[1][j] = map[N - 1][j];
		mDP[0][j] = MDP[0][j] = map[N - 1][j];
	}
	for (int i = N - 2; i >= 0; i--) {
		MDP[0][0] = map[i][0] + max(MDP[1][0], MDP[1][1]);
		mDP[0][0] = map[i][0] + min(mDP[1][0], mDP[1][1]);
		MDP[0][1] = map[i][1] + max(max(MDP[1][0], MDP[1][1]), MDP[1][2]);
		mDP[0][1] = map[i][1] + min(min(mDP[1][0], mDP[1][1]), mDP[1][2]);
		MDP[0][2] = map[i][2] + max(MDP[1][1], MDP[1][2]);
		mDP[0][2] = map[i][2] + min(mDP[1][1], mDP[1][2]);
		for (int j = 0; j < 3; j++) {
			MDP[1][j] = MDP[0][j];
			mDP[1][j] = mDP[0][j];
		}
	}
	cout << max(max(MDP[0][0], MDP[0][1]), MDP[0][2]) << ' ';
	cout << min(min(mDP[0][0], mDP[0][1]), mDP[0][2]);
	delete[] map;
	delete[] MDP;
	delete[] mDP;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	p2096();
	return 0;
}