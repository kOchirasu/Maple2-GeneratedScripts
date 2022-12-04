""" trigger/02020112_bf/reconnect.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Reconnect', value=1):
            return 버프쏴주기(self.ctx)


class 버프쏴주기(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[916], skillId=70002105, level=1, isSkillSet=False)
        self.set_timer(timerId='1', seconds=5, startDelay=0, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Reconnect', value=2):
            return 종료(self.ctx)
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[931], skillId=70002112, level=1, isSkillSet=False)


initial_state = 대기
