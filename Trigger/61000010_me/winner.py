""" trigger/61000010_me/winner.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[102]):
            return 업적(self.ctx)


class 업적(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=102, type='trigger', achieve='WinSanghaiRunners')


initial_state = 대기
