
class Action(object):


    def play_action(self):
        pass

class OneActorActions(Action):

    def __init__(self,action,actors):
        self.actor = actors[action.actor_id]


class TwoActorActions(Action):
    def __init__(self,action,actors):
        self.actor = actors[action.actor_id]
        self.acted_upon = actors[action.acted_upon]


class look_at(TwoActorActions):
    #TODO : Implement action
    def play_action(self):
        self.actor.lookAt(self.acted_upon)

class bark(OneActorActions):
    #TODO : Implement action
    def play_action(self):
        pass

class wander(OneActorActions):
    #TODO : Implement action
    def play_action(self):
        pass

class say(OneActorActions):
    #TODO : Implement action
    def play_action(self):
        # Display a speech bubble above the character containing the text in text property
        # Add sound from text to speech in phase 2
        pass

class run_towards(TwoActorActions):
    #TODO : Implement action
    def play_action(self):
        pass















class ActionFactory(object):

    Actions={
        "look_at":look_at,
        "bark":bark,
        "wander":wander,
        "say":say,
        "run_towards":run_towards
    }




    @staticmethod
    def create_action(action,actors):
        type = action["sub_type"]
        return ActionFactory.Actions[type](action,actors)


















