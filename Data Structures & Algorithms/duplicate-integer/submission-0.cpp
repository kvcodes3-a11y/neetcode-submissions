class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int c;
        for(int i = 0; i<nums.size(); i++)
        {
            c = 0;
            for(int j = 0; j<nums.size(); j++)
            {
                if(nums[i] == nums[j])
                {
                    c++;
                }
            }
            if(c>1)
            {
                return true;
            }
        }
        return false;
    }
};