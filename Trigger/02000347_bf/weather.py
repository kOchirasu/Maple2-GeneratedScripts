""" trigger/02000347_bf/weather.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=False)
        self.set_interact_object(triggerIds=[10000804], state=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[60002]):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000804], state=1)
        self.set_effect(triggerIds=[600], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000804], stateValue=0):
            return 비내림(self.ctx)


class 비내림(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=True)
        self.set_timer(timerId='30', seconds=30)
        self.set_event_ui(type=1, arg2='$02000347_BF__MAIN1__4$', arg3='2000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='30'):
            self.set_event_ui(type=1, arg2='$02000347_BF__MAIN1__3$', arg3='2000', arg4='0')
            return 시작(self.ctx)
        if self.monster_dead(boxIds=[101]):
            self.set_effect(triggerIds=[600], visible=False)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
