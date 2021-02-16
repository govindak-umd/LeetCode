class Solution {
public:
    bool canJump(vector<int>& nums) {
        int len = nums.size();
        if (len == 1){
            return true;
        }
        if (nums.at(0) == 0){
            return false;
        }
        nums.pop_back();
        int idx = 1; // idx in the list from 1 - > length of the list
        int prev_high = 0;
        int global_prev_high = 0;
        for (auto curr_jump: nums){
            for (int i = 0; i <= curr_jump ; i ++){
                cout << " curr_jump : " << curr_jump << endl;
                cout << " i : " << i << endl;
                cout << " idx : " << idx << endl;
                prev_high = idx + i;
                cout << " max _position reached : " << prev_high << endl;
                cout << " global_prev_high reached : " << global_prev_high << endl;
                cout << " ================ " << endl;
                if (i + idx == len ){
                    if (prev_high >= i + idx)
                        return true;
                }
                if (global_prev_high < prev_high){
                    global_prev_high = prev_high;
                }
            }
            cout << " --- NEXT JUMP ----" << endl;
            idx += 1;
        }
        return false;
    }
};

// Solution not found, so submitted this
//class Solution {
//public:
//    bool canJump(vector<int>& nums) {
//        int max_pos = 0;
//        int len = nums.size();
//        for (int i = 0; i <= max_pos; i++){
//            max_pos = max(nums[i]+i,max_pos);
//            if(max_pos>= len-1){
//                return true;
//            }
//        }
//        return false;
//    }
//};
//