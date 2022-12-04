""" trigger/02000076_tw_henesysvillage/02_npcbackup02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[1002], questIds=[10002041], questStates=[1]):
            return 지원군생성(self.ctx)


class 지원군생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[202], animationEffect=False)
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_22')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=4002, spawnIds=[202]):
            return 지원군이동(self.ctx)


class 지원군이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_202')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=2001, spawnIds=[202]):
            return 지원군소멸(self.ctx)


class 지원군소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[202])
        self.set_timer(timerId='1', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
