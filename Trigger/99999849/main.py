""" trigger/99999849/main.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Test', value=2):
            return None # Missing State: 두번


initial_state = 대기
