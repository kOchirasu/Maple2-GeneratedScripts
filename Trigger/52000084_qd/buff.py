""" trigger/52000084_qd/buff.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=199, skillId=70000115)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 버프(self.ctx)


class 버프(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[199], skillId=70000115, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 버프(self.ctx)
        if not self.user_detected(boxIds=[199]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
