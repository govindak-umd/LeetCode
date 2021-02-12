class Solution {
public:
    int climbStairs(int n) {
        if (n == 1){
            return 1;
        }
        else if(n == 2){
            return 2;
        }
        else{
            long int fib_seq[n+1];
            fib_seq[0] = 1;
            fib_seq[1] = 2;
            for (int i=2 ; i < n +1 ; i ++ ){
                fib_seq[i] = fib_seq[i-1] + fib_seq[i-2];
            }
            cout << fib_seq[n-1] << endl;
            return fib_seq[n-1];
        }
    }
};