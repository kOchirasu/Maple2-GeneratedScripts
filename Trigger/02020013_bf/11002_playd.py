""" trigger/02020013_bf/11002_playd.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PlayD', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='PlayD', value=1):
            return ActorOff()


class ActorOff(state.State):
    def on_enter(self):
        set_actor(triggerId=11002, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell D

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000059], arg2=0):
            return ActorOn()
        if user_value(key='PlayD', value=0):
            return ResetDelay()


class ActorOn(state.State):
    def on_enter(self):
        set_actor(triggerId=11002, visible=True, initialSequence='ks_quest_musical_B01_orange') # Bell D

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return ResetDelay()
        if user_value(key='PlayD', value=0):
            return ResetDelay()


class ResetDelay(state.State):
    def on_enter(self):
        set_actor(triggerId=11002, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell D

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return ActorOff()
        if user_value(key='PlayD', value=0):
            return Wait()


