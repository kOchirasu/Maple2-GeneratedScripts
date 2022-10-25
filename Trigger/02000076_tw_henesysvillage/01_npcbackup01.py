""" trigger/02000076_tw_henesysvillage/01_npcbackup01.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[1001], questIds=[10002041], questStates=[1]):
            return 지원군생성(self.ctx)


class 지원군생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_11')
        self.set_conversation(type=1, spawnId=101, script='$02000076_TW_HenesysVillage__01_NPCBACKUP01__0$', arg4=1)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=3001, spawnIds=[101]):
            return 지원군이동(self.ctx)


class 지원군이동(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=2001, spawnIds=[101]):
            return 지원군소멸(self.ctx)


class 지원군소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.set_timer(timerId='1', seconds=60)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
