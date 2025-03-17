# Roller-Coaster-Lab

Lab Week 7 - Spring 2025 🎢

## Overview
This week, you'll practice implementing and using three fundamental data structures: Stacks, Queues, and Priority Queues. You will create a simplified theme park ride management simulation to better understand how these structures manage data.

**Objectives**

- Implement a Stack (LIFO) to simulate guests using an elevator-style ride (loading and unloading guests).

- Implement a Queue (FIFO) to manage guests waiting in line for a popular roller coaster.

- Implement a Priority Queue to manage guests based on VIP status or Fast Pass holders.

- Demonstrate the practical use of stacks, queues, and priority queues through interactive simulation.

-----------------------------------------------------------

**Part 1: Stack – Elevator Drop Ride Simulation**

Create a class <ins>ElevatorRide</ins>:

-  Use a stack to simulate guests entering an elevator ride.

-  Guests board one at a time and exit in reverse order (the last person in is the first out).

-  Methods required:

    - <ins>board_guest(guest_name)</ins> - adds a guest.

    - <ins>start_ride(capacity)</ins> - simulates the ride, displaying guest names as they exit.
 
-----------------------------------------------------------

**Part 2: Queue – Roller Coaster Ride Simulation**

Create a class <ins>RollerCoasterRide</ins>:

-  Use a queue to manage guests waiting for the roller coaster.

-  Guests enter the queue and exit in the same order they arrived (first in, first out).

-  Methods required:

    - <ins>join_queue(guest_name)</ins> - adds a guest to the line.

    - <ins>start_ride(capacity)</ins> - simulates loading and running the coaster, displaying guest names as they board.

-----------------------------------------------------------

**Part 3: Priority Queue – VIP Guest Management**

Create a class <ins>VIPRide</ins>:

-  Use a priority queue to manage guests based on priority levels (e.g., VIP or Fast Pass holders).

-  Guests with higher priority board the ride before others.

-  Methods required:

    - <ins>add_guest(guest_name, priority)</ins> - adds a guest with their priority (lower number indicates higher priority).

    - <ins>start_ride(capacity)</ins> - simulates the ride, displaying guest names as they board based on priority.

-----------------------------------------------------------

# Rubric

    - Stack and Queue implementation (30%)
    - Priority queue for VIPs (30%)
    - Demo Questions (30%)
    - Code Quality and Style (10%)

-----------------------------------------------------------

# What to submit:
    - Your code as a .py or .ipynb file
    - A screenshot of the output you will have while testing your program
