class Solution {
public:
  bool isMatch(string s, string p) {
    if (p.empty()) {
      return s.empty();
    }
    bool fristMatch = !s.empty() && (s[0] == p[0] || p[0] == '.');
    if (p.size() >= 2 && p[1] == '*') {
      return isMatch(s, p.substr(2, p.size())) ||
             (fristMatch && isMatch(s.substr(1, s.size()), p));
    } else {
      return fristMatch &&
             isMatch(s.substr(1, s.size()), p.substr(1, p.size()));
    }
  }
};