class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int>combined;
        double median;
        for(auto num1 : nums1){
            combined.push_back(num1);
        }
        for(auto num2 : nums2){
            combined.push_back(num2);
        }
        sort(combined.begin(),combined.end());
        if(combined.size() % 2 != 0){
            median = combined[int(combined.size() / 2)];
            return median;
        }
        else{
            std :: cout << double(combined[int((combined.size()/2) - 1)])<< std :: endl;
            std :: cout << double(combined[int(combined.size()/2)]) << std :: endl;
            median = (double(combined[int((combined.size()/2) - 1)])+ double(combined[int(combined.size()/2)]))/2;
            return median;
        }
    }
    
};