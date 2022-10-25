""" trigger/02000320_bf/wakeup_04.xml """
import common


class 자는중(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4001, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=4002, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=4003, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=4004, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=4005, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=4006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 도둑듬(self.ctx)


class 도둑듬(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000329], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000329], stateValue=0):
            return 깨어남1(self.ctx)


class 깨어남1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=8)
        self.set_actor(triggerId=4001, visible=True, initialSequence='Bore_A')
        self.set_actor(triggerId=4002, visible=True, initialSequence='Bore_A')
        self.set_actor(triggerId=4004, visible=False, initialSequence='Bore_A')
        self.set_actor(triggerId=4005, visible=False, initialSequence='Stun_A')
        self.set_actor(triggerId=4006, visible=False, initialSequence='Stun_A')
        self.create_monster(spawnIds=[40004], animationEffect=True)
        self.set_conversation(type=1, spawnId=40004, script='$02000320_BF__WAKEUP_04__0$', arg4=2, arg5=0)
        self.create_monster(spawnIds=[40005], animationEffect=True)
        self.set_conversation(type=1, spawnId=40005, script='$02000320_BF__WAKEUP_04__1$', arg4=2, arg5=1)
        self.create_monster(spawnIds=[40006], animationEffect=True)
        self.set_conversation(type=1, spawnId=40006, script='$02000320_BF__WAKEUP_04__2$', arg4=2, arg5=2)
        self.create_monster(spawnIds=[40001])
        self.create_monster(spawnIds=[40002])
        self.create_monster(spawnIds=[40003])
        self.set_conversation(type=1, spawnId=40003, script='$02000320_BF__WAKEUP_04__3$', arg4=2, arg5=3)
        self.set_conversation(type=1, spawnId=40001, script='$02000320_BF__WAKEUP_04__4$', arg4=2, arg5=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10'):
            return 깨어남2(self.ctx)


class 깨어남2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='11', seconds=4)
        self.set_conversation(type=1, spawnId=40002, script='$02000320_BF__WAKEUP_04__5$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=40001, script='$02000320_BF__WAKEUP_04__6$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=40003, script='$02000320_BF__WAKEUP_04__7$', arg4=2, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='11'):
            return 깨어남3(self.ctx)


class 깨어남3(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='12', seconds=1)
        self.set_actor(triggerId=4001, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=4002, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='12'):
            return 깨어남4(self.ctx)


class 깨어남4(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[40004,40005,40006]):
            return 다시잠듬(self.ctx)
        if not self.monster_in_combat(boxIds=[40004,40005,40006]):
            return 다시자러감(self.ctx)


class 다시자러감(common.Trigger):
    def on_enter(self):
        self.remove_balloon_talk(spawnId=40004)
        self.remove_balloon_talk(spawnId=40005)
        self.remove_balloon_talk(spawnId=40006)
        self.remove_balloon_talk(spawnId=40001)
        self.remove_balloon_talk(spawnId=40002)
        self.remove_balloon_talk(spawnId=40003)
        self.set_timer(timerId='14', seconds=4)
        self.set_conversation(type=1, spawnId=40004, script='$02000320_BF__WAKEUP_04__8$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=40005, script='$02000320_BF__WAKEUP_04__9$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=40006, script='$02000320_BF__WAKEUP_04__10$', arg4=2, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='14'):
            return 다시잠듬(self.ctx)


class 다시잠듬(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[40001,40002,40003,40004,40005,40006])
        self.set_timer(timerId='15', seconds=7)
        self.set_actor(triggerId=4004, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=4005, visible=True, initialSequence='Stun_A')
        self.set_actor(triggerId=4006, visible=True, initialSequence='Stun_A')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='15'):
            return 도둑듬(self.ctx)


initial_state = 자는중
