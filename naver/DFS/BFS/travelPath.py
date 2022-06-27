def remove_edge(tickets, begin, target):
    if len(tickets[begin]) == 1 :
        del tickets[begin]
    else :
        tickets[begin].remove(target)
        
def add_edge(tickets, begin, target):
    if not begin in tickets :
        tickets[begin] = [target]
    else :
        tickets[begin].append(target)

def dfs(begin, tickets):
    # print(begin, tickets)
    if not begin in tickets and tickets: return None
    elif not begin in tickets : return [begin]

    airport = sorted(list(set(tickets[begin])))
    for target in airport:
        # print(begin, target)
        remove_edge(tickets, begin, target)
        res = dfs(target, tickets)
        if res != None :
            res.append(begin)
            return res
        add_edge(tickets, begin, target)
        
    return None

def solution(tickets):
    flight = {}
    for begin, target in tickets:
        add_edge(flight, begin, target)
        
    res = dfs("ICN", flight)
    res.reverse()
    return res