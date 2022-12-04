""" trigger/02000320_bf/wakeup_03.xml """
import trigger_api


class 자는중(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3001, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=3002, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=3003, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=3004, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=3005, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=3006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 도둑듬(self.ctx)


class 도둑듬(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000317], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000317], stateValue=0):
            return 깨어남1(self.ctx)


class 깨어남1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=8)
        self.set_actor(triggerId=3001, visible=True, initialSequence='Bore_A')
        self.set_actor(triggerId=3002, visible=True, initialSequence='Bore_A')
        self.set_actor(triggerId=3004, visible=False, initialSequence='Bore_A')
        self.set_actor(triggerId=3005, visible=False, initialSequence='Stun_A')
        self.set_actor(triggerId=3006, visible=False, initialSequence='Stun_A')
        self.create_monster(spawnIds=[30004], animationEffect=True)
        self.set_conversation(type=1, spawnId=30004, script='$02000320_BF__WAKEUP_03__0$', arg4=2, arg5=0)
        self.create_monster(spawnIds=[30005], animationEffect=True)
        self.set_conversation(type=1, spawnId=30005, script='$02000320_BF__WAKEUP_03__1$', arg4=2, arg5=1)
        self.create_monster(spawnIds=[30006], animationEffect=True)
        self.set_conversation(type=1, spawnId=30006, script='$02000320_BF__WAKEUP_03__2$', arg4=2, arg5=2)
        self.create_monster(spawnIds=[30001])
        self.create_monster(spawnIds=[30002])
        self.create_monster(spawnIds=[30003])
        self.set_conversation(type=1, spawnId=30003, script='$02000320_BF__WAKEUP_03__3$', arg4=2, arg5=3)
        self.set_conversation(type=1, spawnId=30001, script='$02000320_BF__WAKEUP_03__4$', arg4=2, arg5=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 깨어남2(self.ctx)


class 깨어남2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='11', seconds=4)
        self.set_conversation(type=1, spawnId=30002, script='$02000320_BF__WAKEUP_03__5$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=30001, script='$02000320_BF__WAKEUP_03__6$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=30003, script='$02000320_BF__WAKEUP_03__7$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='11'):
            return 깨어남3(self.ctx)


class 깨어남3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='12', seconds=1)
        self.set_actor(triggerId=3001, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=3002, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='12'):
            return 깨어남4(self.ctx)


class 깨어남4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[30004,30005,30006]):
            return 다시잠듬(self.ctx)
        if not self.monster_in_combat(boxIds=[30004,30005,30006]):
            return 다시자러감(self.ctx)


class 다시자러감(trigger_api.Trigger):
    def on_enter(self):
        self.remove_balloon_talk(spawnId=30004)
        self.remove_balloon_talk(spawnId=30005)
        self.remove_balloon_talk(spawnId=30006)
        self.remove_balloon_talk(spawnId=30001)
        self.remove_balloon_talk(spawnId=30002)
        self.remove_balloon_talk(spawnId=30003)
        self.set_timer(timerId='14', seconds=4)
        self.set_conversation(type=1, spawnId=30004, script='$02000320_BF__WAKEUP_03__8$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=30005, script='$02000320_BF__WAKEUP_03__9$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=30006, script='$02000320_BF__WAKEUP_03__10$', arg4=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='14'):
            return 다시잠듬(self.ctx)


class 다시잠듬(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[30001,30002,30003,30004,30005,30006])
        self.set_timer(timerId='15', seconds=7)
        self.set_actor(triggerId=3004, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=3005, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=3006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='15'):
            return 도둑듬(self.ctx)


initial_state = 자는중
