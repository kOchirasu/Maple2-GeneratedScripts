""" trigger/52100041_qd/magic_05.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002076], state=0):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7005], visible=False)
        self.set_mesh(trigger_ids=[1105], visible=False, start_delay=0, interval=200, fade=15)
        self.set_mesh(trigger_ids=[1205], visible=True, start_delay=0, interval=200, fade=15)
        self.spawn_monster(spawn_ids=[205], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[205]):
            return Event_05(self.ctx)


class Event_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_achievement(trigger_id=715, type='trigger', achieve='Hauntedmansion')
        self.spawn_monster(spawn_ids=[145,146,147], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Event_05_b(self.ctx)


class Event_05_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=147, patrol_name='MS2PatrolData_2136')
        self.set_dialogue(type=1, spawn_id=147, script='$52100041_QD__MAGIC_05__0$', time=2, arg5=2)
        self.set_dialogue(type=1, spawn_id=145, script='$52100041_QD__MAGIC_05__1$', time=3, arg5=4)
        self.set_dialogue(type=1, spawn_id=146, script='$52100041_QD__MAGIC_05__1$', time=3, arg5=5)
        self.set_dialogue(type=1, spawn_id=147, script='$52100041_QD__MAGIC_05__3$', time=3, arg5=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Event_05_c(self.ctx)


class Event_05_c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[148], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Event_05_d(self.ctx)


class Event_05_d(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=148, patrol_name='MS2PatrolData_2137')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_05_e(self.ctx)


class Event_05_e(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[145,146,147])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_05_f(self.ctx)


class Event_05_f(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[148])


initial_state = idle
