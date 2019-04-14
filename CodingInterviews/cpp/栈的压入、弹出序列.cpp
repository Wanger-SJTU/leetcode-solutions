class Solution {
public:
    bool IsPopOrder(vector<int> pushV, vector<int> popV) 
    {
        stack<int> st;
        int id=0;
        for(int i=0;i<popV.size();++i){
            while(st.empty()||st.top()!=popV[i]){
                st.push(pushV[id++]);
                if(id>pushV.size()){
                    return false;
                }
            }
            st.pop();
        }
        if(st.empty())
            return true;
        else
            return false;
    }
};