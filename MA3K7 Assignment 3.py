import random

def play_game(numbers_range):
    numbers = list(range(1, numbers_range + 1))
    
    while len(numbers) > 1:
        a, b = random.sample(numbers, 2)
        
        difference = abs(a - b)
        
        numbers.remove(a)
        numbers.remove(b)
        
        numbers.append(difference)
        
    return numbers[0]

final_number = play_game(2024)
print(final_number)