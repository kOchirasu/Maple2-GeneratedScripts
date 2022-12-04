""" trigger/80000015_bonus/skill_08.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[713], enable=False)
        self.set_skill(triggerIds=[714], enable=False)
        self.set_skill(triggerIds=[715], enable=False)
        self.set_skill(triggerIds=[716], enable=False)
        self.set_skill(triggerIds=[717], enable=False)
        self.set_skill(triggerIds=[718], enable=False)
        self.set_skill(triggerIds=[719], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 스킬01(self.ctx)


class 스킬01(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[713], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 스킬02(self.ctx)


class 스킬02(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[714], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 스킬03(self.ctx)


class 스킬03(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[715], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 스킬04(self.ctx)


class 스킬04(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[716], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 스킬05(self.ctx)


class 스킬05(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[717], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 스킬06(self.ctx)


class 스킬06(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[718], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 스킬07(self.ctx)


class 스킬07(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[719], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 대기시간(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
