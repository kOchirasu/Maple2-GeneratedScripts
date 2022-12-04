""" trigger/02000350_bf/debuff_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[102]):
            return 버프(self.ctx)


class 버프(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3600', seconds=3600)
        self.add_buff(boxIds=[102], skillId=70000071, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3600'):
            return 대기(self.ctx)


initial_state = 대기
