""" trigger/02000421_bf/main.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기
        self.set_mesh(triggerIds=[6001], visible=False)
        self.set_mesh(triggerIds=[6002], visible=False)
        self.set_mesh(triggerIds=[6003], visible=False)
        self.set_mesh(triggerIds=[6004], visible=False)
        self.set_mesh(triggerIds=[6005], visible=False)
        self.set_mesh(triggerIds=[6006], visible=False)
        self.set_mesh(triggerIds=[6007], visible=False)
        self.set_mesh(triggerIds=[6008], visible=False)
        self.set_mesh(triggerIds=[6009], visible=False)
        self.set_mesh(triggerIds=[6010], visible=False)
        self.set_mesh(triggerIds=[6011], visible=False)
        self.set_mesh(triggerIds=[6012], visible=False)
        self.set_mesh(triggerIds=[6013], visible=False)
        self.set_mesh(triggerIds=[6014], visible=False)
        self.set_mesh(triggerIds=[6015], visible=False)
        self.set_mesh(triggerIds=[6016], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=700, minUsers='1'):
            return Ready_Idle(self.ctx)


class Ready_Idle(trigger_api.Trigger):
    pass


initial_state = Ready
