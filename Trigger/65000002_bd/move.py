""" trigger/65000002_bd/move.xml """
import trigger_api


class 이동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=102, boxId=10):
            return 이동(self.ctx)


initial_state = 이동
