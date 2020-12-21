class Solution {
public:
    int maxArea(vector<int>& height) {
        int prev;
        int idx = 0;
        std::vector<int> all_covered;
        int area;
        for (auto vec: height){
            all_covered.push_back(vec);
            std::cout << vec << std :: endl;
            if (idx > 0){
                for (int i = 0; i <= all_covered.size(); i++ ){
                    std ::cout << i << vec << std :: endl;
                    // if (all_covered[i] >= vec){
                    //     int new_area = vec*(i-1);
                    //     if (new_area > area)
                    //         area = new_area;
                    //     std :: cout << "area " << vec << " and " << i << " = "<< vec*(i-1) << std :: endl;
                    // }
                }
            }
            idx +=1;
            std :: cout << " --- " << std :: endl;
        }
        return area;
    }
};