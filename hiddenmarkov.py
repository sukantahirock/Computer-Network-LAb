import numpy as np

# Define the states (weather) and observations (activities)
states = ['Rainy', 'Cloudy', 'Sunny']
observations = ['Walk', 'Shop', 'Clean']

# Define the initial state probabilities
initial_probabilities = {'Rainy': 0.4, 'Cloudy': 0.3, 'Sunny': 0.3}

# Define the transition probabilities
transition_probabilities = {
    'Rainy': {'Rainy': 0.6, 'Cloudy': 0.3, 'Sunny': 0.1},
    'Cloudy': {'Rainy': 0.4, 'Cloudy': 0.4, 'Sunny': 0.2},
    'Sunny': {'Rainy': 0.2, 'Cloudy': 0.4, 'Sunny': 0.4}
}

# Define the emission probabilities
emission_probabilities = {
    'Rainy': {'Walk': 0.1, 'Shop': 0.4, 'Clean': 0.5},
    'Cloudy': {'Walk': 0.6, 'Shop': 0.3, 'Clean': 0.1},
    'Sunny': {'Walk': 0.2, 'Shop': 0.4, 'Clean': 0.4}
}

def viterbi(observation_sequence):
    n = len(observation_sequence)
    m = len(states)

    # Initialize the Viterbi matrix and backpointer matrix
    viterbi_matrix = np.zeros((m, n))
    backpointer_matrix = np.zeros((m, n), dtype=int)

    # Initialize the first column of the Viterbi matrix using initial probabilities
    for i, state in enumerate(states):
        viterbi_matrix[i, 0] = initial_probabilities[state] * emission_probabilities[state][observation_sequence[0]]
    
    # Fill in the Viterbi matrix
    for t in range(1, n):
        for i, state in enumerate(states):
            probabilities = [viterbi_matrix[j, t - 1] * transition_probabilities[prev_state][state] *
                             emission_probabilities[state][observation_sequence[t]] for j, prev_state in enumerate(states)]
            viterbi_matrix[i, t] = max(probabilities)
            backpointer_matrix[i, t] = np.argmax(probabilities)
    
    # Find the best path
    best_path = [0] * n
    best_path[n - 1] = np.argmax(viterbi_matrix[:, n - 1])
    for t in range(n - 2, -1, -1):
        best_path[t] = backpointer_matrix[best_path[t + 1], t + 1]

    return [states[state_index] for state_index in best_path]

# Example observation sequence
observation_sequence = ['Walk', 'Shop', 'Clean']

# Find the most likely weather sequence
result = viterbi(observation_sequence)
print("Most likely weather sequence:", result)
