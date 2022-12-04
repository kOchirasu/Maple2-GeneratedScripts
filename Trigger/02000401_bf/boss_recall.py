""" trigger/02000401_bf/boss_recall.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[2099]):
            return 발신(self.ctx)


class 발신(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='recall', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
