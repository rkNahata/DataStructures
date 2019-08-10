
class SNode():

    #constructor
    def __init__(self):
        self.data = None
        self.next = None

    #method to set data
    def setData(self,data):
        self.data = data

    #method to get data field fof a node
    def getData(self):
        return self.data

    #method to get next node
    def getNext(self):
        return self.next

    #method to set next node
    def setNext(self,next):
        self.next=next
    #has next
    def hasNext(self):
        return self.next!=None


class SinglyLinkedList():

    def __init__(self):

        self.head = None

    def insert(self,data):
        new_node = SNode()
        new_node.data = data
        new_node.next=None
        self.head = new_node

    def Size(self):
        current = self.head
        count = 0
        while current:
            current = current.getNext()
            count+=1
        return count

    #Search return node having data else error is returned
    def Search(self,data):
        current = self.head
        found = False
        while current and found is False:
            if current.getData()==data:
                found = True
            else:
                current=current.getNext()
        if found is False:
            raise ValueError("data not found in the list")
        return current

    def Delete(self,data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
                previous = current
            current = current.getNext()
        if not found:
            raise ValueError("data not found in the list")
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())







