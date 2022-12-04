""" trigger/02000335_bf/invisiblewall04.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=706, boxId=1):
            return 벽면처리(self.ctx)


class 벽면처리(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[7051,7052,7053,7054,7055,7056,7057,7058,7059,7060], visible=False, delay=0, scale=10) # 벽 해제


initial_state = 시작
