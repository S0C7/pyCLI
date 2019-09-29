import yaml
import io
'''
    This 
'''
def readyml(filepath):
    with io.open(filepath, "r") as stream:
        data_loaded = yaml.safe_load(stream)
    return data_loaded

print(readyml("resources/init.yml"))
