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
    print("The coaster is now activated with all riders on board! \n Please wait until the next ride if you are waiting.")

# ========================================================

