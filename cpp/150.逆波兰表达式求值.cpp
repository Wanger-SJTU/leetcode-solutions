#include "leetcode.h"
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> sta;
       for(string& str:tokens){
           if(str=="+"||str=="-"||str=="*"||str=="/"){
               int num2=sta.top();
               sta.pop();
               int num1=sta.top();
               sta.pop();
               if(str=="+") sta.push(num1+num2);
               else if(str=="-") sta.push(num1-num2);
               else if(str=="*") sta.push(num1*num2);
               else sta.push(num1/num2);
           }
           else sta.push(stoi(str));
       }
       return sta.top();
    }
};