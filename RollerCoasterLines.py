#  Stack – Elevator Drop Ride Simulation

class Stack:
  def __init__():

class ElevatorRide:
  '''
  This class uses a stack to simulate guests entering an elevator ride where each guests boards one at a time and exit in reverse order (the last person in is the first out).
  '''

# method board_guest(guest_name)

# method start_ride(capacity)

# ========================================================

# Queue – Roller Coaster Ride Simulation

class DoubleNode:
  def __init__(self, value=None):
    self.value = value
    self.next = None
    self.prev = None

class Queue: 
  """Add in elements to tail, exit queue from head"""
  def __init__(self):
    self.head = None
    self.tail = None
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

  def enqueue(self, val):
    data = DoubleNode(val)
    if self.isEmpty():
        self.head = self.tail = data
    else:
        self.tail.next = data
        data.prev = self.tail
        self.tail = data
    self.size += 1

  def dequeue(self):
    if self.isEmpty():
        return None
    temp = self.head
    self.head = self.head.next
    if self.head is not None:
        self.head.prev = None
    else:
        # if empty
        self.tail = None
    self.size -= 1
    return temp.value
  
  def peek(self):
    if self.isEmpty():
        return None
    return self.head.value
  
  def getLength(self):
    return self.size

class RollerCoasterRide:
  '''
  This class uses a queue to manage guests waiting for the roller coaster where guests enter the queue and exit in the same order they arrived (first in, first out).
  '''

# method join_queue(guest_name)

# method start_ride(capacity)

# ========================================================

# Priority Queue – VIP Guest Management

class VIPRide:
  '''
  This class uses a priority queue to manage guests based on priority levels (e.g., VIP or Fast Pass holders) or where guests with higher priority board the ride before others.
  '''

# method add_guest(guest_name, priority)

# method start_ride(capacity)
