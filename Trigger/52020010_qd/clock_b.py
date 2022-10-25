""" trigger/52020010_qd/clock_b.xml """
import common


class Idle(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_effect(triggerIds=[5006], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[2003]):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001272], stateValue=0):
            return Event_Start(self.ctx)


class Event_Start(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5003], visible=True)
        self.create_monster(spawnIds=[201], animationEffect=True) # 아빠 유령
        self.create_monster(spawnIds=[202], animationEffect=True) # 엄마 유령
        self.create_monster(spawnIds=[203], animationEffect=True) # 애기 유령

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Event_01(self.ctx)


class Event_01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5004], visible=True)
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_3001')
        self.add_balloon_talk(spawnId=203, msg='와! 쾅쾅한다!', duration=2500, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_02(self.ctx)


class Event_02(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=202, msg='여보... 우리 어쩌면 좋아요?', duration=2800, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_03(self.ctx)


class Event_03(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=201, msg='일이 이렇게 되어버릴 줄은...', duration=2800, delayTick=0)
        self.add_balloon_talk(spawnId=202, msg='우리 도망 못가는거죠?', duration=2800, delayTick=1000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_04(self.ctx)


class Event_04(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5005], visible=True)
        self.add_balloon_talk(spawnId=203, msg='쾅쾅! 쾅쾅!', duration=2000, delayTick=0)
        self.add_balloon_talk(spawnId=201, msg='난 대체 무얼 위해...', duration=2800, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_05(self.ctx)


class Event_05(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=202, msg='여보!', duration=2800, delayTick=0)
        self.add_balloon_talk(spawnId=201, msg='!!!', duration=2000, delayTick=1000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_06(self.ctx)


class Event_06(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=201, msg='여보, 내 딸... 모두 미안하오...', duration=2000, delayTick=1000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_07(self.ctx)


class Event_07(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5006], visible=True)
        self.add_balloon_talk(spawnId=202, msg='여보...', duration=2000, delayTick=1000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Event_End(self.ctx)


class Event_End(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_effect(triggerIds=[5006], visible=False)
        self.destroy_monster(spawnIds=[201])
        self.destroy_monster(spawnIds=[202])
        self.destroy_monster(spawnIds=[203])


initial_state = Idle
