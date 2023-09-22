import heapq

# 5.getMinCost
def getMinCost(cost, compatible1, compatible2, min_compatible):
    both_clusters = [cost[i] for i in range(len(cost)) if compatible1[i] and compatible2[i]]
    only_c1 = [cost[i] for i in range(len(cost)) if compatible1[i] and not compatible2[i]]
    only_c2 = [cost[i] for i in range(len(cost)) if compatible2[i] and not compatible1[i]]

    heapq.heapify(both_clusters)
    heapq.heapify(only_c1)
    heapq.heapify(only_c2)

    total_cost = 0
    while min_compatible:
        cost_both = both_clusters[0] if both_clusters else float('inf')
        if only_c1 and only_c2 and only_c1[0] + only_c2[0] <= cost_both:
            total_cost += heapq.heappop(only_c1) + heapq.heappop(only_c2)
        else:
            total_cost += heapq.heappop(both_clusters)
        min_compatible -= 1

    if min_compatible and (not only_c1 or not only_c2):
        return -1

    return total_cost

# Test
cost = [2, 4, 6, 5]
compatible1 = [1, 1, 1, 0]
compatible2 = [0, 0, 1, 1]
min_compatible = 2
print(getMinCost(cost, compatible1, compatible2, min_compatible))  # Expected 13

# Test
cost = [4,8,7,3,2,9]
compatible1 = [1, 1, 1, 0,0,1]
compatible2 = [1, 1,0,1,0,0]
min_compatible = 2
print(getMinCost(cost, compatible1, compatible2, min_compatible))  # Expected 12

# Test
cost = [3,4,5,6,3,2,10]
compatible1 = [1, 1, 0,1,1, 1,0]
compatible2 = [0,0,1, 0,1,1,0]
min_compatible = 3
print(getMinCost(cost, compatible1, compatible2, min_compatible))  # Expected 13

# Test
cost = [50,80,100,1,2,3,4]
compatible1 = [1,1,1,1,1,0,0]
compatible2 = [1,1,1,0,0,1,1]
min_compatible = 4
print(getMinCost(cost, compatible1, compatible2, min_compatible))  # Expected 140

# Test
cost = [50,80,100,1,2,3,4]
compatible1 = [1,1,1,1,1,0,0]
compatible2 = [1,1,1,0,0,1,1]
min_compatible = 2
print(getMinCost(cost, compatible1, compatible2, min_compatible))  # Expected 10


# 4.Maximizing Task Priority

def maximumPrioritySum(priority: list[int], x: int, y: int):
    mxHeap = []
    for p in priority:
        if len(mxHeap) < x or mxHeap[0] < p:
            heapq.heappush(mxHeap, p)
        if len(mxHeap) > x:
            heapq.heappop(mxHeap)
    n = len(mxHeap)
    picks = [0] * n
    for i in range(n):
        picks[i] = heapq.heappop(mxHeap)
    return (y // x) * sum(picks) + (sum(picks[-(y % x):]) if y % x else 0)
print(maximumPrioritySum([3, 1, 2], 5, 7))
print(maximumPrioritySum([4,8,7,3,2,9], 5, 7))