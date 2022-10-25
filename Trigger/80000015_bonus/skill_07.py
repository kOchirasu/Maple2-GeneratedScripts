""" trigger/80000015_bonus/skill_07.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[712], enable=False)
        self.set_skill(triggerIds=[726], enable=False)
        self.set_visible_breakable_object(triggerIds=[7701,7702,7703,7704], visible=False)
        self.set_breakable(triggerIds=[7701,7702,7703,7704], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199]):
            return 대기시간(self.ctx)


class 대기시간(common.Trigger):
    def on_enter(self):
        self.set_visible_breakable_object(triggerIds=[7701,7702,7703,7704], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[7701,7702,7703,7704], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 스킬발동(self.ctx)


class 스킬발동(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[712], enable=True)
        self.set_skill(triggerIds=[726], enable=True)
        self.set_breakable(triggerIds=[7701,7702,7703,7704], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 시작(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
