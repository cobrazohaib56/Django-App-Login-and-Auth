import os

def required_env_var(var_name):
    name = os.environ.get(var_name)
    if name is None:
        raise EnvironmentError(f'Error, variable not found')
    return name
    