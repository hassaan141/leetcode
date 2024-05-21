public class Solution {
    public bool IsPalindrome(int x) {
        if(x<0){
            return false;
        }

        string newstr = x.ToString();
        char [] arr = newstr.ToCharArray();
        Array.Reverse(arr);
        string rev = new string(arr);
        int back = int.Parse(rev);

        if (x == back){
            return true;
        }
        else{
            return false;
        }
    }
}
