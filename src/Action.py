from direct.interval.MetaInterval import Sequence
from direct.task import Task


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

        AIbehaviors = self.actor.AIchar.getAiBehaviors()
        AIbehaviors.seek(self.acted_upon.model)
        self.actor.model.loop("run")
        self.actorPos = self.actor.model.getPos()
        self.modelPos = self.acted_upon.model.getPos()
       # self.task_Mgr.add(self.stop_task)




    def stop_task(self,task):


        if self.actorPos.x == self.modelPos.x and self.actorPos.y == self.modelPos.y:
            self.actor.model.stop()

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


















