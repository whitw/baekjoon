#include <iostream>
using namespace std;

int K, N;
int* arr;

bool possible(int X) {
	int result = 0;
	for (int i = 0; i < K; i++) {
		result += (arr[i] / X);
	}
	return result >= N;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> K >> N;
	arr = new int[K];
	for (int i = 0; i < K; i++) {
		cin >> arr[i];
	}
	long long int min=1, max= 4294967296;
	//min: min의 길이로 잘랐을 때 반드시 N개 이상의 랜선을 얻을 수 있음
	//max: max의 길이로 잘랐을 때 반드시 N개 미만의 랜선을 얻을 수 있음
	//최적해: min + 1 == max, min.
	while (min < max) {
		long long int mid = (min + max) / 2;
		if (possible(mid)) {
			min = mid;
		}
		else {
			max = mid; 
		}
		if (min + 1 == max) {
			cout << min;
			break;
		}
	}
	delete[] arr;
	return 0;
}