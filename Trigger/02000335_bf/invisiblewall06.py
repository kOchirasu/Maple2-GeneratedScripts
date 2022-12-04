""" trigger/02000335_bf/invisiblewall06.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=708, boxId=1):
            return 벽면처리(self.ctx)


class 벽면처리(trigger_api.Trigger):
    pass


initial_state = 시작
