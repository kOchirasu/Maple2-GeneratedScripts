""" trigger/52020010_qd/main_c.xml """
import common


class Idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2007], questIds=[60200055], questStates=[2]):
            return Actor_On(self.ctx)
        if self.quest_user_detected(boxIds=[2007], questIds=[60200055], questStates=[3]):
            return Actor_On(self.ctx)
        if self.quest_user_detected(boxIds=[2007], questIds=[60200060], questStates=[1]):
            return Actor_On(self.ctx)
        if self.quest_user_detected(boxIds=[2007], questIds=[60200060], questStates=[2]):
            return Actor_Off(self.ctx)
        if self.quest_user_detected(boxIds=[2007], questIds=[60200060], questStates=[3]):
            return Actor_Off(self.ctx)


class Actor_On(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=8001, visible=True, initialSequence='Event_01_A')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2007], questIds=[60200060], questStates=[2]):
            return Actor_Off(self.ctx)
        if self.quest_user_detected(boxIds=[2007], questIds=[60200060], questStates=[3]):
            return Actor_Off(self.ctx)


class Actor_Off(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=8001, visible=True, initialSequence='Event_01_A')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2007], questIds=[60200060], questStates=[2]):
            return Actor_Off(self.ctx)
        if self.quest_user_detected(boxIds=[2007], questIds=[60200060], questStates=[2]):
            return Actor_Off(self.ctx)


initial_state = Idle
