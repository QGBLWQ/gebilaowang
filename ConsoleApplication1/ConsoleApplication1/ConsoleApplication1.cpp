﻿class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> combination;
        sort(candidates.begin(), candidates.end());
        dfs(candidates, target, 0, combination, result);
        return result;
    }

private:
    void dfs(vector<int>& candidates, int target, int start, vector<int>& combination, vector<vector<int>>& result) {
        if (target == 0) {
            result.push_back(combination);
            return;
        }

        for (int i = start; i < candidates.size(); i++) {
            if (candidates[i] > target) {
                break;
            }
            combination.push_back(candidates[i]);
            dfs(candidates, target - candidates[i], i, combination, result);
            combination.pop_back();
        }
    }
};