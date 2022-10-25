""" trigger/02010054_bf/star_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3301,3302,3303,3304,3305], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000856], stateValue=0):
            return 소멸(self.ctx)


class 소멸(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3301,3302,3303,3304,3305], visible=True, arg3=0, delay=500, scale=3)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            self.set_mesh(triggerIds=[3301,3302,3303,3304,3305], visible=False, arg3=0, delay=900, scale=2)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
