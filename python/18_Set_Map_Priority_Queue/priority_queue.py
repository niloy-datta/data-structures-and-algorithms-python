import heapq

def main():
    # priority_queue<int,vector<int>,greater<int>> pq;
    pq = []
    heapq.heappush(pq, 10)
    heapq.heappush(pq, 5)
    heapq.heappush(pq, 30)
    print(pq[0])
    heapq.heappush(pq, 2)
    print(pq[0])
    heapq.heappop(pq)  # 2
    heapq.heappop(pq)  # 5
    print(pq[0])

if __name__ == "__main__":
    main()
