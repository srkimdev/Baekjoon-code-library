a, b = map(int, input().split())

a_100 = a // 100
a_10 = (a % 100) // 10 
a_1 = a % 10

b_100 = b // 100
b_10 = (b % 100) // 10  
b_1 = b % 10

new_a = a_1 * 100 + a_10 * 10 + a_100
new_b = b_1 * 100 + b_10 * 10 + b_100

print(max(new_a, new_b))