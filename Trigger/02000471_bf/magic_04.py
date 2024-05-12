""" trigger/02000471_bf/magic_04.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2040315, key='10002022clear', value=0)
        self.set_user_value(trigger_id=2040319, key='10002022clear', value=0)
        self.set_user_value(trigger_id=2040322, key='10002022clear', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002022], state=0):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7004], visible=False)
        self.set_mesh(trigger_ids=[1104], visible=False, start_delay=0, interval=200, fade=15)
        self.set_mesh(trigger_ids=[1204], visible=True, start_delay=0, interval=200, fade=15)
        self.spawn_monster(spawn_ids=[204], auto_target=False)
        self.add_buff(box_ids=[204], skill_id=70002031, level=1, is_player=True, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[204]):
            return Event_04(self.ctx)


class Event_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2040315, key='10002022clear', value=1)
        self.set_user_value(trigger_id=2040319, key='10002022clear', value=1)
        self.set_user_value(trigger_id=2040322, key='10002022clear', value=1)
        self.set_achievement(trigger_id=714, type='trigger', achieve='Hauntedmansion')
        self.spawn_monster(spawn_ids=[144], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Event_04_b(self.ctx)


class Event_04_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=144, script='$02000471_BF__MAGIC_04__0$', time=2, arg5=2)
        self.set_dialogue(type=1, spawn_id=144, script='$02000471_BF__MAGIC_04__1$', time=4, arg5=5)
        self.move_npc(spawn_id=144, patrol_name='MS2PatrolData_2134')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Event_04_c(self.ctx)


class Event_04_c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=144, script='$02000471_BF__MAGIC_04__2$', time=3, arg5=1)
        self.set_dialogue(type=1, spawn_id=144, script='$02000471_BF__MAGIC_04__3$', time=3, arg5=4)
        self.move_npc(spawn_id=144, patrol_name='MS2PatrolData_2135')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return Event_04_d(self.ctx)


class Event_04_d(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[144])


initial_state = idle
