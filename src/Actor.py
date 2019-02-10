from random import randint

from direct.actor.Actor import Actor
from collections import namedtuple

from panda3d.bullet import BulletCapsuleShape, ZUp, BulletCharacterControllerNode, BulletRigidBodyNode
from panda3d.core import BitMask32

from src.DataBaseManager import get_database
import os
from panda3d.ai import *


DEFAULTCHARACTER = "../models/dummy"
DEFAULTANIMAL = "../models/dummy"
DEFAULTDYNAMICOBJECT = ""
DEFAULTCHARACTERANIMATIONS = []
DEFAULTANIMALANIMATIONS = []
DEFAULTOBJECTANIMATIONS = []
DEFAULTOBJNAME = ""
DEFAULTDYNAMICOBJECTNAME=""
DEFAULTCHARACTERNAME=""
DEFAULTANIMALNAME=""

DEFAULTOBJ = ""
DEFAULTOBJANIM = []

defaults = {
    "person":(DEFAULTCHARACTER,DEFAULTCHARACTERNAME,DEFAULTCHARACTERANIMATIONS),
    "animal":(DEFAULTANIMAL,DEFAULTANIMALNAME,DEFAULTANIMALANIMATIONS),
    "dynamic_object":(DEFAULTDYNAMICOBJECT,DEFAULTDYNAMICOBJECTNAME,DEFAULTOBJECTANIMATIONS),

}



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


# class BaseActor(object):
#
#     def __init__(self):
#
#         self.model =object()
#     def reparent(self,scene):
#         self.model.reparentTo(scene)
#
#     def set_pos(self,pos):
#         self.model.setPos(-100,400, -100)
#
#     def set_scale(self,scale):
#         self.model.setScale(10,10,10)
#
#
# class Animal(BaseActor):
#
#     def __init__(self, actor):
#         a = namedtuple("actor", actor.keys())(*actor.values())
#         self.id = a.id
#         self.type = a.subtype
#         self.properties = a.properties
#         db = get_database()
#         animal = db.animals.find_one(
#             {"type": self.type})  # TODO: Add checks if the model is not found retrieve default model
#
#         temp_path =os.path.join("../models/animals", animal.modelname) #TODO : may change the extension to egg
#
#         self.modelpath = temp_path if os.path.exists(temp_path) else DEFAULTANIMAL
#         #TODO : Add a check if the animation is not loaded correctly
#         self.animations = dict(
#             [(anim, os.path.join("../models/animals", "%s_%s"%(animal["modelname"], anim))) for anim in
#              animal["animations"]])
#         self.model = Actor(self.modelpath, self.animations)
#
#
#
# class Character(BaseActor):
#
#     def __init__(self, actor):
#
#         a = namedtuple("actor", actor.keys())(*actor.values())
#
#         db = get_database()
#
#         self.id = a.id
#         self.type = a.subtype
#         self.properties = a.properties
#
#         character = db.characters.find_one({"type": self.type})  # TODO: Add checks if the model is not found retrieve default model
#
#
#         self.modelpath = os.path.join("../models/characters", character['modelname'])
#         self.animations = dict(
#             [(anim, os.path.join("../models/characters", ("%s_%s"%(character['modelname'],anim)))) for anim in
#              character['animations']])
#         print(self.animations)
#         self.model = Actor(self.modelpath, self.animations)
#         #TODO : Adjust poisition and scale outside of this function
#         self.model.setScale(10,10,10)
#         #self.model.setPos(-100,400,-100)
#         self.AIchar = AICharacter(str(self.id),self.model,100, self.model.getSx()*0.05,self.model.getSx()*5)
#
#
#
#     def add_character_controller(self):
#         height = self.model.getSz()
#         radius = self.model.getSx()//2
#         shape = BulletCapsuleShape(radius, height - 2*radius, ZUp)
#         self.player_node = BulletRigidBodyNode()
#         self.player_node.add_shape(shape)
#         return self.player_node
#
#
#
#
#
#
#
#
#
#
#
# class ActorFactory(object):
#
#     Actors_dictionary = {
#         "person": Character,
#         "animal": Animal
#     }
#
#     @staticmethod
#     def create_actor(actor):
#         type = actor["type"]
#         return ActorFactory.Actors_dictionary.get(type, lambda: "Invalid")(actor)


def get_default_model(type):
    model_path,animations = defaults.get(type,(DEFAULTOBJ,DEFAULTOBJECTANIMATIONS))
    return model_path,animations



class BaseActor(object):

    def __init__(self,actor):

        self.model =object()

        a = namedtuple("actor", actor.keys())(*actor.values())

        db = get_database()

        self.id = a.id
        self.subtype = a.subtype
        self.properties = a.properties
        self.type = a.type



        models = [model for model in db.objects.find({"type":self.subtype})]
        #check if models exist otherwise load dummy actor
        if len(models)>0:
            print(len(models))
            model_index = randint(0,len(models)-1)
            model_choice= models[model_index]
            directory_path = model_choice["directory"]
            self.model_name = model_choice["name"]


            model_animations = model_choice["animations"]
            self.boundingX = model_choice["boundingX"]
            self.boundingY = model_choice["boundingY"]
            self.boundingZ = model_choice["boundingZ"]
        else:
            directory_path,self.model_name,model_animations = get_default_model(self.type)

            self.boundingX = 1.0
            self.boundingY = 1.0
            self.boundingZ = 1.0

        self.model_path = os.path.join(directory_path,self.model_name)
        self.animations = dict(
            [(anim, os.path.join(directory_path, ("%s_%s"%(self.model_name,anim)))) for anim in
             model_animations])
        print(self.animations)

        self.model = Actor(self.model_path, self.animations)
        print("my model")

        #TODO : Adjust poisition and scale outside of this function
        #self.model.setScale(10,10,10)
        #self.model.setPos(-100,400,-100)
        self.AIchar = AICharacter(str(self.id),self.model,100, self.model.getSx()*0.05,self.model.getSx()*5)

    def reparent(self,obj):
        self.model.reparentTo(obj)

    def set_pos(self,pos):
        #self.model.setPos(-100,400, -100)
        self.model.setPos(pos)

    def set_scale(self,scale):
        #self.model.setScale(10,10,10)
        self.model.setScale(scale)

