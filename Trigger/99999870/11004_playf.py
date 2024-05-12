""" trigger/99999870/11004_playf.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='PlayF', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PlayF', value=1):
            return ActorOff(self.ctx)


class ActorOff(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=11004, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell F

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000061], stateValue=0):
            # Bell F
            return ActorOn(self.ctx)
        if self.user_value(key='PlayF', value=0):
            return ResetDelay(self.ctx)


class ActorOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=11004, visible=True, initialSequence='ks_quest_musical_B01_green') # Bell F

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=700):
            return ResetDelay(self.ctx)
        if self.user_value(key='PlayF', value=0):
            return ResetDelay(self.ctx)


class ResetDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=11004, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell F

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return ActorOff(self.ctx)
        if self.user_value(key='PlayF', value=0):
            return Wait(self.ctx)


initial_state = Wait
