Recursive sequence:
A function F is defined as follows F(n)= (1) +(2*3) + (4*5*6) ... upto n terms (look at the examples for better clarity). Given an integer n, determine the F(n).
Note: As the answer can be very large, return the answer modulo 109+7

Solution:(Python)

class Solution:
    def sequence(self, n):
        mod = 10**9 + 7
        tot_sum = 0
        st_num = 1
        
        for i in range(1, n + 1):
            product = 1
            for j in range(i):
                product = (product * (st_num % mod)) % mod
                st_num += 1
            tot_sum = (tot_sum + product) % mod
        return tot_sum
