#include <bits/stdc++.h>

using namespace std;

int main() {
	ios::sync_with_stdio(0), cin.tie(0);
	string s;
	while (getline(cin, s)) {
		if (s == ".") break;
		stack<char> st;
		bool isBalance = true;
		for (auto c : s) {
			if (c == '(' || c == '[') st.push(c);
			else if (c == ')') {
				if (st.empty() || st.top() != '(') {
					isBalance = false;
					break;
				}
				st.pop();
			}
			else if (c == ']') {
				if (st.empty() || st.top() != '[') {
					isBalance = false;
					break;
				}
				st.pop();
			}
		}
		if (!st.empty()) isBalance = false;
		if (isBalance) {
			cout << "yes\n";
		}
		else {
			cout << "no\n";
		}
	}
}