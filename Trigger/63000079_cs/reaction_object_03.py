""" trigger/63000079_cs/reaction_object_03.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[5001]):
            return 채집가능(self.ctx)


class 채집가능(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[603], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[603], stateValue=2):
            self.create_item(spawnIds=[1003])
            return 채집완료(self.ctx)


class 채집완료(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=30, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 대기(self.ctx)


initial_state = 대기
