class Solution {
public:
    string reverseWords(string s) {
        int n = s.size();
        if(!n) return s;
        int left = 0, right = 0;
        while(right<n){
            while(right < n && s[right] != ' ') right++; //找到下一个空格
            int next = right-- + 1; //next是翻转完这个单词之后，left和right接下来要反转的单词的开始
            while(left<right) swap(s[left++],s[right--]); //原地翻转
            left = next; right = next; //指针跳到下一个判断位
        }
        return s;
    }
};