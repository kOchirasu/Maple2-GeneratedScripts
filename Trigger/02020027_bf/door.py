""" trigger/02020027_bf/door.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[9001,9002,9003,9004,9005,9006,9007], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(compare='lower', value=50, spawnId=201, isRelative=True):
            return 문열림(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[9001,9002,9003,9004,9005,9006,9007], visible=False, arg3=0, delay=0, scale=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1002]):
            return 문닫힘(self.ctx)


class 문닫힘(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[9001,9002,9003,9004,9005,9006], visible=True, arg3=0, delay=0, scale=10)
        self.set_mesh(triggerIds=[9007], visible=True, arg3=0, delay=0, scale=0) # <두번째 방 튀어나갈 사람에 대한 예외처리로 페이드없이 바로 생기는 투명 메쉬>

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
