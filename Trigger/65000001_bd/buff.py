""" trigger/65000001_bd/buff.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[104]):
            return 버프(self.ctx)


class 버프(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.add_buff(boxIds=[102], skillId=70000040, level=1, isPlayer=False, isSkillSet=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
