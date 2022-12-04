""" trigger/02000076_tw_henesysvillage/01_npcbackup04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[1001], questIds=[10002041], questStates=[1]):
            return 지원군생성(self.ctx)


class 지원군생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_14')
        self.set_conversation(type=1, spawnId=104, script='$02000076_TW_HenesysVillage__01_NPCBACKUP04__0$', arg4=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=3004, spawnIds=[104]):
            return 지원군이동(self.ctx)


class 지원군이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_104')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=2001, spawnIds=[104]):
            return 지원군소멸(self.ctx)


class 지원군소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[104])
        self.set_timer(timerId='4', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 대기(self.ctx)


initial_state = 대기
