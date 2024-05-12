""" trigger/02000076_tw_henesysvillage/02_npcbackup04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[1002], questIds=[10002041], questStates=[1]):
            return 지원군생성(self.ctx)


class 지원군생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[204], animationEffect=False)
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_24')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=4004, spawnIds=[204]):
            return 지원군이동(self.ctx)


class 지원군이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=204, script='$02000076_TW_HenesysVillage__02_NPCBACKUP04__0$', arg4=1)
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_204')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=2001, spawnIds=[204]):
            return 지원군소멸(self.ctx)


class 지원군소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[204])
        self.set_timer(timerId='1', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
