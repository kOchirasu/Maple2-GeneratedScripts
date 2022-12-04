""" trigger/02000486_bf/105_resurrection_1.xml """
import trigger_api


class 전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[901]):
            return 타임(self.ctx)


class 타임(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=240000):
            return 버프(self.ctx)


class 버프(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='RageBuff_2', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 버프_종료(self.ctx)


class 버프_종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='RageBuff_2', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return None


initial_state = 전투시작
