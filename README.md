# The Torchbearer

**Student Name:** Michael Pham
**Student ID:** 132006066
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  A single shortest path run from S is not enough, because the torchbearer must be able to collect all relics during its path. It must find the shortest path to _all_ relics from every relic, which cannot always be considered by just a single shortest path from only the start.

- **What decision remains after all inter-location costs are known:**
  After knowing the fuel cost from the start to all relics, and one relic to another or the end, the remaining decision is to pick the shortest path that collects all relics and reaches the end.

- **Why this requires a search over orders (one sentence):**
  To make this decision, the algorithm would have to search through multiple different possible paths, as multiple shortest paths needed.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source                                                                                                                                                            
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dungeon Start    | There must be a source node for the torchbearer to calculate the optimal path, the initial source node is wherever the torchbearer starts in the dungeon                      |
| Relic Room       | As the torchbearer traverses the dungeon, it stops at relic rooms to collect a relic and then path to the next nearest relic, with the previous relic room as the source node |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property                    | Your answer                                            |
|-----------------------------|--------------------------------------------------------|
| Data structure name         | HashMap/Dictionary                                     |
| What the keys represent     | The keys represent a source node                       |
| What the values represent   | Shortest distance to other nodes from that source node |
| Lookup time complexity      | O(1)                                                   |
| Why O(1) lookup is possible | Key lookup of a HashMap is O(1)                        |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** Dijkstras is needed for how many relics rooms there are, plus the start node.
- **Cost per run:** Let n = |V|, m = |E|, k = |M|. Single shortest-path run costs O(m log n). Each run of Dijkstra's checks for shortest path to every other possible source node. So the cost for each run would go up to m, the number of edges, and log n to alter the priority queue, where n is the amount of nodes or the max possible size of the priority queue.
- **Total complexity:** k(m log n)
- **Justification (one line):** The algorithm calls dijkstras k times, where k is the amount of source nodes in the graph.

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
For every node 'v' in S, dist[v] contains the shortest path length from the start node to node 'v'.
- **For nodes not yet finalized (not in S):**
  For every node 'u' not in S, dust[u] contains the shortest path length from the start node pathing through available nodes in S, to node 'u'.

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
At iteration 0, S will be an empty list, as no shortest paths have been found yet. Nodes not in S, aka every other node will be set to infinity in dist[] asides from the source node which will be 0, so the invariant holds, as these are the shortest possible paths at iteration 0.

- **Maintenance : why finalizing the min-dist node is always correct:**
Finalizing the node that's first in the priority queue, or the min-dist node, is the best option because all edge weights are nonnegative, meaning any alternative path through another unfinished node would only increase the total path cost or not find a shorter route.

- **Termination : what the invariant guarantees when the algorithm ends:**
When the algorithm finishes, every reachable node has been finalized, so dist[v] contains the true shortest-path distance from the source to every reachable vertex in the graph.

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

The Torchbearer's path depends on accurate shortest path distances, because incorrect distances could cause it to choose a nonoptimal relic order or fail to find the minimum fuel route to the exit.

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** A purely greedy solution would only consider the cheapest path to the next possible relic at each stop. However this doesn't consider that each choice will lead to a different possible path, that might be more expensive later on if only the greedy choice is made each time.
- **Counter-example setup:** Let S->B=1, S->C=5, B->C=100, B->T=2, C->B=1, and C->T=1 
- **What greedy picks:** In this graph, greedy would pick ->B first. Then it is forced into picking B->C for 100, as the other option is the exit but all other relics must be picked first. From C, it goes to the exit T. So the total cost is 1+100+1 = 102. The flaw was that the greedy solution wants to pick B first because it's the cheapest, but that leads to a bad path later.
- **What optimal picks:** Optimal would consider the bad options that picking B leads to, so it picks C first. From C, it picks B. From B, it moves to the exit T. The cost is 5+1+2 = 8.
- **Why greedy loses:** Greedy loses because it only considers the current cheapest edge and ignores how that choice affects the remaining route costs needed to collect all relics and reach the exit.

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

The algorithm has to explore all possible relic path orders, and then compare the options instead of trying to pick the greedy solution every time.

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description                                              |
|---|-----------------------|-----------|----------------------------------------------------------|
| Current location | CurrentLocation       | String    | Name of the node                                         |
| Relics already collected | CollectedRelics       | Set       | Holds a set of node names                                |
| Fuel cost so far | TotalSpentFuel        | Integer   | The amount of fuel the torchbearer has spent in its path |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer                                                                          |
|---|--------------------------------------------------------------------------------------|
| Data structure chosen | Set                                                                                  |
| Operation: check if relic already collected | Time complexity: O(1)                                                                |
| Operation: mark a relic as collected | Time complexity:O(1)                                                                 |
| Operation: unmark a relic (backtrack) | Time complexity:O(1)                                                                 |
| Why this structure fits | A set allows for quick lookup and access which we'll need when we check relic status |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** k!, where k is the number of relics in the graph. 
- **Why:** With k relics, theres k! possible paths and orders of collecting the relics. The algorithm might have to search every possible order before finding the minimum cost one.

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** The best complete paths so far are tracked
- **When it is used:** It's used everytime a new path is being calculated, and checks if a currently exploring path is already more expensive than the best completed one so far
- **What it allows the algorithm to skip:** It allows the algorithm to end paths short that are worse than the current best path

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** The current path cost, and collected relics are known 
- **What the lower bound accounts for:** In an unfinished path, the lower bound is the current cost so far. Since to finish the path, you would have to increase the path cost since there's no negative path costs.
- **Why it never overestimates:** The pruning won't overestimate because the path costs are pre-calculated from Dijkstras, which finds the shortest path costs

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

Since the paths between rooms are non-negative, if an unfinished path is already more expensive than a finished one, there is no way for it to beat the currently found best one. The unfinished path must increase its cost to finish the route, which would only make it worse than the currently found best path.

---

## References
- CS 460 Lecture Notes
- https://www.geeksforgeeks.org/dsa/dijkstras-shortest-path-algorithm-greedy-algo-7/  
  Used to help with writing Dijkstra's Algorithm code
