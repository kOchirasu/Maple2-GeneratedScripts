""" trigger/02000320_bf/wakeup_04.xml """
import trigger_api


class 자는중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=4003, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=4004, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=4005, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=4006, visible=True, initial_sequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 도둑듬(self.ctx)


class 도둑듬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000329], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000329], state=0):
            return 깨어남1(self.ctx)


class 깨어남1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=8)
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='Bore_A')
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Bore_A')
        self.set_actor(trigger_id=4004, initial_sequence='Bore_A')
        self.set_actor(trigger_id=4005, initial_sequence='Stun_A')
        self.set_actor(trigger_id=4006, initial_sequence='Stun_A')
        self.spawn_monster(spawn_ids=[40004])
        self.set_dialogue(type=1, spawn_id=40004, script='$02000320_BF__WAKEUP_04__0$', time=2)
        self.spawn_monster(spawn_ids=[40005])
        self.set_dialogue(type=1, spawn_id=40005, script='$02000320_BF__WAKEUP_04__1$', time=2, arg5=1)
        self.spawn_monster(spawn_ids=[40006])
        self.set_dialogue(type=1, spawn_id=40006, script='$02000320_BF__WAKEUP_04__2$', time=2, arg5=2)
        self.spawn_monster(spawn_ids=[40001])
        self.spawn_monster(spawn_ids=[40002])
        self.spawn_monster(spawn_ids=[40003])
        self.set_dialogue(type=1, spawn_id=40003, script='$02000320_BF__WAKEUP_04__3$', time=2, arg5=3)
        self.set_dialogue(type=1, spawn_id=40001, script='$02000320_BF__WAKEUP_04__4$', time=2, arg5=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 깨어남2(self.ctx)


class 깨어남2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=4)
        self.set_dialogue(type=1, spawn_id=40002, script='$02000320_BF__WAKEUP_04__5$', time=2)
        self.set_dialogue(type=1, spawn_id=40001, script='$02000320_BF__WAKEUP_04__6$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=40003, script='$02000320_BF__WAKEUP_04__7$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 깨어남3(self.ctx)


class 깨어남3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=1)
        self.set_actor(trigger_id=4001, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 깨어남4(self.ctx)


class 깨어남4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[40004,40005,40006]):
            return 다시잠듬(self.ctx)
        if not self.monster_in_combat(spawn_ids=[40004,40005,40006]):
            return 다시자러감(self.ctx)


class 다시자러감(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_balloon_talk(spawn_id=40004)
        self.remove_balloon_talk(spawn_id=40005)
        self.remove_balloon_talk(spawn_id=40006)
        self.remove_balloon_talk(spawn_id=40001)
        self.remove_balloon_talk(spawn_id=40002)
        self.remove_balloon_talk(spawn_id=40003)
        self.set_timer(timer_id='14', seconds=4)
        self.set_dialogue(type=1, spawn_id=40004, script='$02000320_BF__WAKEUP_04__8$', time=2)
        self.set_dialogue(type=1, spawn_id=40005, script='$02000320_BF__WAKEUP_04__9$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=40006, script='$02000320_BF__WAKEUP_04__10$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='14'):
            return 다시잠듬(self.ctx)


class 다시잠듬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[40001,40002,40003,40004,40005,40006])
        self.set_timer(timer_id='15', seconds=7)
        self.set_actor(trigger_id=4004, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=4005, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=4006, visible=True, initial_sequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 도둑듬(self.ctx)


initial_state = 자는중
