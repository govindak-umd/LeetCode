// This solution is the brute force approach. It works and passed a number of test
// cases. However, might cause an issue of time limit exceeded, hence need to refine the code
// a bit. However, the logic is right and will output the correct solution.

class Solution {
public:
    bool isPalindrome(string s){
    if( equal(s.begin(), s.begin() + s.size()/2, s.rbegin()) )
        return true;
    else
        return false;
        
    }
    string longestPalindrome(string s) {
        int len_string = s.size();
        string best_temp;
        string temp;
        int temp_len = 0;
        int temp_len_sub = 0;
        if(s.size() == 1){
            return s;
        }
        else{
            for (int idx = 0; idx < len_string; idx++){
                for(int idx_sub = idx; idx_sub < len_string; idx_sub++){
                    temp = s.substr(idx, len_string - idx_sub);
                    if (isPalindrome(temp) == true){
                        temp_len_sub = temp.size();
                        if (temp_len_sub >= temp_len){
                            best_temp = temp;
                            temp_len = temp_len_sub;
                        }
                    }
                }
            }
        }
        return best_temp;
    }
    
};