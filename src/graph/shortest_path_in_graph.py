import heapq
import sys


# dijkstra's algorithm

def solution(my_graph) :

    distances = {k: sys.maxsize for k, v in my_graph.items() }
    route = {k: k for k, v in my_graph.items()}

    distances["A"] = 0

    myPq = [(0,"A")]

    while myPq:

        curNodeDist, curNodeName = heapq.heappop(myPq)

        for neighbourKey, neighbourDis in my_graph[curNodeName]:
            nextDistance = distances[curNodeName] + neighbourDis

            if nextDistance < distances[neighbourKey]:
                heapq.heappush(myPq, (nextDistance, neighbourKey))
                distances[neighbourKey] = nextDistance
                route[neighbourKey] = route[curNodeName] + neighbourKey

    print(f"result : {distances}")
    print(f"route : {route}")


if __name__ == "__main__":
    myGraph = {"A" : [("B",1), ("E", 2)], "B" : [("C", 3)], "C": [("D", 5)], "E":[("D", 4)], "D":[("D", 0)]}
    solution(myGraph)

    myGraph2 = {"A" : [("B", 1), ("C", 4)],
                "B" : [("C", 2), ("D", 7)],
                "C" : [("D", 1)],
                "D" : [("D", 0)]}

    solution(myGraph2)




