#include "leetcode.h"
class Solution {
public:
   int calculate(string s) {
		int n = 0;
		return p(s, n);
	}
	bool skip(const string& s, int& n) {
		for (;;) {
			if (s.length() <= n) {
				return true;
			}
			if (s[n] == ' ') {
				n++;
			} else {
				return false;
			}
		}
	}
	int p(const string& s, int& n) {
		return a(s, n) + p1(s, n);
	}
	int p1(const string& s, int& n) {
		if (skip(s, n)) {
			return 0;
		}
		if (s[n] == '+') {
			n++;
			return a(s, n) + p1(s, n);
		} else if (s[n] == '-') {
			// s[n] == '-'
			n++;
			return -a(s, n) + p1(s, n);
		} else {
			return 0;
		}
	}
	int a(const string& s, int& n) {
		skip(s, n);
		if (s[n] == '(') {
			n++;
			int t = p(s, n);
			skip(s, n);
			// s[n] == ')'
			n++;
			return t;
		} else {
			// number
			int t = 0;
			while (isdigit(s[n])) {
				t = t * 10 + (s[n] - '0');
				n++;
			}
			return t;
		}
	}
};