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

- **Number of Dijkstra runs:** Dijkstras is needed for how many relics rooms there are, plus the start node
- **Cost per run:** Let n = |V|, m = |E|, k = |M|. Single shortest-path run costs O(m log n). Each run of Dijkstra's checks for shortest path to every other possible source node. So the cost for each run would go up to m, the number of edges, and log n to alter the priority queue, where n is the amount of nodes or the max possible size of the priority queue
- **Total complexity:** k(m log n)
- **Justification (one line):** The algorithm calls dijkstras k times, where k is the amount of source nodes in the graph

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _Your answer here._

- **For nodes not yet finalized (not in S):**
  _Your answer here._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _Your answer here._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Your answer here._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _Your answer here._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_Your answer here._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References
- CS 460 Lecture Notes
- https://www.geeksforgeeks.org/dsa/dijkstras-shortest-path-algorithm-greedy-algo-7/  
  Used to help with writing Dijkstra's Algorithm code
