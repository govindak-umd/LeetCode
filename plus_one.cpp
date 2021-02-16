class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        string num= "";
        for(auto digit: digits){
            string dig = std::to_string(digit);
            num+=dig;
        }
        long int num2 = stoll(num);
        num2+=1;
        string number_string = std::to_string(num2);
        std::vector<char> v(number_string.begin(), number_string.end());
        for (const char &c: v)
            std::cout << c << endl;
        std::vector<int> intNumbers;
        for (const auto& c : v)
            intNumbers.push_back(c-48);
        return intNumbers;
    }
};