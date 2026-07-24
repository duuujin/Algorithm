import heapq
def solution(book_time):
    times = []
    
    for book in book_time:
        start = book[0]
        end = book[1]
        
        sh, sm = map(int, start.split(":"))
        eh, em = map(int, end.split(":"))

        start_min = sh * 60 + sm
        end_min = eh * 60 + em + 10    
        times.append([start_min, end_min])

    times.sort()
    heap = []
    
    for start, end in times:
        if heap and start >= heap[0]:
            heapq.heappop(heap)
        
        heapq.heappush(heap, end)
    
    
    
    return len(heap)