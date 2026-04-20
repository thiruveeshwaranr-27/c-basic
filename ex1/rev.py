class Solution:
    def reverse(self, x: int) -> int:
        # Step 1: Sign handle pannu
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        res = 0
        while x != 0:
            # Step 2: Kadaisi digit edu (e.g., 123 -> 3)
            digit = x % 10
            # Step 3: Result-ah build pannu
            res = (res * 10) + digit
            x //= 10 # Number-ah koraichi kitte po
            
        # Step 4: 32-bit range check
        if res > 2**31 - 1:
            return 0
            
        return res * sign
