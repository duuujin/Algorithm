def solution(k, tangerine):
    answer = 0
    # 정렬
    tangerine.sort()
    
    count = 1
    counts = []
    
    # 크기별 귤 개수 확인
    for i in range(1, len(tangerine)):
        if tangerine[i] == tangerine[i - 1]:
            count += 1
        else:
            counts.append(count)
            count = 1
    
    counts.append(count)
    
    # 귤 개수가 많은 크기부터 순서대로 내림차순 정렬
    counts.sort(reverse=True)
    
    # 귤 골라담기
    total = 0
    for cnt in counts:
        total += cnt
        answer += 1
        if total >= k:
            break
    
    return answer