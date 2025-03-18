import heapq

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

#test for vip ride (priority q)
def main():
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
    print("Ride Queue:", rideED.pQueue)
    print("----------------------------------------\n")
    rideED.start_ride(2) # each roller coaster run only 2 ppl
    print("----------------------------------------\n") #spacer
    print("Ride Queue after Ride Queue #1:", rideED.pQueue)
    rideED.start_ride(4) 
    print("----------------------------------------\n") #spacer
    rideED.start_ride(10) 
    
if __name__ == "__main__":
    main()