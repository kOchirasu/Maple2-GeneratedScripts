""" trigger/02000498_bf/debuff_03.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[104]):
            return 버프(self.ctx)


class 버프(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3600', seconds=3600)
        self.add_buff(boxIds=[104], skillId=70000071, level=3, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3600'):
            return 대기(self.ctx)


initial_state = 대기
