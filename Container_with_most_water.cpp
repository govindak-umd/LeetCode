class Solution {
public:
    int maxArea(vector<int>& height) {
        int area = 0;
        int new_area = 0;
        int len = height.size();
        for (int i = 0; i<len; i++){
            for (int i2 = i; i2<len; i2++){
                if (height[i2] > height[i]){
                    new_area = height[i] * (i2-i);
                }
                else {
                    new_area = height[i2] * (i2-i);
                }
                if(new_area > area){
                    area = new_area;
                }
            }
        }
        return area;
    }
};