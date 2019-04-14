class Solution
{
public:
    void push(int node) {
        stack1.push(node);
    }

    int pop() {
        int res = 0;
        if (stack2.size()>0)
        {
            res = stack2.top();
            stack2.pop();
        }
        else
        {
            while(stack1.size() > 0)
            {
                stack2.push(stack1.top());
                stack1.pop();
            }
             res = stack2.top();
             stack2.pop();
        }
       
        return res;
    }

private:
    stack<int> stack1;
    stack<int> stack2;
};