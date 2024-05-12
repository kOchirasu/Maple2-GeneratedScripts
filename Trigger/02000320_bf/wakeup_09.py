""" trigger/02000320_bf/wakeup_09.xml """
import trigger_api


class 자는중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=9001, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=9002, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=9003, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=9004, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=9005, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=9006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 도둑듬(self.ctx)


class 도둑듬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000353], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000353], stateValue=0):
            return 깨어남1(self.ctx)


class 깨어남1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='10', seconds=8)
        self.set_actor(triggerId=9001, visible=True, initialSequence='Bore_A')
        self.set_actor(triggerId=9002, visible=True, initialSequence='Bore_A')
        self.set_actor(triggerId=9004, visible=False, initialSequence='Bore_A')
        self.set_actor(triggerId=9005, visible=False, initialSequence='Stun_A')
        self.set_actor(triggerId=9006, visible=False, initialSequence='Stun_A')
        self.create_monster(spawnIds=[90004], animationEffect=True)
        self.set_conversation(type=1, spawnId=90004, script='$02000320_BF__WAKEUP_09__0$', arg4=2, arg5=0)
        self.create_monster(spawnIds=[90005], animationEffect=True)
        self.set_conversation(type=1, spawnId=90005, script='$02000320_BF__WAKEUP_09__1$', arg4=2, arg5=1)
        self.create_monster(spawnIds=[90006], animationEffect=True)
        self.set_conversation(type=1, spawnId=90006, script='$02000320_BF__WAKEUP_09__2$', arg4=2, arg5=2)
        self.create_monster(spawnIds=[90001])
        self.create_monster(spawnIds=[90002])
        self.create_monster(spawnIds=[90003])
        self.set_conversation(type=1, spawnId=90003, script='$02000320_BF__WAKEUP_09__3$', arg4=2, arg5=3)
        self.set_conversation(type=1, spawnId=90001, script='$02000320_BF__WAKEUP_09__4$', arg4=2, arg5=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 깨어남2(self.ctx)


class 깨어남2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='11', seconds=4)
        self.set_conversation(type=1, spawnId=90002, script='$02000320_BF__WAKEUP_09__5$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=90001, script='$02000320_BF__WAKEUP_09__6$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=90003, script='$02000320_BF__WAKEUP_09__7$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='11'):
            return 깨어남3(self.ctx)


class 깨어남3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='12', seconds=1)
        self.set_actor(triggerId=9001, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=9002, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='12'):
            return 깨어남4(self.ctx)


class 깨어남4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[90004,90005,90006]):
            return 다시잠듬(self.ctx)
        if not self.monster_in_combat(boxIds=[90004,90005,90006]):
            return 다시자러감(self.ctx)


class 다시자러감(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_balloon_talk(spawnId=90004)
        self.remove_balloon_talk(spawnId=90005)
        self.remove_balloon_talk(spawnId=90006)
        self.remove_balloon_talk(spawnId=90001)
        self.remove_balloon_talk(spawnId=90002)
        self.remove_balloon_talk(spawnId=90003)
        self.set_timer(timerId='14', seconds=4)
        self.set_conversation(type=1, spawnId=90004, script='$02000320_BF__WAKEUP_09__8$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=90005, script='$02000320_BF__WAKEUP_09__9$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=90006, script='$02000320_BF__WAKEUP_09__10$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='14'):
            return 다시잠듬(self.ctx)


class 다시잠듬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[90001,90002,90003,90004,90005,90006])
        self.set_timer(timerId='15', seconds=7)
        self.set_actor(triggerId=9004, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=9005, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=9006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='15'):
            return 도둑듬(self.ctx)


initial_state = 자는중
