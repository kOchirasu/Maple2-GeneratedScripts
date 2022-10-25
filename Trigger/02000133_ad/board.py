""" trigger/02000133_ad/board.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000346], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000346], stateValue=0):
            return 어나운스(self.ctx)


class 어나운스(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000133_AD__BOARD__0$', arg3='4000', arg4='101')
        self.set_timer(timerId='5', seconds=5, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 대기(self.ctx)


initial_state = 대기
