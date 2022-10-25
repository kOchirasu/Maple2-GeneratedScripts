""" trigger/99999905/move.xml """
import common


class 이동(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=102, boxId=10):
            return 이동(self.ctx)


initial_state = 이동
