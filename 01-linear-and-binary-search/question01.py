'''
Credit: https://jovian.com/learn/data-structures-and-algorithms-in-python/lesson/lesson-1-binary-search-linked-lists-and-complexity

Question:
Alice has some cards with numbers written on them.
She arranges the cards in decreasing order, and lays them out face down in a sequence
on a table. She challenges Bob to pick out the card containing a given number by
turning over as few cards as possible. Write a function to help Bob locate the card.

Step-by-step solution:
Step 1:
- State the problem: Find position of a given number in a list of numbers arranged in
                decreasing order. Minimize number of times we access elements from the list.
- Input formats:
        cards: a list of numbers sorted in decreasing order
                E.g. [13, 11, 10, 7, 4, 3, 1, 0]
        query: a number, whose position in the array is to be determined
                E.g. 7
                
- Output format:
        position: the position of query in the list cards
                E.g. 3

Step 2: Test cases (Example inputs & outputs)

Step 3: Correct solution in English:
        Linear Search Algorithm - O(n)
    1. Create a variable "position" with valoe 0
    2. Check whether the number at index position in card equals query
    3. If it does, position is the answer and can be returned from the function
    4. If not, increment the value of position by 1 and repeat steps 2 to 5
        till we reach last position
    5. If the number was not found, return -1

Step 4: Implement the solution and test it using example inputs

Step 5: Algorithm's complexity and identify inefficiencies (if any)
Step 6: Apply the right technique to overcome inefficiency. Repeat step 3-5.
        Binary Search Algorithm - O(logn)
    1. Find the middle element of the list
    2. If it matches queried number, return the middle position as the answer
    3. If it is less than the queried number, then search the first half of the list
    4. more, second half
    5. If no more elements remain, return -1
'''


######### Test case sample 00
test = {
    'input' : {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query' : 7
    },
    'output' : 3
}
# Create a list for storing test cases
tests = [] 
tests.append(test)
# Test case 01: query occurs somewhere in the middle of the list cards
tests.append ( {
    'input' : {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query' : 1
    },
    'output' : 6
} )
# Test case 02: query is the first element in cards
tests.append ( {
    'input' : {
        'cards': [4, 2, 1, -1],
        'query' : 4
    },
    'output' : 0
} )
# Test case 03: query is the last element in cards
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})
# Test case 04: cards contains just 1 element, which is query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})
# Test case 05: cards does not contain query, ASSUME funtion will return -1
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})
# Test case 06: cards is empty, function will return -1
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})
# Test case 07: cards contains repeating numbers
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})
# Test case 08: query occurs at more than 1 position in cards.
#               ASSUME function will return the first occurrence of query
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})
# Test case 09: query occurs at more than 1 position in cards
#               also query is the first element in the list
#               ASSUME function will return the first occurrence of query
tests.append({
    'input': {
        'cards': [6, 6, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 0
})
# Test case 10: the size of the list cards is now really big
#               Use this to compare the execution time between
#                   linear search and binary search
'''
tests.append({
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998
})
'''



'''
Step 3: Correct solution in English:
        Linear Search Algorithm - O(n)
    1. Create a variable "position" with value 0
    2. Check whether the number at index position in card equals query
    3. If it does, position is the answer and can be returned from the function
    4. If not, increment the value of position by 1 and REPEAT steps 2 to 5
        till we reach last position
    5. If the number was not found, return -1
'''
######### Linear Search Algorithm function
def locate_card_linear_search(cards, query):
    # Create a variable "position" with value 0
    position = 0
    
    # print('cards:',cards)
    # print('query:',query)

    # Set up a loop for repitition
    while position < len(cards):
        # print('position',position)
        
        # Check whether the number at index position in card equals query
        if cards[position] == query:
            # Answer found! Return and exit...
            return position
            
        # Increment position
        position += 1
        
    return -1



'''
Step 6: Apply the right technique to overcome inefficiency. Repeat step 3-5.
        Binary Search Algorithm - O(logn)
        Binary search runs in logarithmic time
    1. Find the middle element of the list
    2. If it matches queried number, return the middle position as the answer
    3. If it is less than the queried number, then search the first half of the list
    4. more, second half
    5. If no more elements remain, return -1
'''
######### Binary Search Algorithm function _ Option 01 (my idea)
def locate_card_binary_search_01(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        # // Operator (Floor Division)
        print("lo:",lo,", hi:",hi)
        mid = (lo + hi) // 2
        mid_number = cards[mid]

        if mid_number == query:
            print(mid)
            if mid > 0 and cards[mid-1] == query:
                hi = mid - 1
            else:
                return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1
    return -1
    
    
#####   Binary Search Algorithm function _ Option 02 (jovian notebook)
def test_location(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'
    
def locate_card_binary_search_02(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid -1
        elif result == 'right':
            lo = mid + 1
    return -1
    

#####   Binary Search Algorithm function _ Option 03 (jovian notebook)
def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1
    
def locate_card_binary_search_03(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] > query:
            return 'right'
        else:
            return 'left'
        
    return binary_search(0,len(cards)-1,condition)



######### Test my function

# 1. Just print all the test cases as a dictionary
# print(tests)

# 2. Print each test case and result of each using Python dictionary
# '''
caseNumber = 0
for key in tests:
    print(f"Test case {caseNumber}: {key}")
    result = locate_card_binary_search_03(**key['input']) == key['output']
    print(f" {result}")    
    caseNumber += 1
# '''
    
# 3. Print the sample result of test case 00, 2 lines below are the same
'''
result = locate_card_linear_search(**test['input']) == test['output']
result = locate_card(test['input']['cards'], test['input']['query']) == test['output']
print(result)
'''

# 4. Print a test case of yourChoice and its result
'''
yourChoice = 8
print(tests[yourChoice])
cardsYourChoice = tests[yourChoice]['input']['cards']
queryYourChoice = tests[yourChoice]['input']['query']
print(f"The position of the query that function returns: {locate_card_binary_search(cardsYourChoice, queryYourChoice)}")
'''