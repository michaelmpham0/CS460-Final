"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Michael Pham
Student ID:   132006066

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq
from queue import PriorityQueue

from pandas.util.version import Infinity


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():

    return ("Why a single shortest-path run from S is not enough: A single shortest path run from S is not enough, because the torchbearer must be able to collect all relics during its path. It must find the shortest path to all relics from every relic, which cannot always be considered by just a single shortest path from only the start."
            "\nWhat decision remains after all inter-location costs are known: After knowing the fuel cost from the start to all relics, and one relic to another or the end, the remaining decision is to pick the shortest path that collects all relics and reaches the end."
            "\nWhy this requires a search over orders (one sentence): To make this decision, the algorithm would have to search through multiple different possible paths, as multiple shortest paths needed.")


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):

    SourceNodes = [spawn]
    for RelicNode in relics:
        if RelicNode not in SourceNodes:
            list.append(SourceNodes, RelicNode)

    return SourceNodes


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """

    PQ = PriorityQueue()

    dist_table = {}

    for node in graph:
        dist_table[node] = float('inf')

    dist_table[source] = 0
    PQ.put((0,source))

    while PQ.qsize() > 0:
        dequeue = PQ.get()
        NewDistance = dequeue[0]
        NewNode = dequeue[1]


        if NewDistance > dist_table[NewNode]:
            continue

        for NeighborNode,NeighborDistance in graph[NewNode]:
            NewTotalDistance = NeighborDistance + NewDistance

            if NewTotalDistance < dist_table[NeighborNode]:
                dist_table[NeighborNode] = NewTotalDistance
                PQ.put((NewTotalDistance,NeighborNode))

    dist_table.pop(source)

    return dist_table


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """

    SourceNodes = select_sources(spawn,relics,exit_node)
    dist_table = {}

    for Node in SourceNodes:
        dist_table[Node] = run_dijkstra(graph,Node)

    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():

    return ("For nodes already finalized (in S): For every node 'v' in S, dist[v] contains the shortest path length from the start node to node 'v'."
"\nFor nodes not yet finalized (not in S): For every node 'u' not in S, dist[u] contains the shortest path length from the start node pathing through available nodes in S, to node 'u'."
"\nInitialization : why the invariant holds before iteration 1: At iteration 0, S will be an empty list, as no shortest paths have been found yet. Nodes not in S, aka every other node will be set to infinity in dist[] asides from the source node which will be 0, so the invariant holds, as these are the shortest possible paths at iteration 0."
"\nMaintenance : why finalizing the min-dist node is always correct: Finalizing the node that's first in the priority queue, or the min-dist node, is the best option because all edge weights are nonnegative, meaning any alternative path through another unfinished node would only increase the total path cost or not find a shorter route."
"\nTermination : what the invariant guarantees when the algorithm ends: When the algorithm finishes, every reachable node has been finalized, so dist[v] contains the true shortest-path distance from the source to every reachable vertex in the graph.")


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    return ("The failure mode: A purely greedy solution would only consider the cheapest path to the next possible relic at each stop. However this doesn't consider that each choice will lead to a different possible path, that might be more expensive later on if only the greedy choice is made each time."
"\nCounter-example setup: Let S->B=1, S->C=5, B->C=100, B->T=2, C->B=1, and C->T=1"
"\nWhat greedy picks: In this graph, greedy would pick ->B first. Then it is forced into picking B->C for 100, as the other option is the exit but all other relics must be picked first. From C, it goes to the exit T. So the total cost is 1+100+1 = 102. The flaw was that the greedy solution wants to pick B first because it's the cheapest, but that leads to a bad path later."
"\nWhat optimal picks: Optimal would consider the bad options that picking B leads to, so it picks C first. From C, it picks B. From B, it moves to the exit T. The cost is 5+1+2 = 8."
"\nWhy greedy loses: Greedy loses because it only considers the current cheapest edge and ignores how that choice affects the remaining route costs needed to collect all relics and reach the exit.")


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """

    best = [float('inf'), []]

    _explore(dist_table,spawn,set(relics),[],0,exit_node,best)
    return (best[0], best[1])


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """

    #base case, finished relic path
    if len(relics_remaining) == 0:
        if exit_node in dist_table[current_loc]:
            FinalCost = cost_so_far + dist_table[current_loc][exit_node]
            if FinalCost < best[0]:
                best[0] = FinalCost
                # copy the list cause the backtracking changes it
                best[1] = relics_visited_order.copy()

        return

    #The pruning is safe because there's no negative paths, so unfinished routes will always increase the cost as it travels towards the exit
    if cost_so_far >= best[0]:
        #prune this path
        return

    RelicsCopy = relics_remaining.copy()

    for NextRelic in RelicsCopy:
        if NextRelic not in dist_table[current_loc]:
            continue

        Distance = dist_table[current_loc][NextRelic]

        #print(current_loc+"->"+NextRelic+" :"+str(Distance))

        cost_so_far += Distance
        relics_remaining.remove(NextRelic)
        relics_visited_order.append(NextRelic)

        _explore(dist_table, NextRelic, relics_remaining, relics_visited_order, cost_so_far, exit_node, best)

        #undo step
        cost_so_far -= Distance
        relics_remaining.add(NextRelic)
        relics_visited_order.pop()



# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """


    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    return find_optimal_route(dist_table, spawn, relics, exit_node)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":

    _run_tests()
