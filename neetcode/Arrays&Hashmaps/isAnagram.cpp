class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;

        std::unordered_map<char, int> s_map;
        std::unordered_map<char, int> t_map;

        for(int i = 0; i<s.length(); i++){
            s_map[s[i]]++;
            t_map[t[i]]++;

        }

        for (auto i: s_map){
            std::cout<<i.first<<" "<<i.second<<std::endl;
        }
        for (auto i: t_map){
            std::cout<<i.first<<" "<<i.second<<std::endl;
        }
        for(auto c: s_map){
            char key = c.first;
            if(c.second != t_map[key]){
                return false;
            }
        }

        return true;

    }
};