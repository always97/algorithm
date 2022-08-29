#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int ac_sum[1025][1025];

int main() {

	ios::sync_with_stdio(0);
	cin.tie(0);

	int N, M, num;
	cin >> N >> M;

	for (int y = 0; y < N; y++) {
		for (int x = 0; x < N; x++) {
			cin >> num;
			ac_sum[y + 1][x + 1] = ac_sum[y][x + 1] + ac_sum[y + 1][x] - ac_sum[y][x] + num;
		}
	}

	for (int i = 0; i < M; i++) {
		int x1, y1, x2, y2;
		cin >> y1 >> x1 >> y2 >> x2;
		int find_sum = ac_sum[y2][x2] - ac_sum[y1 - 1][x2] - ac_sum[y2][x1 - 1] + ac_sum[y1 - 1][x1 - 1];
		cout << find_sum << '\n';

	}

	return 0;
}