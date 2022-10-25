""" trigger/02020030_bf/11003_playe.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='PlayE', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='PlayE', value=1):
            return ActorOff(self.ctx)


class ActorOff(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=11003, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell E

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000060], stateValue=0):
            return ActorOn(self.ctx)
        if self.user_value(key='PlayE', value=0):
            return ResetDelay(self.ctx)


class ActorOn(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=11003, visible=True, initialSequence='ks_quest_musical_B01_yellow') # Bell E

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=700):
            return ResetDelay(self.ctx)
        if self.user_value(key='PlayE', value=0):
            return ResetDelay(self.ctx)


class ResetDelay(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=11003, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell E

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return ActorOff(self.ctx)
        if self.user_value(key='PlayE', value=0):
            return Wait(self.ctx)


initial_state = Wait
