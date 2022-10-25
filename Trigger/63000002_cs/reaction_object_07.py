""" trigger/63000002_cs/reaction_object_07.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[5001]):
            return 채집가능(self.ctx)


class 채집가능(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[607], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[607], stateValue=2):
            self.create_item(spawnIds=[1007])
            return 채집완료(self.ctx)


class 채집완료(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='7', seconds=30, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='7'):
            return 대기(self.ctx)


initial_state = 대기
