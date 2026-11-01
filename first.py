#BUILT A STACK WHICH must contain only 5 items not more than 5
class stack:
    def __init__(self,capacity):
        self.items = []
        self.capacity = capacity

    def push(self,item):
        if len(self.items)< self.capacity:
            self.items.append(item)
        else:
            print("stack full")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("stack empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) ==0
               


s = stack(3)
s.push(10)
s.push(20)
print(s.peek())
print(s.pop())


        