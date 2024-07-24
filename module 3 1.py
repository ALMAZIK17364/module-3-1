global calls
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(baseStr = ""):
    newStr = []
    count_calls()


    newStr.append(str(len(baseStr)))
    newStr.append(baseStr.upper())
    newStr.append(baseStr.lower())

    newTuple = tuple(newStr)

    return(newTuple)

def is_contains(needWord = "", wordList = []):
    count_calls()
    for i in wordList:
        if i == needWord:
            return True
            break
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)