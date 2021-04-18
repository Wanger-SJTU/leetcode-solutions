#include "leetcode.h"
class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        vector<string> res; 
        unordered_set<string> visited{{s}}; 
        queue<string> queue_record{{s}};
        bool found = false;
        while(!queue_record.empty()){
            string curStr = queue_record.front();
            queue_record.pop();
            if(IsValidString(curStr)) { 
                res.push_back(curStr);
                found = true;
            }
            if(found) {
                continue;
            }
            for(int i = 0; i < curStr.size(); i++){
                if(curStr[i] != '(' && curStr[i] != ')' ) {
                    continue;
                }
                string tmp = curStr.substr(0,i)+curStr.substr(i+1, curStr.size()-1);
                if(!visited.count(tmp)) { 
                    queue_record.push(tmp);
                    visited.insert(tmp);
                }
            }
        }
        return res;
    }

    bool IsValidString(string curStr)
    {
        int cnt = 0;
        for(int i = 0; i < curStr.size(); i++){
            if(curStr[i] == '(') {
                ++cnt;
            }
            else if (curStr[i] == ')' && --cnt < 0) {
                return false;
            }
        }
        return cnt==0;
    }
    
};