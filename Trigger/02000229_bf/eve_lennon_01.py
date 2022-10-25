""" trigger/02000229_bf/eve_lennon_01.xml """
import common


class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[101], questIds=[10002180], questStates=[1]):
            return NPC이동(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[1001])


class NPC이동(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1001, patrolName='Patrol_1001')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[1001]):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1001])
        self.set_timer(timerId='1', seconds=20)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
