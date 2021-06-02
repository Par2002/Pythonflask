# Print following a pattern without using any loop. (Hint use recursive functions)

# Examples : 

# Input: n = 16
# Output: 16, 11, 6, 1, -4, 1, 6, 11, 16

# Input: n = 10
# Output: 10, 5, 0, 5, 10

def stack(num):
    
    if num<=0:
        print(num)
    
        return

    else:
        print(num)
        stack(num-5)
        print(num)
        return

stack(16)
stack(10)

# _________________________________________

