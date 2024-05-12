""" trigger/02000471_bf/magic_01.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2040315, key='10002019clear', value=0)
        self.set_user_value(trigger_id=2040316, key='10002019clear', value=0)
        self.set_user_value(trigger_id=2040317, key='10002019clear', value=0)
        self.set_user_value(trigger_id=2040322, key='10002019clear', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002019], state=0):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7001], visible=False)
        self.set_mesh(trigger_ids=[1101], visible=False, start_delay=0, interval=200, fade=15)
        self.set_mesh(trigger_ids=[1201], visible=True, start_delay=0, interval=200, fade=15)
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.add_buff(box_ids=[201], skill_id=70002001, level=1, is_player=True, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[201]):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=2040315, key='10002019clear', value=1)
        self.set_user_value(trigger_id=2040316, key='10002019clear', value=1)
        self.set_user_value(trigger_id=2040317, key='10002019clear', value=1)
        self.set_user_value(trigger_id=2040322, key='10002019clear', value=1)
        self.set_achievement(trigger_id=711, type='trigger', achieve='Hauntedmansion')
        self.spawn_monster(spawn_ids=[161,162,163], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Event_01_b(self.ctx)


class Event_01_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=161, sequence_name='Bore_A')
        self.set_npc_emotion_sequence(spawn_id=162, sequence_name='Bore_A')
        self.set_npc_emotion_sequence(spawn_id=163, sequence_name='Bore_A')
        self.set_dialogue(type=1, spawn_id=161, script='$02000471_BF__MAGIC_01__0$', time=3, arg5=2)
        self.set_dialogue(type=1, spawn_id=162, script='$02000471_BF__MAGIC_01__1$', time=3, arg5=4)
        self.set_dialogue(type=1, spawn_id=163, script='$02000471_BF__MAGIC_01__2$', time=3, arg5=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return Event_01_c(self.ctx)


class Event_01_c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[161,162,163])


initial_state = idle
