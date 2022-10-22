""" trigger/02020030_bf/11004_playf.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PlayF', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='PlayF', value=1):
            return ActorOff()


class ActorOff(state.State):
    def on_enter(self):
        set_actor(triggerId=11004, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell F

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000061], arg2=0):
            return ActorOn()
        if user_value(key='PlayF', value=0):
            return ResetDelay()


class ActorOn(state.State):
    def on_enter(self):
        set_actor(triggerId=11004, visible=True, initialSequence='ks_quest_musical_B01_green') # Bell F

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return ResetDelay()
        if user_value(key='PlayF', value=0):
            return ResetDelay()


class ResetDelay(state.State):
    def on_enter(self):
        set_actor(triggerId=11004, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell F

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return ActorOff()
        if user_value(key='PlayF', value=0):
            return Wait()

