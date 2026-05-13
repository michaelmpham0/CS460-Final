# Development Log – The Torchbearer

**Student Name:** Michael Pham
**Student ID:** 132006066

---

## Entry 1 – 5/10/2026: Initial Plan

I expected implementing Dijkstra's and the precomputation would be difficult, but not overly difficult. The algorithm is well documented and there's plenty of information and videos about it online. I expect writing the main algorithm that uses Dijkstra's and the computed distances in order to solve the problem would be the hardest part. This part would bring together multiple functions and would be challenging. I expect to go about solving these problems step by step, and printing test results along the way.

---

## Entry 2 – 5/12/2026: Writing README



I finished the README, and it was a good opportunity to think about the problems of implementing the code. I already wrote the code for computing the distances, but next I would have to implement the recursion and logic for actually finding the best route. Like the previous entry, I am expecting this to be the hardest part. The READMe also showed me that this problem will have pruning it. I was planning to solve the order search without pruning, which would have always had O(n!) time complexity to find the shortest order.

---


## Entry 3 – 5/13/2026: Post-Implementation Reflection

When implementing the _explore function, I encountered many bugs. A problem I had was my base case was not being reached properly. My best kept showing as infinity with no relics. This was because for my base case where I updated best, I set the final cost to best[0] + distance to end. But best[0] was intialized to infinity, and I should have used cost_so_far instead. There were many bugs like this where I used the wrong variable or some other minor mistake.

I think to improve this I could probably change how the recursive function explores paths to the remaining relics. Right now it's unsorted, but I think it could be improved if there was a heuristic used instead of just looping through all neighbors.


---

## Final Entry – 5/13/2026: Time Estimate

| Part | Estimated Hours                                                  |
|---|------------------------------------------------------------------|
| Part 1: Problem Analysis | 1 hour                                                           |
| Part 2: Precomputation Design | 2 hours                                                          |
| Part 3: Algorithm Correctness | 45 minutes                                                       |
| Part 4: Search Design | 45 minutes                                                       |
| Part 5: State and Search Space | 1 hour                                                           |
| Part 6: Pruning | 1 hour                                                           |
| Part 7: Implementation | 4 hours (I wrote parts of the code alongside writing the README) |
| README and DEVLOG writing | 3 hours                                                          |
| **Total** | 13 hours 30 minutes                                              |
