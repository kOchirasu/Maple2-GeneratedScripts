""" trigger/02000320_bf/wakeup_06.xml """
import common


class 자는중(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=6001, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=6002, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=6003, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=6004, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=6005, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=6006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 도둑듬(self.ctx)


class 도둑듬(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000350], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000350], stateValue=0):
            return 깨어남1(self.ctx)


class 깨어남1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=8)
        self.set_actor(triggerId=6001, visible=True, initialSequence='Bore_A')
        self.set_actor(triggerId=6002, visible=True, initialSequence='Bore_A')
        self.set_actor(triggerId=6004, visible=False, initialSequence='Bore_A')
        self.set_actor(triggerId=6005, visible=False, initialSequence='Stun_A')
        self.set_actor(triggerId=6006, visible=False, initialSequence='Stun_A')
        self.create_monster(spawnIds=[60004], animationEffect=True)
        self.set_conversation(type=1, spawnId=60004, script='$02000320_BF__WAKEUP_06__0$', arg4=2, arg5=0)
        self.create_monster(spawnIds=[60005], animationEffect=True)
        self.set_conversation(type=1, spawnId=60005, script='$02000320_BF__WAKEUP_06__1$', arg4=2, arg5=1)
        self.create_monster(spawnIds=[60006], animationEffect=True)
        self.set_conversation(type=1, spawnId=60006, script='$02000320_BF__WAKEUP_06__2$', arg4=2, arg5=2)
        self.create_monster(spawnIds=[60001])
        self.create_monster(spawnIds=[60002])
        self.create_monster(spawnIds=[60003])
        self.set_conversation(type=1, spawnId=60003, script='$02000320_BF__WAKEUP_06__3$', arg4=2, arg5=3)
        self.set_conversation(type=1, spawnId=60001, script='$02000320_BF__WAKEUP_06__4$', arg4=2, arg5=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10'):
            return 깨어남2(self.ctx)


class 깨어남2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='11', seconds=4)
        self.set_conversation(type=1, spawnId=60002, script='$02000320_BF__WAKEUP_06__5$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=60001, script='$02000320_BF__WAKEUP_06__6$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=60003, script='$02000320_BF__WAKEUP_06__7$', arg4=2, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='11'):
            return 깨어남3(self.ctx)


class 깨어남3(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='12', seconds=1)
        self.set_actor(triggerId=6001, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=6002, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='12'):
            return 깨어남4(self.ctx)


class 깨어남4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[60004,60005,60006]):
            return 다시잠듬(self.ctx)
        if not self.monster_in_combat(boxIds=[60004,60005,60006]):
            return 다시자러감(self.ctx)


class 다시자러감(common.Trigger):
    def on_enter(self):
        self.remove_balloon_talk(spawnId=60004)
        self.remove_balloon_talk(spawnId=60005)
        self.remove_balloon_talk(spawnId=60006)
        self.remove_balloon_talk(spawnId=60001)
        self.remove_balloon_talk(spawnId=60002)
        self.remove_balloon_talk(spawnId=60003)
        self.set_timer(timerId='14', seconds=4)
        self.set_conversation(type=1, spawnId=60004, script='$02000320_BF__WAKEUP_06__8$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=60005, script='$02000320_BF__WAKEUP_06__9$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=60006, script='$02000320_BF__WAKEUP_06__10$', arg4=2, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='14'):
            return 다시잠듬(self.ctx)


class 다시잠듬(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[60001,60002,60003,60004,60005,60006])
        self.set_timer(timerId='15', seconds=7)
        self.set_actor(triggerId=6004, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=6005, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=6006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='15'):
            return 도둑듬(self.ctx)


initial_state = 자는중
