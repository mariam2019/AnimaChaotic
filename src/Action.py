from direct.interval.MetaInterval import Sequence, Vec3
from direct.task import Task
from panda3d.core import Point3


class Action(object):



    def play_action(self):
        pass

class OneActorActions(Action):

    def __init__(self,action,actors,task_mgr):
        self.task_Mgr = task_mgr
        self.actor = actors[action.actor_id]


class TwoActorActions(Action):
    def __init__(self,action,actors,task_mgr,static_objects):

        print("two actor constructor",action,actors)
        self.task_Mgr = task_mgr
        self.actor = actors[action.actor_id]
        self.acted_upon = static_objects[action.acted_upon]
        print(self.actor,self.acted_upon)


class look_at(TwoActorActions):
    #TODO : Implement action
    def play_action(self):
        self.actor.model.lookAt(self.acted_upon.model)
        pass

class bark(OneActorActions):
    #TODO : Implement action
    def play_action(self):
        pass

class wander(OneActorActions):
    #TODO : Implement action
    def play_action(self):


        AIbehaviors = self.actor.AIchar.getAiBehaviors()

        AIbehaviors.wander(100, 0, 300, 1.0)
        self.actor.model.loop("run")



class say(OneActorActions):
    #TODO : Implement action
    def play_action(self):
        # Display a speech bubble above the character containing the text in text property
        # Add sound from text to speech in phase 2
        pass

class run_towards(TwoActorActions):
    #TODO : Implement action
    def play_action(self):

        # AIbehaviors = self.actor.AIchar.getAiBehaviors()
        # AIbehaviors.seek(self.acted_upon.model)

        self.actor.model.loop("run")
        # This lets the actor move to point 10, 10, 10 in 1.0 second.
        myInterval1 =  self.actor.model.posInterval(1.0, Point3(-200, 400, -100))

        # This move takes 2.0 seconds to complete.
        myInterval2 =  self.actor.model.posInterval(2.0, Point3(0, 400, -100))

        # # You can specify a starting position, too.
        # myInterval3 =  self.actor.player_node.posInterval(1.0, Point3(2, -3, 8), startPos=Point3(2, 400, 1))

        # This rotates the actor 180 degrees on heading and 90 degrees on pitch.
        myInterval4 =  self.actor.model.hprInterval(1.0, Vec3(180, 90, 0))
        # self.actorPos = self.actor.model.getPos()
        # self.modelPos = self.acted_upon.model.getPos()
        #self.task_Mgr.add(self.stop_task)
        seq =Sequence(myInterval1,myInterval4,myInterval4)
        seq.start()




    def stop_task(self,task):


        # if self.actorPos.x == self.modelPos.x and self.actorPos.y == self.modelPos.y:
        #     self.actor.model.stop()

        return Task.cont

















class ActionFactory(object):

    Actions={
        "look_at":look_at,
        "bark":bark,
        "wander":wander,
        "say":say,
        "run_towards":run_towards
    }




    @staticmethod
    def create_action(action,actors,static_objects,task_mgr):


        type = action.sub_type
        return ActionFactory.Actions[type](action,actors,task_mgr,static_objects)


















