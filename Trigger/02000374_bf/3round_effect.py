""" trigger/02000374_bf/3round_effect.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='3Round_Effect', value=1):
            return Spawn_Start_Ready(self.ctx)


class Spawn_Start_Ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7999], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Skill_01(self.ctx)


class Skill_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[5021], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Skill_02(self.ctx)


class Skill_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[5022], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Skill_03(self.ctx)


class Skill_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[5023], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Skill_04(self.ctx)


class Skill_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[5024], enable=True)


initial_state = idle
