#include <iostream>
#include <vector>
using namespace std;

bool possible(vector<int>& V, int N, int M) {
	long long int my_wood = 0;
	for (auto i : V) {
		my_wood += max(0, i - N);
	}
	return my_wood >= (long long int)M;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int N, M, t;
	vector<int> V;
	int VMax = -2147483648, VMin = 0;
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> t;
		V.push_back(t);
		if (VMax < t) VMax = t;
	}
	//VMin: 잘랐을 때 반드시 M을 얻을 수 있는 임의의 값
	//VMax: 잘랐을 때 절대 M을 얻을 수 없는 임의의 값
	int center;
	while (VMin < VMax) {
		if (VMin + 1 == VMax) break;
		center = (VMin + VMax) / 2;
		if (possible(V, center, M)) { VMin = center; }
		else VMax = center;
	}
	cout << VMin;
	return 0;
}