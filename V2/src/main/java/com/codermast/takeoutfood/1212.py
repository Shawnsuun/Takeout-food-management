def solution(queries, diff):
    numbers = {}
    result = []
    
    for query in queries:
        if query.startswith("+"):
            x = int(query[1:])
            numbers[x] = numbers.get(x, 0) + 1
        elif query.startswith("-"):
            x = int(query[1:])
            if x in numbers:
                numbers[x] -= 1
                if numbers[x] == 0:
                    del numbers[x]
        
        count = 0
        for num in numbers:
            if num + diff in numbers:
                count += numbers[num] * numbers[num + diff]
        result.append(count)
    
    return result


queries = ["+4", "+5", "+2", "-4"]
diff = 1
print(solution(queries, diff))  # [0, 1, 1, 0]


queries = ["+2", "+2", "+4", "+3", "-2"]
diff = 1
print(solution(queries, diff))  # [0, 0, 0, 3, 2]


queries = ["+1", "-1", "+3", "+5", "+2"]
diff = 2
print(solution(queries, diff))  #[0, 0, 0, 1, 1]


queries = ["+10", "+7", "+3", "-7", "-10", "+10"]
diff = 3
print(solution(queries, diff))  #[0, 1, 1, 0, 0, 0]
