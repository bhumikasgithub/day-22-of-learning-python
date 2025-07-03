#1
def next_in_line(lst, num):
    if len(lst) == 0:
        return "No list has been selected"
    lst.append(num)         # Step 1: Add new number to the end
    lst.pop(0)              # Step 2: Remove the first element
    return lst              # Step 3: Return the updated list
print(next_in_line([5, 6, 7, 8, 9], 1))
# Output: [1, 6, 7, 8, 9]

print(next_in_line([7, 6, 3, 23, 17], 10))
# Output: [10, 6, 3, 23, 17]

print(next_in_line([], 6))
# Output: "No list has been selected"

#2
def get_budgets(lst):
    total = 0
    for person in lst:
        total += person['budget']
    return total
print(get_budgets([
  { "name": "John",  "age": 21, "budget": 23000 },
  { "name": "Steve", "age": 32, "budget": 40000 },
  { "name": "Martin","age": 16, "budget": 2700 }
]))

#3
def alphabet_soup(txt):
    sorted_letters = sorted(txt)
    result = ''.join(sorted_letters)
    return result
print(alphabet_soup("hello"))       # Output: "ehllo"
print(alphabet_soup("edabit"))      # Output: "abdeit"
print(alphabet_soup("hacker"))      # Output: "acehkr"
print(alphabet_soup("geek"))        # Output: "eegk"
print(alphabet_soup("javascript"))  # Output: "aacijprstv"

#4
def compound_interest(p, t, r, n):
    
    amount = p * (1 + r / n) ** (n * t)
    
    return round(amount, 2)

print(compound_interest(10000, 10, 0.06, 12))  

#5
def return_only_integer(lst):
    result = []
    for item in lst:
        if type(item) == int:
            result.append(item)
    return result
print(return_only_integer([9, 2, "space", "car", "lion", 16]))
# Output: [9, 2, 16]

print(return_only_integer(["hello", 81, "basketball", 123, "fox"]))
# Output: [81, 123]

print(return_only_integer([10, "121", 56, 20, "car", 3, "lion"]))
# Output: [10, 56, 20, 3]

print(return_only_integer(["String",  True,  3.3,  1]))
# Output: [1]



