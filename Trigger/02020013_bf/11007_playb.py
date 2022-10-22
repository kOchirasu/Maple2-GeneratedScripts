""" trigger/02020013_bf/11007_playb.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PlayB', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='PlayB', value=1):
            return ActorOff()


class ActorOff(state.State):
    def on_enter(self):
        set_actor(triggerId=11007, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell B

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000064], arg2=0):
            return ActorOn()
        if user_value(key='PlayB', value=0):
            return ResetDelay()


class ActorOn(state.State):
    def on_enter(self):
        set_actor(triggerId=11007, visible=True, initialSequence='ks_quest_musical_B01_purple') # Bell B

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return ResetDelay()
        if user_value(key='PlayB', value=0):
            return ResetDelay()


class ResetDelay(state.State):
    def on_enter(self):
        set_actor(triggerId=11007, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell B

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return ActorOff()
        if user_value(key='PlayB', value=0):
            return Wait()


