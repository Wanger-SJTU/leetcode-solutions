class Solution {
public:
    void push(int value) {
        if(restore.empty()||minStack.top() >= value)
        {
            minStack.push(value);
        }
        restore.push(value);
    }
    void pop() 
    {
        if(restore.top() == minStack.top())
            minStack.pop();
        restore.pop();
    }
    int top() {
        return restore.top();
    }
    int min() {
        return minStack.top();
    }
private:
    stack<int> minStack;
    stack<int> restore;
};