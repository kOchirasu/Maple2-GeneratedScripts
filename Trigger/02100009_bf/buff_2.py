""" trigger/02100009_bf/buff_2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 버프(self.ctx)


class 버프(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[101], skillId=50000206, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 대기(self.ctx)


initial_state = 대기
