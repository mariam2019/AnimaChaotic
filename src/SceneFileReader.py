
import json
from collections import namedtuple
class SceneFileReader(object):

    def __init__(self,filename):

        self.filename = filename


    def readFile(self):

        with open(self.filename) as data_file:
            data = json.load(data_file)

        scene_nodes = [namedtuple('SceneNode',node.keys())(*node.values()) for node in data["scene_nodes"]]

        return scene_nodes
