class Solution {
public:
  vector<vector<int>> combinationSum2(vector<int> &candidates, int target) {
    vector<int> cur_res;
    sort(candidates.begin(), candidates.end());
    search(candidates, 0, candidates.size(), cur_res, target);
    return res;
  }

private:
  vector<vector<int>> res;
  void search(vector<int> candidates, int srt, int n, vector<int> cur_res,
              int target) {
    if (target == 0) {
      res.push_back(cur_res);
      return;
    }

    for (int i = srt; i < n && target - candidates[i] >= 0; i++) {
      if (i == srt || candidates[i] != candidates[i - 1]) {
        cur_res.push_back(candidates[i]);
        search(candidates, i + 1, n, cur_res, target - candidates[i]);
        cur_res.pop_back();
      }
    }
  }
};