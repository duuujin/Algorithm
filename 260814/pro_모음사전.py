def solution(word):
    moeum = ['A', 'E', 'I', 'O', 'U' ]
    lst = []
    
    def dfs(current):
        if current != "":
            lst.append(current)
        
        if len(current) == 5: 
            return
        
        for mo in moeum:
            dfs(current + mo)
            
    dfs("")
    
    return lst.index(word) + 1