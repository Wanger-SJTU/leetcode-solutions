class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map <string,vector<string> > m;
        for(string& s : strs)
        {
            string t = s;
            sort(t.begin(),t.end());
            m[t].push_back(s);   //t为单词的按顺序排列，作为key值，m[t]则为该单词的异位词构成的vector，作为value值
        }
        for(auto& n : m)                //n为键和值组成的pair
            res.push_back(n.second);
        return res;
    }
};