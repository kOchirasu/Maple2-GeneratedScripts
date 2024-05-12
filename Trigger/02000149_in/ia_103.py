""" trigger/02000149_in/ia_103.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000192], state=1)
        self.set_actor(trigger_id=203, visible=True, initial_sequence='Sit_Chair_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000192], state=0):
            return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(trigger_id=203, visible=False, initial_sequence='Sit_Chair_Idle_A')
        self.spawn_monster(spawn_ids=[403])


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=403, patrol_name='MS2PatrolData_503')
        self.set_dialogue(type=1, spawn_id=403, script='$02000149_IN__IA_103__0$', time=2, arg5=0)
        self.set_dialogue(type=1, spawn_id=403, script='$02000149_IN__IA_103__1$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=603, spawn_ids=[403]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[403])
        self.set_timer(timer_id='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
