from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase, TextureStage
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3, NodePath
from panda3d.ai import *
from direct.gui.OnscreenImage import OnscreenImage
from src.Actor import *
from src.Action import *
import random

from src.SceneFileReader import SceneFileReader

DEFAULTBACKGROUND = "../../backgrounds/street/street1.jpg"

class SceneManager(ShowBase):

    def __init__(self,scene_nodes):
        ShowBase.__init__(self)
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        self.static_objects = []
        self.dynamic_objects = []
        self.actors = []
        self.actions = []
        self.scene_nodes = scene_nodes

        for scene in scene_nodes:
            self.load_background(scene.scene_tag,scene.time)
            self.load_terrain(scene.scene_tag)
            self.load_static_objects(scene.static_objects)
            self.load_Actors(scene.Actors)
            self.satisfy_scene_constrains(scene.initial_constrains)
            self.add_weather()
            # Now we need to play the animations
            # First: instantiate the actions
            for subscene in scene.subscenes:
                subscene_object = namedtuple("SubScene",subscene.keys(),*subscene.values())
                actions = subscene_object.actions
                for action in actions:
                    a = namedtuple("Action",action.keys(),*action.values())
                    act = ActionFactory.create_action(a,self.actors)
                    self.actions.append(act)
            # Second: Play the animations

                for action in self.actions:
                    action.play_action()






    def load_background(self,scene_tag,scene_time):
        #TODO : Add dummy background to load in case there is no background
        background_dir_path = os.path.join("../../backgrounds",scene_tag)
        images = [str(image) for image in os.listdir(self.background_dir_path)]
        #pick random background from the given images
        if len(images)>0:
            imageindex = random.randint(0,len(images)-1)
            image = images[imageindex]
            self.background_path=os.path.join(background_dir_path,image)
        else:
            self.background_path=DEFAULTBACKGROUND

        #TODO: Adjust the image brightness to match day or night(scene_time)

        self.b=OnscreenImage(parent=self.render2d, image =self.background_path)

        self.b.reparentTo(self.render2d)

        self.cam2d.node().getDisplayRegion(0).setSort(-20)




    def load_terrain(self,scene_tag):
        print(scene_tag)

    def load_static_objects(self,static_objects):
        print(static_objects)

    def load_Actors(self,actors):
        self.actors = dict([(actor["id"],ActorFactory.create_actor(actor)) for actor in actors])
        #TODO : Actors positioning required

        #Now reparent each actor to render
        for actor in self.actors.values():
            actor.reparentTo(self.render)




    def satisfy_scene_constrains(self,initial_constrains):
        print(initial_constrains)

    def add_weather(self):
        print("weather")


    #TODO: Define a procedure to move the camera instead of this
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), -20)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont







