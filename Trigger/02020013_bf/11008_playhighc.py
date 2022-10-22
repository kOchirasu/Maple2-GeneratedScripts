""" trigger/02020013_bf/11008_playhighc.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PlayHighC', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='PlayHighC', value=1):
            return ActorOff()


class ActorOff(state.State):
    def on_enter(self):
        set_actor(triggerId=11007, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell HighC

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000065], arg2=0):
            return ActorOn()
        if user_value(key='PlayHighC', value=0):
            return ResetDelay()


class ActorOn(state.State):
    def on_enter(self):
        set_actor(triggerId=11008, visible=True, initialSequence='ks_quest_musical_B01_pink') # Bell HighC

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return ResetDelay()
        if user_value(key='PlayHighC', value=0):
            return ResetDelay()


class ResetDelay(state.State):
    def on_enter(self):
        set_actor(triggerId=11008, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell HighC

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return ActorOff()
        if user_value(key='PlayHighC', value=0):
            return Wait()


