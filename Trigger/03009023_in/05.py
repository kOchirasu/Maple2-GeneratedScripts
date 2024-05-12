""" trigger/03009023_in/05.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000237], state=1)
        self.spawn_monster(spawn_ids=[105], auto_target=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000237], state=0):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=8)
        self.destroy_monster(spawn_ids=[105])
        self.spawn_monster(spawn_ids=[205], auto_target=True)
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_205')
        self.set_dialogue(type=1, spawn_id=205, script='$03009023_IN__05__0$', time=4, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[205])
        self.set_timer(timer_id='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
