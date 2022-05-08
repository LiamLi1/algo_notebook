'''
Calculate the total wait time for a customer C to speak to an agent given N agents,
M customers, and T[] time for an agent to serve a customer.
T[i] represents the amount of time it takes for an agent i to serve one customer.
One agent can serve one customer at a time. All N agents can serve concurrently.
The customer chooses the agent with the lowest wait time.

eg:
N = 2
M = 4
T = [4, 5]
First customer chooses agent 1. Second customer chooses agent 2.
Third customer chooses agent 1. Forth customer chooses agent 2.
Customer C will wait 8 minutes.

'''
import heapq
def waitTime(n, m, T):
    h = []
    for t in T:
        heapq.heappush(h, (0, t))

    for i in range(m):
        wait_time, process_time = heapq.heappop(h)
        wait_time += process_time
        heapq.heappush(h, (wait_time, process_time))

    res, process_time = heapq.heappop(h)
    return res

if __name__ == '__main__':
    N = 2
    M = 4
    T = [4, 5]
    print(waitTime(N, M, T))