class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int c;
        for(int i = 0; i<nums.size(); i++)
        {
            c = 0;
            for(int j = 0; j<nums.size(); j++)
            {
                if(nums[i] == nums[j] && i!=j)
                {
                    return true;
                }
            }
        }
        return false;
    }
};