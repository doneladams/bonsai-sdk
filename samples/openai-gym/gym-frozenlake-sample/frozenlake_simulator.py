import sys
import numpy
import logging

from bonsai_ai import Brain, Config
from bonsai_gym import GymSimulator
from gym.envs.registration import register

log = logging.getLogger('gym_simulator')
log.setLevel(logging.DEBUG)

# frozenlake
ENVIRONMENT = 'FrozenLake-no-slip-v0'

# Map types: 4x4 or 8x8.
MAP_4x4 = '4x4'
MAP_8x8 = '8x8'

# Whether or not choose the non-deterministic states.
IS_SLIPPERY = False

# Register a custom environment for frozen lake with deterministic states
register(
    id=ENVIRONMENT,
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name': MAP_4x4,
            'is_slippery': IS_SLIPPERY},
    tags={'wrapper_config.TimeLimit.max_episode_steps': 100},
    reward_threshold=0.78,
)


class FrozenLake(GymSimulator):
    environment_name = ENVIRONMENT
    simulator_name = 'frozenlake_simulator'

    def gym_to_state(self, observation):
        state = {'current_pos': observation}
        return state

    def action_to_gym(self, actions):
        return actions['command']


if __name__ == '__main__':
    # create a brain, openai-gym environment, and simulator
    config = Config(sys.argv)
    brain = Brain(config)
    sim = FrozenLake(brain)
    sim.run_gym()