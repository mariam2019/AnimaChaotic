from panda3d.core import Point3

from src.DataBaseManager import get_database
import os

DEFAULT_OBJECT="../models/dummy.egg"

class BaseObject(object):

    def __init__(self,m_object,loader):

        db = get_database()

        self.id = m_object['id']
        self.type = m_object['type']
        obj = db.objects.find_one({"type":self.type})
        obj_path = os.path.join("../models/objects",type) if obj is not None else DEFAULT_OBJECT

        self.model = loader.loadModel(obj_path)
        #TODO Remove that temp code Mariam will adjust position and scale
        self.set_pos(Point3(0,450,-90))
        self.set_scale(Point3(10,10,10))

    def reparent(self,scene):
        self.model.reparentTo(scene)


    def set_pos(self,pos):
        self.model.setPos(pos)

    def set_scale(self,scale):
        self.model.setScale(scale)



