""" trigger/02000335_bf/invisiblewall03.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=705, boxId=1):
            return 벽면처리(self.ctx)


class 벽면처리(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[7040,7041,7042,7043,7044,7045,7046,7047,7048,7049,7050], visible=False, delay=0, scale=10) # 벽 해제


initial_state = 시작
