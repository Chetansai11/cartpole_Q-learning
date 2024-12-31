import gymnasium as gym
import numpy as np
import time
import pickle

# Load the environment
env = gym.make('CartPole-v1', render_mode='human')

# Load the trained Q-table
with open(r'c:\Users\asus\Desktop\MS\RL\cartpole Q-learning\q_table.pkl', 'rb') as f:
    q_table = pickle.load(f)

# Observation discretization settings
Observation = [30, 30, 50, 50]
np_array_win_size = np.array([0.25, 0.25, 0.01, 0.1])



def get_discrete_state(state):
    discrete_state = state/np_array_win_size+ np.array([15,10,1,10])
    return tuple(discrete_state.astype(int))


EPISODES = 5  # Number of episodes to run for testing
for episode in range(EPISODES):
    state, _ = env.reset()  # Reset the environment
    discrete_state = get_discrete_state(state)
    done = False
    episode_reward = 0

    print(f"Starting episode {episode + 1}")

    while not done:
        # Choose the best action based on the Q-table
        action = np.argmax(q_table[discrete_state])

        # Step the environment
        new_state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        episode_reward += reward

        # Update the state
        new_discrete_state = get_discrete_state(new_state)
        discrete_state = new_discrete_state

        # Sleep to slow down rendering for better visualization
        time.sleep(0.05)

    print(f"Episode {episode + 1} finished with reward: {episode_reward}")

# Close the environment
env.close()