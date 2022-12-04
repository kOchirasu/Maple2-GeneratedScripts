""" trigger/02000076_tw_henesysvillage/02_npcbackup05.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[1002], questIds=[10002041], questStates=[1]):
            return 지원군생성(self.ctx)


class 지원군생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[205], animationEffect=False)
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_25')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=4005, spawnIds=[205]):
            return 지원군이동(self.ctx)


class 지원군이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_205')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=2001, spawnIds=[205]):
            return 지원군소멸(self.ctx)


class 지원군소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[205])
        self.set_timer(timerId='1', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
