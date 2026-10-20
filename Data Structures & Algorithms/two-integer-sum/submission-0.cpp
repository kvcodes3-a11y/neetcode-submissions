class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        for(int i = 0; i < nums.size(); i++)
        {
            res.clear();
            res.push_back(i);
            for(int j = 0; j < nums.size() && j != i; j++)
            {
                if(nums[j] + nums[i] == target)
                {
                    res.insert(res.begin(), j);
                    return res;
                }
            }
        }
    }
};
