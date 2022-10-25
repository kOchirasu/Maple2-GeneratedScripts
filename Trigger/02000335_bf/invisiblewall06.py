""" trigger/02000335_bf/invisiblewall06.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=708, boxId=1):
            return 벽면처리(self.ctx)


class 벽면처리(common.Trigger):
    pass


initial_state = 시작
