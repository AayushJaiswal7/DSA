class Queue:
    def __init__(self):
        self.val=[]
    
    def push(self,x):
        self.val.append(x)

    def pop(self):
        if len(self.val)==0:
            return -1
        x=self.val[0]
        self.val.pop(0)
        return x

    def front(self):
        if len(self.val)==0:
            return -1
        return self.val[0]

    def isEmpty(self):
        if len(self.val)==0:
            return True
        return False

class MyStack:

    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()
        

    def push(self, x: int) -> None:
        while not self.q1.isEmpty():
            self.q2.push(self.q1.pop())
        self.q1.push(x)
        while not self.q2.isEmpty():
            self.q1.push(self.q2.pop())
        

    def pop(self) -> int:
        return self.q1.pop()
        

    def top(self) -> int:
        if self.q1.isEmpty():
            return -1
        return self.q1.front()
        

    def empty(self) -> bool:
        return self.q1.isEmpty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()