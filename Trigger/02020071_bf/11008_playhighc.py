""" trigger/02020071_bf/11008_playhighc.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='PlayHighC', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PlayHighC', value=1):
            return ActorOff(self.ctx)


class ActorOff(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=11007, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell HighC

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000065], stateValue=0):
            return ActorOn(self.ctx)
        if self.user_value(key='PlayHighC', value=0):
            return ResetDelay(self.ctx)


class ActorOn(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=11008, visible=True, initialSequence='ks_quest_musical_B01_pink') # Bell HighC

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=700):
            return ResetDelay(self.ctx)
        if self.user_value(key='PlayHighC', value=0):
            return ResetDelay(self.ctx)


class ResetDelay(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=11008, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell HighC

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return ActorOff(self.ctx)
        if self.user_value(key='PlayHighC', value=0):
            return Wait(self.ctx)


initial_state = Wait
