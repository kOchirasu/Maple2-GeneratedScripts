""" trigger/02010039_bf/checkbridge06.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[5002], questIds=[40002110], questStates=[1]):
            return 업적발생(self.ctx)


class 업적발생(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=5002, type='trigger', achieve='checkBridge')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 초기화준비(self.ctx)


class 초기화준비(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
