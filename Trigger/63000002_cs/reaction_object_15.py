""" trigger/63000002_cs/reaction_object_15.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[5001]):
            return 채집가능(self.ctx)


class 채집가능(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[615], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[615], stateValue=2):
            self.create_item(spawnIds=[1015])
            return 채집완료(self.ctx)


class 채집완료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='15', seconds=30, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='15'):
            return 대기(self.ctx)


initial_state = 대기
