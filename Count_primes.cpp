class Solution {
public:
    int countPrimes(int n) {
        int num_primes = 0;
        int sub_count = 0;
        std::vector<int>recorded_primes;
        for(int i =2 ;i < n; i ++){
            sub_count = 0;
            std::vector<int>::iterator it = std::find(recorded_primes.begin(), recorded_primes.end(), i);
            if (it != recorded_primes.end()){
                num_primes+=1;
            }
            else{
                for(int j = 2 ;j < i; j ++){
                    if (i%j==0){
                        sub_count+=1;
                        break;
                    }
                }
                if (sub_count == 0){
                    recorded_primes.push_back(i);
                    num_primes+=1;
                }
            }
        }
        return num_primes;
    }
};