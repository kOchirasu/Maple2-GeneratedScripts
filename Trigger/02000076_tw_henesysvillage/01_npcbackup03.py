""" trigger/02000076_tw_henesysvillage/01_npcbackup03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[1001], questIds=[10002041], questStates=[1]):
            return 지원군생성(self.ctx)


class 지원군생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_13')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=3003, spawnIds=[103]):
            return 지원군이동(self.ctx)


class 지원군이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_103')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=2001, spawnIds=[103]):
            return 지원군소멸(self.ctx)


class 지원군소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[103])
        self.set_timer(timerId='2', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 대기(self.ctx)


initial_state = 대기
