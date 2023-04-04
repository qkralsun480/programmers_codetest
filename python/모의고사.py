from collections import Counter
def solution(answers):
    answer = []
    test_case = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    test_temp =[]
    for j in range(0,3):
        count=0
        for i, temp in enumerate(answers):
            if temp == test_case[j][i%len(test_case[j])]:
                count +=1
        test_temp.append(count) 
    for idx, num in enumerate(test_temp):
        if num == max(test_temp) :
            answer.append(idx +1)

    return answer
