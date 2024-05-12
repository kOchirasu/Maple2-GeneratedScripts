""" trigger/02000335_bf/invisiblewall05.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=707, minUsers='1'):
            return 벽면처리(self.ctx)


class 벽면처리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[7061,7062,7063,7064,7065,7066,7067,7068,7069,7070], visible=False, delay=0, scale=10) # 벽 해제


initial_state = 시작
