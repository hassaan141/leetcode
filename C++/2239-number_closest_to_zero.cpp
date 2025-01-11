class Solution {
public:
    int findClosestNumber(vector<int>& nums) {

        int small = nums[0];
        int otherSmall = false;
        for(int i=1; i<nums.size(); i++){

            if(std::abs(nums[i]) < std::abs(small)){
                small=nums[i];
                otherSmall = false;
            }
            if(nums[i] == small*-1){
                otherSmall=true;
            }
        }
        return otherSmall? abs(small): small;     
    }

};