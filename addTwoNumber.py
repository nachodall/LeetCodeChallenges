# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNumber(node1: Optional[ListNode]) -> int:
            listOfNumbers = []
            currentNode = node1

            while currentNode != None:
                listOfNumbers.append(currentNode.val)
                currentNode = currentNode.next

            number = 0

            for i in range(len(listOfNumbers)-1,-1,-1):
                digit = listOfNumbers[i]
                number = number * 10 + digit
            
            return number
        
        def createLinkedList(resultado: int) -> [ListNode]:
            listOfNumbers = []
            linkedList = ListNode(resultado % 10)

            while resultado > 0:
                listOfNumbers.append(resultado % 10)
                resultado = resultado // 10

            current = linkedList

            for value in listOfNumbers[1:]:
                current.next = ListNode(value)
                current = current.next

            return linkedList

        resultado = getNumber(l1) + getNumber(l2)

        return createLinkedList(resultado)
