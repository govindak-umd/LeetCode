class Solution {
public:
    int maxArea(vector<int>& height) {
        std::vector<int> all_covered;
        int area = 0;
        int new_area = 0;
        for (int i = 0; i<height.size(); i++){
            for (int i2 = i; i2<height.size(); i2++){
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
            std :: cout << " -- " << std::endl;
        }
        std :: cout << " final area : " << area << std :: endl;
        return area;
    }
};