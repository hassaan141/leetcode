class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        //first value is the value that we looked at, second is the index it was at
        std::unordered_map<int, int> map;

        for(int i = 0; i<nums.size(); i++){
            if(map.count(target - nums[i])){
                return {map[target - nums[i]], i};
            }else{
                map[nums[i]] = i;
            }
        }
        
    }
};

/*
    first iteration: 

    [{3, 4}  ]



*/