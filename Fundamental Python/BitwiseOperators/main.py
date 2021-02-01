""" BITWISE NOT
- If n is positive: ~n = -n-1
- If n is negative: ~n =  n-1

- Example:

int unsigned x = 200;
int x = 100; // --> tham chiếu đến kiểu unsigned 
int x = -100; // Máy tính biểu diễn dưới dạng bù của 2
                                _
Chuyển đổi sang dạng bù của 2:  x + 1

- Example:

short s = -129; // short: 2 bytes
// 129                 : 0000 0000 1000 0001
// F(~129 + 1)(số bù 2): 1111 1111 0111 1110
                                           1
                        ----------------------
                         1111 1111 0111 1111
// Convert from bit sequence to 
// - Unsigned: 2^15+2^14+....+ 0.2^7+ 2^6+...+2^0 = 32639
// - Comple  :-2^15+2^14+....+ 0.2^7+ 2^6+...+2^0 = -129
"""
print(~2)

""" Bitwise XOR
a is the same b --> 0 else 1
          _   _
| a ^ b = ab+ab |

0 ^ 1 = 1
0 ^ 0 = 0
"""
print(bin(6^5))

print(0 | 1)


""" Bitwise Left Shift + Bitwise Right Shift
** Left
2 = 0b 10 

7 = 0b 0111 --> left shift --> 1110

- Performing a left bit shift of 1 is equivalent to multiplication of 2
- Performing a left bit shift of n is equivalent to multiplication of 2**n

** Right
- Vice versa
"""
print(2 << 1)
print(bin(2<<1))

print(3 << 1)

print(2 >> 2)


