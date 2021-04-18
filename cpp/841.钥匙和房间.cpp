#include "leetcode.h"
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int N = rooms.size();
        vector<bool> visited(N, false);
        visited[0] = true;
        queue<int> queuePath;
        for (auto next : rooms[0]) {
            if (!visited[next]) {
                queuePath.push(next);
            }
        }
        while (!queuePath.empty()) {
            int cur = queuePath.front();
            queuePath.pop();
            visited[cur] = true;
            for (auto next : rooms[cur]) {
                if (!visited[next]) {
                    queuePath.push(next);
                }
            }
        }
        for(auto item : visited){
            if(!item){
                return false;
            }
        }
        return true;
    }
};