import itertools

def calculate_probability(actual_directions, remembered_directions):
    # Find the number of '?' characters in the remembered_directions string
    num_question_marks = remembered_directions.count('?')
    
    # Generate all possible combinations of coin toss outcomes for the '?' characters
    coin_tosses = itertools.product(['+', '-'], repeat=num_question_marks)
    
    # Keep track of the number of outcomes that result in Kefa ending up in the correct position
    correct_outcomes = 0
    
    for coin_toss_result in coin_tosses:
        # Create a new string by replacing '?' characters with the corresponding coin toss result
        trial_directions = remembered_directions.replace('?', '{}').format(*coin_toss_result)
        
        # Check if Kefa ends up in the correct position after following the actual and trial directions
        if get_final_position(actual_directions) == get_final_position(trial_directions):
            correct_outcomes += 1
    
    # Return the probability of ending up in the correct position
    return correct_outcomes / (2**num_question_marks)

def get_final_position(directions):
    # Calculate Kefa's final position after following the given directions
    return directions.count('+') - directions.count('-')

# Read the input strings
actual_directions = input().strip()
remembered_directions = input().strip()

# Calculate and print the probability of Kefa ending up in the correct position
print('{:.6f}'.format(calculate_probability(actual_directions, remembered_directions)))
