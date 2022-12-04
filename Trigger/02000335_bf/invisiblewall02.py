""" trigger/02000335_bf/invisiblewall02.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=704, boxId=1):
            return 벽면처리(self.ctx)


class 벽면처리(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[7021,7022,7023,7024,7025,7026,7027,7028,7029,7030,7031,7032], visible=False, delay=0, scale=10) # 벽 해제


initial_state = 시작
