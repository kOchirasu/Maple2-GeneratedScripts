""" trigger/02000498_bf/debuff_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return 버프(self.ctx)


class 버프(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3600', seconds=3600)
        self.add_buff(boxIds=[103], skillId=70000071, level=2, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3600'):
            return 대기(self.ctx)


initial_state = 대기
