""" trigger/02000243_bf/timer.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[2001], visible=False)
        self.set_effect(triggerIds=[2002], visible=False)
        self.set_effect(triggerIds=[2003], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[202]):
            return 초재기1(self.ctx)


class 초재기1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='99', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='99'):
            return 초재기2(self.ctx)


class 초재기2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='99', seconds=3)
        self.set_event_ui(type=1, arg2='$02000243_BF__TIMER__0$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[2001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='99'):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='99', seconds=3)
        self.set_event_ui(type=1, arg2='$02000243_BF__TIMER__1$', arg3='3000', arg4='0')
        self.set_effect(triggerIds=[2002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='99'):
            return 초재기3(self.ctx)


class 초재기3(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000243_BF__TIMER__2$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='99'):
            return 유저이동음성(self.ctx)


class 유저이동음성(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 유저이동(self.ctx)


class 유저이동(trigger_api.Trigger):
    pass


initial_state = 대기
