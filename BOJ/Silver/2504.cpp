#include <bits/stdc++.h>

using namespace std;
int main() {
	ios::sync_with_stdio(0), cin.tie(0);
	string str;
	cin >> str;
	bool isValid = true;
	stack<char> st;
	int result = 0, tmp = 1;
	
	for (unsigned i = 0; i < str.length(); i++) {

		if (str[i] == '(') {
			st.push(str[i]);
			tmp *= 2;
		}
		else if (str[i] == ')') {
			if (st.empty() || st.top() != '(') {
				isValid = false;
				break;
			}
			else if (st.top() == '(') {
				if (str[i - 1] == '(') {
					result += tmp;
				}	
					st.pop();
					tmp /= 2;
			}
		}
		else if (str[i] == '[') {
			st.push(str[i]);
			tmp *= 3;
		}
		else if (str[i] == ']') {
			if (st.empty() || st.top() != '[') {
				isValid = false;
				break;
			}
			else if (st.top() == '[') { 
				if (str[i - 1] == '[') {
					result += tmp;
				}
				st.pop();
				tmp /= 3;
			}
		}
	}
	if (!st.empty() || !isValid) result = 0;
	cout << result;
}