""" trigger/02000076_tw_henesysvillage/01_npcbackup08.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[1001], questIds=[10002041], questStates=[1]):
            return 지원군생성(self.ctx)


class 지원군생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.move_npc(spawnId=108, patrolName='MS2PatrolData_18')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=3008, spawnIds=[108]):
            return 지원군이동(self.ctx)


class 지원군이동(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=108, patrolName='MS2PatrolData_108')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=2001, spawnIds=[108]):
            return 지원군소멸(self.ctx)


class 지원군소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[108])
        self.set_timer(timerId='3', seconds=120)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 대기(self.ctx)


initial_state = 대기
