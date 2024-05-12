""" trigger/02000076_tw_henesysvillage/01_npcbackup07.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[1001], quest_ids=[10002041], quest_states=[1]):
            return 지원군생성(self.ctx)


class 지원군생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[107], auto_target=False)
        self.move_npc(spawn_id=107, patrol_name='MS2PatrolData_17')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=3007, spawn_ids=[107]):
            return 지원군이동(self.ctx)


class 지원군이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=104, script='$02000076_TW_HenesysVillage__01_NPCBACKUP07__0$', time=1)
        self.move_npc(spawn_id=107, patrol_name='MS2PatrolData_107')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=2001, spawn_ids=[107]):
            return 지원군소멸(self.ctx)


class 지원군소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[107])
        self.set_timer(timer_id='3', seconds=90)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 대기(self.ctx)


initial_state = 대기
