import yaml

with open("python_env.yaml", "r") as f:
    env = yaml.safe_load(f)
    print(type(env))  # should be <class 'dict'>