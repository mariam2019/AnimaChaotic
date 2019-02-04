from direct.actor.Actor import Actor
from collections import namedtuple
from src.DataBaseManager import get_database
import os
from panda3d.ai import *


DEFAULTCHARACTER = "../models/dummy.egg"
DEFAULTANIMAL = "../models/dummy.egg"


# def Character1(): #temporary may be deleted
#
#     def __init__(self):
#         #TODO: Add more properties (clothes - color )
#         self.properties = {"type":"boy"
#                            }
#         self.adjectives = []    # TODO : May be needed to get the closest character match
#         self.m_id = 1
#         self.model_path = ""  # TODO: Set to a default model path
#         self.model = object()
#         self.actions_dictionary = dict()  # TODO: set to a default dictionary
#         self.action = object()  # TODO: set to a default action
#         self.position = object()  # TODO:set to a default position
#         self.scale = object()  # TODO: set to a default scale
#
#     def set_id(self, id):
#         self.m_id = id
#
#     def load_Actor(self, model_path, actions_dictionary):
#         self.model_path = model_path
#         self.actions_dictionary = actions_dictionary
#         self.model = Actor(model_path, actions_dictionary)
#
#     def set_action(self, action):
#         self.action = action
#
#     def set_position(self, pos):
#         self.model.setpos(*pos)
#
#     def set_scale(self, scale):
#         self.model.setScale(*scale)


class BaseActor(object):

    def __init__(self):

        self.model =object()
    def reparent(self,scene):
        self.model.reparentTo(scene)

    def set_pos(self,pos):
        self.model.setPos(-100,400, -100)

    def set_scale(self,scale):
        self.model.setScale(10,10,10)


class Animal(BaseActor):

    def __init__(self, actor):
        a = namedtuple("actor", actor.keys())(*actor.values())
        self.id = a.id
        self.type = a.subtype
        self.properties = a.properties
        db = get_database()
        animal = db.animals.find_one(
            {"type": self.type})  # TODO: Add checks if the model is not found retrieve default model

        temp_path =os.path.join("../models/animals", animal.modelname) #TODO : may change the extension to egg

        self.modelpath = temp_path if os.path.exists(temp_path) else DEFAULTANIMAL
        #TODO : Add a check if the animation is not loaded correctly
        self.animations = dict(
            [(anim, os.path.join("../models/animals", "%s_%s"%(animal["modelname"], anim))) for anim in
             animal["animations"]])
        self.model = Actor(self.modelpath, self.animations)


class Character(BaseActor):

    def __init__(self, actor):

        a = namedtuple("actor", actor.keys())(*actor.values())

        db = get_database()

        self.id = a.id
        self.type = a.subtype
        self.properties = a.properties

        character = db.characters.find_one({"type": self.type})  # TODO: Add checks if the model is not found retrieve default model


        self.modelpath = os.path.join("../models/characters", character['modelname'])
        self.animations = dict(
            [(anim, os.path.join("../models/characters", ("%s_%s"%(character['modelname'],anim)))) for anim in
             character['animations']])
        print(self.animations)
        self.model = Actor(self.modelpath, self.animations)
        #TODO : Adjust poisition and scale outside of this function
        self.model.setScale(10,10,10)
        self.model.setPos(-100,400,-100)
        self.AIchar = AICharacter(str(self.id),self.model,100, 500,5)




class ActorFactory(object):

    Actors_dictionary = {
        "person": Character,
        "animal": Animal
    }

    @staticmethod
    def create_actor(actor):
        type = actor["type"]
        return ActorFactory.Actors_dictionary.get(type, lambda: "Invalid")(actor)
