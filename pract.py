# def contains_duplicates(numbers):
#     seen = set()    
#     for number in numbers:
#         if number not in seen:
#             seen.add(number)
#         else:
#             return True
#     return False
            
# print(contains_duplicates([1, 2, 3, 1]))
# print(contains_duplicates([1, 2, 3, 4]))




# def target_no(numbers):
#     for number in numbers:
#         result = number + number =+ 1
#         if result != 9:
#             return False

# def two_sum(numbers, target):
    
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             if numbers[i] + numbers[j] == target:
#                 return [i, j]



def two_sum(numbers, target):
    seen = {}
    
    for i, number in enumerate(numbers):
        need = target - number
        if need in seen:
            return [i, seen[need]]
        else: 
            seen[number] = i
        

print(two_sum([2, 7, 11, 15], 9))