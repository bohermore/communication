import gym
import numpy as np
import tensorflow as tf
from gym.utils import seeding


class CustomEnv(gym.Env):
    labels = None
    images = None
    def __init__(self):
        self.seed()
        (self.images, self.labels), _ = tf.keras.datasets.mnist.load_data()
        self.state = None

    def step(self, action):
        reward = action == sum(self.hidden_state)
        return self.state, reward, True, {}

    def reset(self):
        first_index = np.random.randint(0, len(self.labels))
        second_index = np.random.randint(0, len(self.labels))

        self.state = (self.images[first_index], self.images[second_index])
        self.hidden_state = (self.labels[first_index], self.labels[second_index])
        # print('{} + {} = {} '.format(self.first_label, self.second_label, self.total))
        return self.state

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]


if __name__ == '__main__':
    env = CustomEnv()
    env.reset()
    resp = env.step(10)
    print(resp)
