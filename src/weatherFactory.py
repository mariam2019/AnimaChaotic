import random

from direct.interval.MetaInterval import Sequence
from panda3d.core import Point3



def load_cloudy_weather(loader,scene):

    cloudpos = Point3(-200,400, 0)
    cloudscale = Point3(0.25,0.25,0.25)
    cloud = loader.loadModel("../weather/cloud.egg")
    cloud.setPos(cloudpos)
    cloud.setScale(cloudscale)

    cloud.reparentTo(scene)

    for i in range(7):
        cl = scene.attach_new_node('panda')
        cl.setPos(cloudpos.x*random.uniform(0.25,2.5),400,random.randint(0,50))
        cl.setScale(random.uniform(0.25,2.5))
        cloud.instanceTo(cl)

    interval1 = cloud.posInterval(10.0,Point3(80,400,0))
    interval2 = cloud.posInterval(10.0,Point3(-200,400,0))
    sequence = Sequence(interval1,interval2)
    sequence.loop()








class WeatherFactory(object):
    db = object()

    def __init__(self,loader):
        self.loader = loader


    Weather_dictionary = {
        "cloudy":load_cloudy_weather
    }


    def create_weather(self,type,scene):
        print(type)

        return WeatherFactory.Weather_dictionary.get(type)(self.loader,scene)
