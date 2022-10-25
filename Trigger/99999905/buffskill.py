""" trigger/99999905/buffskill.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[103]):
            return 스킬랜덤(self.ctx)


class 스킬랜덤(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.set_event_ui(type=1, arg2='$99999905__BUFFSKILL__0$', arg3='2000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[103]):
            return 초기화(self.ctx)
        if self.random_condition(rate=33):
            return A스킬작동(self.ctx)
        if self.random_condition(rate=33):
            return B스킬작동(self.ctx)
        if self.random_condition(rate=34):
            return C스킬작동(self.ctx)


class A스킬작동(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7001], enable=True)
        self.set_timer(timerId='120', seconds=120)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='120'):
            self.set_skill(triggerIds=[7001], enable=False)
            return 스킬랜덤(self.ctx)


class B스킬작동(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7002], enable=True)
        self.set_timer(timerId='120', seconds=120)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='120'):
            self.set_skill(triggerIds=[7002], enable=False)
            return 스킬랜덤(self.ctx)


class C스킬작동(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7003], enable=True)
        self.set_timer(timerId='120', seconds=120)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='120'):
            self.set_skill(triggerIds=[7003], enable=False)
            return 스킬랜덤(self.ctx)


class 초기화(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[7001], enable=False)
        self.set_skill(triggerIds=[7002], enable=False)
        self.set_skill(triggerIds=[7003], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
