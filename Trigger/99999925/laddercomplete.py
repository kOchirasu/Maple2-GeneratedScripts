""" trigger/99999925/laddercomplete.xml """
from common import *
import state


class IsLadderComplete(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[311], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[312], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[313], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[314], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[315], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[316], visible=False, animationEffect=False, animationDelay=0)

    def on_tick(self) -> state.State:
        if user_value(key='ladderComp', value=1):
            return ladderComplete()


class ladderComplete(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[311], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[312], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[313], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[314], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[315], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[316], visible=True, animationEffect=True, animationDelay=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return End()


class End(state.State):
    pass


