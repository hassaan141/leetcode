// class Solution {
// public:
//     bool hasDuplicate(vector<int>& nums) {

//         std::vector<int> single = {};
//         for(int i=0; i<nums.size(); i++){

            
//             bool exists = checkArr(single, nums[i]);

//             if(exists){
//                 return true;
//             }
//             else{
//                 single.push_back(nums[i]);
//             }

//         }

//         return false;
//     }

//     bool checkArr(vector<int> &single, int nums){
//         for(int i = 0; i<single.size(); i++){
//             if (single[i] == nums){
//                 return true;
//             }
//         }
//         return false;
//     }
// };

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        std::unordered_set<int> list;

        for(int i =0; i<nums.size(); i++){
            
            if(list.find(nums[i]) != list.end()){
                return true;
            }else{
                list.insert(nums[i]);
            }
        }

        return false;
    }

};
