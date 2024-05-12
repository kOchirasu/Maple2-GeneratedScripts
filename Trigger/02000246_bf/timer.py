""" trigger/02000246_bf/timer.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2001], visible=False)
        self.set_effect(trigger_ids=[2002], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[205]):
            return 초재기1(self.ctx)


class 초재기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='99', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 초재기2(self.ctx)


class 초재기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2001], visible=True)
        self.set_event_ui(type=1, arg2='$02000246_BF__TIMER__0$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='99'):
            return 유저이동(self.ctx)


class 유저이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000141, portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        return 유저이동음성(self.ctx)


class 유저이동음성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_effect(trigger_ids=[2002], visible=True)
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 유저이동(self.ctx)


initial_state = 대기
