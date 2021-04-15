class Solution {
public:
    string removeDuplicateLetters(string s) {
        string stk;
        size_t i = 0;
        for(size_t i = 0;i < s.size(); ++i)
        {
            if(stk.find(s[i]) != string::npos) 
                continue;
            while(!stk.empty()&& stk.back() > s[i]&& 
                s.find(stk.back(), i) != string::npos)
                stk.pop_back();
            stk.push_back(s[i]);
        }
        return stk;
    }
};