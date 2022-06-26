def solution(citations):
    return max([min(x, i+1) for i, x in enumerate(sorted(citations, reverse=True))])