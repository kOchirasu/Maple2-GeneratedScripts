""" trigger/99999870/11006_playa.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='PlayA', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='PlayA', value=1):
            return ActorOff(self.ctx)


class ActorOff(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=11006, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell A

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000063], stateValue=0):
            return ActorOn(self.ctx)
        if self.user_value(key='PlayA', value=0):
            return ResetDelay(self.ctx)


class ActorOn(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=11006, visible=True, initialSequence='ks_quest_musical_B01_navy') # Bell A

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=700):
            return ResetDelay(self.ctx)
        if self.user_value(key='PlayA', value=0):
            return ResetDelay(self.ctx)


class ResetDelay(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=11006, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell A

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return ActorOff(self.ctx)
        if self.user_value(key='PlayA', value=0):
            return Wait(self.ctx)


initial_state = Wait
