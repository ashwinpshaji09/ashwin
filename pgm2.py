stones = [200,121,87,54,65]
print(stones)
while len(stones) > 1:
    stones.sort()
    if stones[-1] == stones[-2]:
        stones.pop(-1)
        stones.pop(-1)
    else:
        stones[-1]-=stones[-2]
        stones.pop(-2)
if not stones:
    print(0)        
else:
    print(stones[0])
    
    
    
'''
    Test case 1:
    
        input :[3,4,6,8,2,3]
        
        output :0
        
    Test case 2: 
    
        input :[15,54,87,65]
        
        output :17
        
    Test case 3:
    
        input :[200,121,87,54,65]
        
        output :3
'''
