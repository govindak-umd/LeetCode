class Solution {
public:
    bool isPalindrome(string s) {
        string new_string = "";
        for (char c: s){
            if(isalpha(c) or isdigit(c)){
                if(isalpha(c))
                    c = char(tolower(c));
                new_string+=c;
            }
        }
        int len = new_string.size();
        for(int i =0; i < len/2; i++){
            if (new_string[i]!=new_string[len-i-1]){
                return false;
            }
        }
        return true;
    }
};
