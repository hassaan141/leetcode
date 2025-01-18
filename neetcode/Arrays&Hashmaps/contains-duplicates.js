class Solution {
  /**
   * @param {number[]} nums
   * @return {boolean}
   */
  hasDuplicate(nums) {

      let singleArr=[nums[0]];
      for(let i =1; i<nums.length; i++){

          if(singleArr.includes(nums[i])){
              return true;
          }
          else{
              singleArr.push(nums[i])
          }
      }
      return false;
  }
}
