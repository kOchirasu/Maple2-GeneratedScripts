""" trigger/80000014_bonus/skill_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[703], enable=False)
        self.set_visible_breakable_object(triggerIds=[7301,7302,7303], visible=False)
        self.set_breakable(triggerIds=[7301,7302,7303], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self):
        self.set_visible_breakable_object(triggerIds=[7301,7302,7303], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[7301,7302,7303], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 스킬발동(self.ctx)


class 스킬발동(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[703], enable=True)
        self.set_breakable(triggerIds=[7301,7302,7303], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 시작(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
