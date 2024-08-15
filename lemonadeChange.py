class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        bill_5 = 0
        bill_10 = 0
        flag=0
        for i in range(0,len(bills)):
            if( bills[i] == 5 ):
                bill_5 += 1
                flag +=1
               
            elif(bills[i] == 10):
                bill_10 += 1
                if bill_5 != 0 :
                    bill_5 -= 1
                    flag +=1
                
            elif ( bills[i] == 20):
                if ( bill_10 !=0 and bill_5 !=0):
                    bill_10 -=1
                    bill_5 -=1
                    flag +=1
                elif (bill_5 >= 3):
                    bill_5 -=3
                    flag +=1
        if len(bills) == flag :
            return True
        else : 
            return False
        
               
# # bills = [5,5,5,10,20]  
# # bills = [5,5,10,10,20]  
# # bills = [5,5,5,10,5,5,10,20,20,20]
# bills = [5,5,5,5,10,5,10,10,10,20]
 
# obj = Solution()
# res=obj.lemonadeChange(bills)

# print(res)