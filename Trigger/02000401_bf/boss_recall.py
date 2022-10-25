""" trigger/02000401_bf/boss_recall.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[2099]):
            return 발신(self.ctx)


class 발신(common.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='recall', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
