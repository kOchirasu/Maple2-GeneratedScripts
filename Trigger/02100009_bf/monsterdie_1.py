""" trigger/02100009_bf/monsterdie_1.xml """
import trigger_api


class 유저감지(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1000049], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[100000001]):
            return 버프(self.ctx)


class 버프(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[100000002], skillId=50000217, level=1, isPlayer=True, isSkillSet=False)
        self.set_skill(triggerIds=[1000049], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return None


initial_state = 유저감지
