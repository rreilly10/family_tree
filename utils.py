import yaml


def get_config(environment):
    with open('config/{}.yaml'.format(environment), 'r') as ymlfile:
        return yaml.load(ymlfile)
