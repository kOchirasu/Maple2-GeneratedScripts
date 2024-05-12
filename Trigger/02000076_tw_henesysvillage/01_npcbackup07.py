""" trigger/02000076_tw_henesysvillage/01_npcbackup07.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[1001], questIds=[10002041], questStates=[1]):
            return 지원군생성(self.ctx)


class 지원군생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.move_npc(spawnId=107, patrolName='MS2PatrolData_17')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=3007, spawnIds=[107]):
            return 지원군이동(self.ctx)


class 지원군이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=104, script='$02000076_TW_HenesysVillage__01_NPCBACKUP07__0$', arg4=1)
        self.move_npc(spawnId=107, patrolName='MS2PatrolData_107')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=2001, spawnIds=[107]):
            return 지원군소멸(self.ctx)


class 지원군소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[107])
        self.set_timer(timerId='3', seconds=90)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 대기(self.ctx)


initial_state = 대기
