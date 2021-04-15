class Solution {
public:
    bool isValid(string s) {
        stack<char> record;
        for(auto c : s)
        {
            switch (c)
            {
                case '(':
                case '[':
                case '{':
                    record.push(c);
                    break;
                case ')':
                    if(record.empty()||record.top() !='(') 
                        return false;
                    else 
                        record.pop();
                        break;
                case ']':
                    if(record.empty()||record.top() !='[') 
                        return false;
                    else 
                        record.pop();
                        break;
                case '}':
                    if(record.empty()||record.top() !='{') 
                        return false;
                    else 
                        record.pop();
                        break;
                default:
                    break;
            }


        }
        return record.empty();
    }
};