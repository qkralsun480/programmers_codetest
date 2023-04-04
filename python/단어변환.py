from collections import deque
def solution(begin, target, words):
    answer = 0
    
    q = deque()
    q.append([begin, answer])
    while q:
        a, b = q.popleft()
        print(a)
        if target == a:
            answer = b
        for text in words:
            count =0
            for i in range(len(a)):
                if text[i] != a[i]:
                    count+=1
            if count == 1:
                words.remove(text)
                q.append([text,b+1])
    return answer
