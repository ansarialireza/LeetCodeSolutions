class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        bill_5 = 0
        bill_10 = 0
        for i in range(0,len(bills)):
            if( bills[i] == 5 ):
                bill_5 += 1               
            elif(bills[i] == 10):
                bill_10 += 1
                if bill_5 != 0 :
                    print(i)
                    bill_5 -= 1
                else :
                    return False
                
            else:
                if ( bill_10 !=0 and bill_5 !=0):
                    bill_10 -=1
                    bill_5 -=1
                elif (bill_5 >= 3):
                    bill_5 -=3
                else:
                    return False
        return True