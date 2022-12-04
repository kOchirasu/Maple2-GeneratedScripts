""" trigger/65000002_bd/buffskill.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return 초대기2(self.ctx)


class 초대기2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 스킬랜덤(self.ctx)


class 스킬랜덤(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.play_system_sound_in_box(sound='BD_Buffskill_00')
        self.show_guide_summary(entityId=26500202, textId=26500202, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[103]):
            return 초기화(self.ctx)
        if self.random_condition(rate=33):
            return A스킬작동(self.ctx)
        if self.random_condition(rate=33):
            return B스킬작동(self.ctx)
        if self.random_condition(rate=34):
            return C스킬작동(self.ctx)


class A스킬작동(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7001], enable=True)
        self.set_timer(timerId='60', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='60'):
            self.set_skill(triggerIds=[7001], enable=False)
            return 스킬랜덤(self.ctx)


class B스킬작동(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7002], enable=True)
        self.set_timer(timerId='60', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='60'):
            self.set_skill(triggerIds=[7002], enable=False)
            return 스킬랜덤(self.ctx)


class C스킬작동(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[7003], enable=True)
        self.set_timer(timerId='60', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='60'):
            self.set_skill(triggerIds=[7003], enable=False)
            return 스킬랜덤(self.ctx)


class 초기화(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_skill(triggerIds=[7001], enable=False)
        self.set_skill(triggerIds=[7002], enable=False)
        self.set_skill(triggerIds=[7003], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
