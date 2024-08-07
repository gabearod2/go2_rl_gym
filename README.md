# Unitree Go2 RL GYM

Forked from [Unitree's RL Gym](https://github.com/unitreerobotics/unitree_rl_gym.git).

### Installation

1. Install Isaac Gym
   - Download and install Isaac Gym Preview 4 from [https://developer.nvidia.com/isaac-gym](https://developer.nvidia.com/isaac-gym)
   - `cd isaacgym/python && pip install -e .`
   - Try running an example `cd examples && python 1080_balls_of_solitude.py`
   - For extra help:
      - [Setting up Isaac Gym](https://learningreinforcementlearning.com/setting-up-isaac-gym-on-an-ubuntu-laptop-785b5a15e5a9)
      - [Install Isaac Gym](https://medium.com/@piliwilliam0306/install-isaac-gym-on-ubuntu-22-04-8ebf4b86e6f7)
2. Create a new python virtual env with python 3.6, 3.7 or 3.8 (3.8 recommended), you can use the following executable:
   ```
   cd isaac gym
   ./create_env_rlgpu.sh
   conda activate rlgpu
   ```
4. Ensure you have the correct pytorch with cuda for your system. I am using torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1+cu117 with an NVIDIA GeForce RTX 4090 (Notebook):
   ```
   pip uninstall torch torchaudio torchvision # if rlgpu's version does not work with your GPU
   pip install torch==1.10.0+cu113 torchvision==0.11.1+cu113 torchaudio==0.10.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html # recommended 
   ```
5. Install rsl_rl (PPO implementation)

   - Clone [https://github.com/leggedrobotics/rsl_rl](https://github.com/leggedrobotics/rsl_rl)
   - `cd rsl_rl && git checkout v1.0.2 && pip install -e .`

6. Install go2_rl_gym
   - Clone this repository
   - Navigate to the folder `go2_rl_gym`
   - `pip install -e .`

### Usage (From root directory)

1. Train:
   `python legged_gym/scripts/train.py --task=go2`

   * To run on CPU add following arguments: `--sim_device=cpu`, `--rl_device=cpu` (sim on CPU and rl on GPU is possible).
   * To run headless (no rendering) add `--headless`.
   * **Important** : To improve performance, once the training starts press `v` to stop the rendering. You can then enable it later to check the progress.
   * The trained policy is saved in `logs/<experiment_name>/<date_time>_<run_name>/model_<iteration>.pt`. Where `<experiment_name>` and `<run_name>` are defined in the train config.
   * The following command line arguments override the values set in the config files:
   * --task TASK: Task name.
   * --resume: Resume training from a checkpoint
   * --experiment_name EXPERIMENT_NAME: Name of the experiment to run or load.
   * --run_name RUN_NAME: Name of the run.
   * --load_run LOAD_RUN: Name of the run to load when resume=True. If -1: will load the last run.
   * --checkpoint CHECKPOINT: Saved model checkpoint number. If -1: will load the last checkpoint.
   * --num_envs NUM_ENVS: Number of environments to create.
   * --seed SEED: Random seed.
   * --max_iterations MAX_ITERATIONS: Maximum number of training iterations.
2. Play:`python legged_gym/scripts/play.py --task=go2`

   * By default, the loaded policy is the last model of the last run of the experiment folder.
   * Other runs/model iteration can be selected by setting `load_run` and `checkpoint` in the train config.


