class stack:
  def __init__(self):
    self.items=[]
  def push(self,data):
    self.items.append(data)
  def pop(self):
    del(self.items[len(self.items)-1])
  def display(self):
    print(self.items)
s=stack()
s.push(20)
s.push(30)
s.push(40)
s.push(10)
s.display()
s.pop()
s.pop()
s.display()
