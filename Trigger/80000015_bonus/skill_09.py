""" trigger/80000015_bonus/skill_09.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[103]):
            return 대기시간(self.ctx)


class 대기시간(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[720], enable=False)
        self.set_skill(triggerIds=[721], enable=False)
        self.set_skill(triggerIds=[722], enable=False)
        self.set_skill(triggerIds=[723], enable=False)
        self.set_skill(triggerIds=[724], enable=False)
        self.set_skill(triggerIds=[725], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 스킬01(self.ctx)


class 스킬01(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[720], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 스킬02(self.ctx)


class 스킬02(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[721], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 스킬03(self.ctx)


class 스킬03(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[722], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 스킬04(self.ctx)


class 스킬04(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[723], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=200):
            return 스킬05(self.ctx)


class 스킬05(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[724], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 스킬06(self.ctx)


class 스킬06(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[725], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 대기시간(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
