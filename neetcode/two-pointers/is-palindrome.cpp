class Solution {
public:
    bool isPalindrome(string s) {

        int left = 0;
        int right = s.size() -1;

        for (int left = 0, right = s.size()-1; left<right;){
            if (std::isalnum(s[left]) && std::isalnum(s[right])){

                if(char(tolower(s[left])) == char(tolower(s[right])) ){
                    right--;
                    left++;
                } else {
                    return false;
                }

            } else if (!(std::isalnum(s[left]))){
                left++;
            }else{
                right--;
            }
        }

        return true;
        
    }
};
