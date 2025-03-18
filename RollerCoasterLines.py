#  Stack – Elevator Drop Ride Simulation

class Node:
  def __init__(self, value=None, next=None):
    self.next = None
    self.value = value

class Stack:
  def __init__(self):
    self.head = None
    self.size = 0

  def __repr__(self):
    output = ""
    nextNode = self.head
    while nextNode is not None:
      output += f"{nextNode.value} -> "
      nextNode = nextNode.next
    output += "None"
    return output

  def isEmpty(self):
    return self.head is None
    
  def peek(self):
    if not self.isEmpty():
      return self.head.value
        
  def pop(self):
    if not self.isEmpty():
      val, self.head = self.head.value, self.head.next
      return val
        
  def push(self, val):
    aNode = Node(val)
    aNode.next, self.head = self.head, aNode

class ElevatorRide:
  '''
  This class uses a stack to simulate guests entering an elevator ride where each guests boards one at a time and exit in reverse order (the last person in is the first out).
  '''
  def __init__(self):
    self.stack = Stack()

# method board_guest(guest_name)
  def board_guest(self, guest_name): # add guest to elevator

# method start_ride(capacity)
  def start_ride(self, capacity): # simulates ride
    print("List of guests exiting the ride")
    print("===============================")

# ========================================================

#test for elevator ride
def main():
    #test for no people in ride
    rideED = ElevatorRide()
    
    
if __name__ == "__main__":
    main()