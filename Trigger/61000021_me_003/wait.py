""" trigger/61000021_me_003/wait.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[100]):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 시작
