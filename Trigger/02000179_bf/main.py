""" trigger/02000179_bf/main.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return None # Missing State: 퀘스트조건체크


class 종료(common.Trigger):
    pass


initial_state = 대기
