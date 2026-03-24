Power Grid Failure Analyzer (DFS-Based)

Overview

The Power Grid Failure Analyzer is a terminal-based application that simulates cascading failures in a power network using Depth First Search (DFS). It models the grid as a graph of interconnected stations and analyzes how a failure at one station can propagate through the system.


---

Problem Statement

Power grids are highly interconnected systems where a failure in one station can affect multiple connected stations. This can lead to cascading failures and large-scale outages. The problem is to efficiently analyze how such failures spread and identify critical points in the network.


---

Concepts Used

Graph Representation

Nodes represent power stations

Edges represent connections


Depth First Search (DFS)

Used to traverse the network

Simulates failure propagation




---

Features

Display the current power grid

Simulate failure of any station

Identify all affected stations

Calculate total impact size

Detect critical stations based on impact

Add connections dynamically



---

How It Works

The power grid is represented as a graph using a dictionary. When a station fails, DFS is applied to traverse all connected nodes and mark them as affected. The system also evaluates each station to determine its impact and identify critical nodes.


---

Usage

Run the program:

python grid.py

Menu options:

Show Grid

Simulate Failure

Find Critical Stations

Add Connection

Exit



---

Example

Input:

Simulate Failure → A

Output:

Affected Stations:
A → B → C → D → E → F

Total affected: 6


---

Applications

Power grid analysis

Infrastructure risk assessment

Network reliability evaluation

Failure propagation studies



---

Limitations

Does not consider real electrical parameters

Assumes all connections are equal

DFS does not guarantee optimal paths



---

Future Improvements

Add weighted connections

Simulate multiple failures

Visualize the network

Compare with BFS

---

Conclusion

This project demonstrates how Depth First Search can be used to analyze failure propagation in interconnected systems. It highlights the practical application of graph traversal in solving real-world infrastructure problems.
