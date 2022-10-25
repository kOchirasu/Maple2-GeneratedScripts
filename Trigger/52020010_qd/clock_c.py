""" trigger/52020010_qd/clock_c.xml """
import common


class Idle(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5007], visible=False)
        self.set_effect(triggerIds=[5008], visible=False)
        self.set_effect(triggerIds=[5009], visible=False)
        self.set_effect(triggerIds=[5010], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[2004]):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001273], stateValue=0):
            return Event_Start(self.ctx)


class Event_Start(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5007], visible=True)
        self.create_monster(spawnIds=[301], animationEffect=True) # 엄마 유령
        self.create_monster(spawnIds=[302], animationEffect=True) # 애기 유령

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return Event_01(self.ctx)


class Event_01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5008], visible=True)
        self.set_npc_emotion_loop(spawnId=302, sequenceName='Bore_B', duration=18000)
        self.add_balloon_talk(spawnId=302, msg='엄마 무서워...', duration=2800, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_02(self.ctx)


class Event_02(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=301, msg='울지마렴... 조금 있으면 괜찮아 질거야...', duration=2800, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_03(self.ctx)


class Event_03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5009], visible=True)
        self.add_balloon_talk(spawnId=301, msg='여보? 어디 간 거에요!', duration=2800, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_04(self.ctx)


class Event_04(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5010], visible=True)
        self.add_balloon_talk(spawnId=301, msg='여보!!!', duration=2800, delayTick=1000)
        self.add_balloon_talk(spawnId=302, msg='엄마... 아빠... 무서워...', duration=2800, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Event_End(self.ctx)


class Event_End(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5007], visible=False)
        self.set_effect(triggerIds=[5008], visible=False)
        self.set_effect(triggerIds=[5009], visible=False)
        self.set_effect(triggerIds=[5010], visible=False)
        self.destroy_monster(spawnIds=[301])
        self.destroy_monster(spawnIds=[302])


initial_state = Idle
