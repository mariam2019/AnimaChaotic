from random import random

from panda3d.core import Point3, Vec3
from panda3d.bullet import BulletBoxShape, BulletRigidBodyNode
from src.DataBaseManager import get_database
import os

DEFAULT_OBJECT="../models/dummy"

class BaseObject(object):

    def __init__(self,m_object,loader):

        db = get_database()

        self.id = m_object['id']
        self.type = m_object['type']

        #self.properties = m_object['properties']


        models = [model for model in db.objects.find({"type":self.type})]
        #check if models exist otherwise load dummy actor
        if len(models)>0:
            model_index = random.randint(0,len(models)-1)
            model_choice= models[model_index]
            model_path = model_choice["directory"]
            self.boundingX = model_choice["boundingX"]
            self.boundingY = model_choice["boundingY"]
            self.boundingZ = model_choice["boundingZ"]

        else:
            model_path = DEFAULT_OBJECT
            self.boundingX = 1.0
            self.boundingY = 1.0
            self.boundingZ = 1.0

        # obj = db.objects.find_one({"type":self.type})
        # obj_path = os.path.join("../models/objects",type) if obj is not None else DEFAULT_OBJECT


        self.model = loader.loadModel(model_path)
        #TODO Remove that temp code Mariam will adjust position and scale
        #self.set_pos(Point3(0,400,-100))
        #self.set_scale(Point3(10,10,10))

    def reparent(self,scene):
        self.model.reparentTo(scene)


    def set_pos(self,pos):
        self.model.setPos(pos)

    def set_scale(self,scale):
        self.model.setScale(scale)

    def add_bounding_box(self):

        dx = self.model.getSx()//2
        dy = self.model.getSy()//2
        dz = self.model.getSz()//2
        shape = BulletBoxShape(Vec3(dx, dy, dz))
        self.physics_node = BulletRigidBodyNode()
        self.physics_node.add_shape(shape)

        return self.physics_node







