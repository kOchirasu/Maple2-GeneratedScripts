""" trigger/02000179_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return None # Missing State: 퀘스트조건체크


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
