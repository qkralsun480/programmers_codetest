def solution(array, commands):
    answer = []
    total_array=[]
    for i in commands:
        array_list =[]
        for j in range(i[0]-1, i[1]):
            array_list.append(array[j])
        array_list.sort()
        answer.append(array_list[i[2]-1])
    return answer
