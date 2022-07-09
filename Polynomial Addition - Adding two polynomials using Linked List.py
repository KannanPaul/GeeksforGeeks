'''Given two polynomial numbers represented by a linked list. 
The task is to complete the function addPolynomial() that adds these lists meaning adds the coefficients who have the same variable powers.

Note:  Given polynomials are sorted in decreasing order of power.

Example 1:

Input:
LinkedList1:  (1,x2) 
LinkedList2:  (1,x3)
Output:
1x^3 + 1x^2
Explanation: Since, x2 and x3 both have
different powers as 2 and 3. So, their
coefficient can't be added up.

Example 2:

Input:
LinkedList1:  (1,x3) -> (2,x2)
LinkedList2:  (3,x3) -> (4,x2)
Output:
4x^3 + 6x^2
Explanation: Since, x3 has two different
coefficients as 3 and 1. Adding them up
will lead to 4x3. Also, x2 has two
coefficients as 4 and 2. So, adding them
up will give 6x2.

Your Task:
The task is to complete the function addPolynomial() which should add the polynomial with same powers 
return the required polynomial in decreasing order of the power in the form of a linked list.'''

Solution:
  Time Complexity: O(N+M)
  Auxiliary Space: O(1)
  
 '''
 class node:
    def __init__(self, coeff, pwr):
        self.coef = coeff
        self.next = None
        self.power = pwr
'''

class Solution:
    # return a linked list denoting the sum with decreasing value of power
    def addPolynomial(self, poly1, poly2):
        # Code here
        newHead= node(0,0)
        c=newHead
        while poly1 != None or poly2 !=None :
            if poly1 == None:
                c.next=poly2
                break
            elif poly2 == None:
                c.next=poly1
                break
            elif poly1.power == poly2.power:
                c.next=node(poly1.coef+poly2.coef,poly1.power)
                poly1=poly1.next
                poly2=poly2.next
            elif poly1.power >= poly2.power:
                c.next=node(poly1.coef,poly1.power)
                poly1=poly1.next
            elif poly1.power <= poly2.power:
                c.next=node(poly2.coef,poly2.power)
                poly2=poly2.next 
            c=c.next
        return newHead.next
        

        
'''
solution link -https://www.geeksforgeeks.org/adding-two-polynomials-using-linked-list/
'''
