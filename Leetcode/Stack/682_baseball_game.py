class Stack:
    def __init__(self):
        self.val=[]
    def push(self,x):
        self.val.append(x)
    def pop(self):
        if len(self.val)==0:
            return -1
        x=self.val[-1]
        self.val.pop()
        return x
    def isEmpty(self):
        if len(self.val)==0:
            return True
        return False
    def top(self):
        if len(self.val)==0:
            return -1
        return self.val[-1]


class Solution:
    def calPoints(self, operations: list[str]) -> int:
        self.score=Stack()
        for op in operations:
            if op=="C":
                self.score.pop()
            elif op=="D":
                prev_score=self.score.top()
                self.score.push(2*prev_score)
            elif op=="+":
                last_score=self.score.pop()
                sum_score=last_score+self.score.top()
                self.score.push(last_score)
                self.score.push(sum_score)
            else:
                self.score.push(int(op))
        return sum(self.score.val)
        