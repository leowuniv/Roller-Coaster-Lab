'''
Welcome to our amusment park with a variety of rides! 
'''

# Rides - Elevator Drop, Roller Coaster; Addition: VIP Guest Management

import heapq

# ========================================================

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
      self.size -= 1
      return val
        
  def push(self, val):
    aNode = Node(val)
    aNode.next, self.head = self.head, aNode
    self.size += 1

class ElevatorRide:
  '''
  This class uses a stack to simulate guests entering an elevator ride where each guests boards one at a time and exit in reverse order (the last person in is the first out).
  '''
  def __init__(self):
    self.stack = Stack()

# method board_guest(guest_name)
  def board_guest(self, guest_name): # add guest to elevator
    self.stack.push(guest_name)
    print(f"{guest_name} has boarded the elevator ride.") #board one at a time

# method start_ride(capacity)
  def start_ride(self, capacity): # simulates ride
    if self.stack.isEmpty(): # check if stack is empty, no one in line to enter ride
      print("The ride cannot be started since there is no one to board the ride.")
      return

    print("Ride preparing to start...")
    print("-------------------------------")
    print("Ride in action!!!")
    print("-------------------------------")
    print("Ride completed.")
    print("List of guests exiting the ride:")
    print("===============================")
    for i in range(min(capacity, self.stack.size)):
      guest = self.stack.pop()
      print(f"{guest} has exited the elevator ride.") # display guest names as they exit (in reverse order)

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
  def __init__(self):
    self.queue = Queue()

  # method join_queue(guest_name)

  def join_queue(self, guest_name): # add guest to the line
    self.queue.enqueue(guest_name)
    print(f"{guest_name} has joined the line.")

  # method start_ride(capacity)

  def start_ride(self, capacity): # simulates loading and running the coaster
    if self.queue.isEmpty():
      print("There is no one in queue for the ride to start.")
      return
     
    print("Preparing to start the rollar coaster ride...") # simulate loading
    print("=============================================")
    print("All riders, please board the ride!")
    print("=============================================")
    for i in range(min(capacity, self.queue.getLength())):
      guest = self.queue.dequeue()
      print(f"{guest} has boarded the ride.")
    print("=============================================")
    print("The coaster is now activated with all riders on board! \nPlease wait until the next ride if you are waiting.")

# ========================================================

# Priority Queue – VIP Guest Management

class PriorityQueue:
  def __init__(self):
    self.heap = []

  def __repr__(self):
    return str(self.heap)

  def isEmpty(self) -> bool:
    return len(self.heap) == 0
    
  def enqueue(self, priority: int, value) -> None:
    heapq.heappush(self.heap, (priority, value)) 

  def dequeue(self):
    if self.heap:
      return heapq.heappop(self.heap)[1] # index for value
    
  def getLength(self) -> int:
    return len(self.heap)

class VIPRide:
  '''
  This class uses a priority queue to manage guests based on priority levels (e.g., VIP or Fast Pass holders) or where guests with higher priority board the ride before others.
  '''
  def __init__(self):
    self.pQueue = PriorityQueue()

  # method add_guest(guest_name, priority)

  def add_guest(self, guest_name, priority=10): # adds guest with their priority, min heap
    self.pQueue.enqueue(priority,guest_name)
    print(f"{guest_name} has joined the line.")

  # method start_ride(capacity)

  def start_ride(self, capacity): # simulates ride, board based on priority 
    if self.pQueue.isEmpty():
      print("There is no one in queue for the ride to start.")
      return
     
    print("Preparing to start the rollar coaster ride...") # simulate loading
    print("=============================================")
    print("All riders, please board the ride!")
    print("=============================================")
    for i in range(min(capacity, self.pQueue.getLength())):
      guest = self.pQueue.dequeue()
      print(f"{guest} has boarded the ride.")
    print("=============================================")
    print("The coaster is now activated with all riders on board! \nPlease wait until the next ride if you are waiting.")

# ========================================================

# roller coaster test
def main1():
    #test for no people in ride
    rideRC = RollerCoasterRide()
    print("Ride Queue:", rideRC.queue)
    rideRC.start_ride(0)
    print("----------------------------------------\n")
    #test for people joining the ride
    print("Ride Queue #1:", rideRC.queue)
    rideRC.join_queue("test1")
    rideRC.join_queue("test2")
    rideRC.join_queue("test3")
    rideRC.join_queue("test4")
    print("Ride Queue:", rideRC.queue)
    print("----------------------------------------\n")
    rideRC.start_ride(2) # each roller coaster run only 2 ppl
    print("----------------------------------------\n") #spacer
    print("Ride Queue after Ride Queue #1:", rideRC.queue)
    rideRC.start_ride(4) 
    print("----------------------------------------\n") #spacer
    rideRC.start_ride(10) 

# test for elevator ride
def main2():
    #test for no people in ride
    rideED = ElevatorRide()
    print(rideED.stack)
    rideED.start_ride(0)
    print("===============================\n")
    # test boarding guests ; last person in should be first person out
    rideED.board_guest("test1")
    rideED.board_guest("test2")
    rideED.board_guest("test3")
    rideED.board_guest("test4") 
    rideED.board_guest("test5") 
    rideED.board_guest("test6") 
    rideED.board_guest("test7") 
    rideED.board_guest("test8") 
    rideED.board_guest("test9") 
    rideED.board_guest("test10") # last person to board
    print("Stack:", rideED.stack)
    print("===============================\n")
    # testing ride start
    rideED.start_ride(10)
    print("Stack:", rideED.stack)
    print("===============================\n")
    # test to start ride again (no one left)
    rideED.start_ride(10)
    print("===============================\n")

# test for vip ride (priority q)
def main3():
    #test for no people in ride
    rideED = VIPRide()
    print("Ride Queue:", rideED.pQueue)
    rideED.start_ride(0)
    print("----------------------------------------\n")
    #test for people joining the ride
    print("Ride Queue #1:", rideED.pQueue)
    rideED.add_guest("test1", 4)
    rideED.add_guest("test2", 3)
    rideED.add_guest("test3", 2)
    rideED.add_guest("test4", 1)
    rideED.add_guest("test5", 5)
    print("Ride Queue:", rideED.pQueue)
    print("----------------------------------------\n")
    rideED.start_ride(2) # each roller coaster run only 2 ppl
    print("----------------------------------------\n") #spacer
    print("Ride Queue after Ride Queue #1:", rideED.pQueue)
    rideED.start_ride(4) 
    print("----------------------------------------\n") #spacer
    rideED.start_ride(10) 
    
if __name__ == "__main__":
    main1() # roller coaster ride
    main2() # elevator ride
    main3() # vip ride

# Can do custom inputs if needed more advanced in the future
