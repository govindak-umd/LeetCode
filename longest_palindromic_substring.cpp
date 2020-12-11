class Solution {
public:
    bool isPalindorme(string s){
    if( equal(s.begin(), s.begin() + s.size()/2, s.rbegin()) )
        return true;
    else
        return false;
        
    }
    
    string longestPalindrome(string s) {
        std::vector<char>palindrome_vec;
        for (auto every_char: s){
            palindrome_vec.push_back(every_char);
        }
        int vec_len = palindrome_vec.size();
        string temp = "";
        for (int idx = 0; idx < vec_len; idx++){
        }
            
        if (isPalindorme(s) == true){
            return "yes";
        }
        else{
            return "no";
        }
    }

            
    
};