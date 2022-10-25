""" trigger/52020010_qd/clock_d.xml """
import common


class Idle(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5011], visible=False)
        self.set_effect(triggerIds=[5012], visible=False)
        self.set_effect(triggerIds=[5013], visible=False)
        self.set_effect(triggerIds=[5014], visible=False)
        self.set_effect(triggerIds=[5015], visible=False)
        self.set_interact_object(triggerIds=[10001275], state=0)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2005], questIds=[60200050], questStates=[1]):
            return Ready(self.ctx)
        if self.quest_user_detected(boxIds=[2005], questIds=[60200050], questStates=[2]):
            return Ready_A(self.ctx)
        if self.quest_user_detected(boxIds=[2005], questIds=[60200050], questStates=[3]):
            return Ready_A(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001275], state=0)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001274], stateValue=0):
            return Event_Start(self.ctx)


class Event_Start(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5011], visible=True)
        self.set_effect(triggerIds=[5012], visible=True)
        self.create_monster(spawnIds=[401], animationEffect=True) # 아빠 유령

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return Event_01(self.ctx)


class Event_01(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=401, msg='대체 어디 있는거야?', duration=2800, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_02(self.ctx)


class Event_02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5013], visible=True)
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_3002')
        self.add_balloon_talk(spawnId=401, msg='분명히 책장 어딘가에 장치가 있었는데...', duration=2800, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_03(self.ctx)


class Event_03(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=401, msg='어째서 이럴 때 기억나지 않는거야!!!', duration=2800, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_04(self.ctx)


class Event_04(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5014], visible=True)
        self.add_balloon_talk(spawnId=401, msg='여기였나?', duration=2800, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_05(self.ctx)


class Event_05(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=401, msg='아니... 생각해보니 소용 없군...', duration=2800, delayTick=0)
        self.set_interact_object(triggerIds=[10001275], state=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_06(self.ctx)


class Event_06(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5015], visible=True)
        self.add_balloon_talk(spawnId=401, msg='어차피 거스를 수 없는 운명인 것을...', duration=2800, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Event_End(self.ctx)


class Event_End(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5011], visible=False)
        self.set_effect(triggerIds=[5012], visible=False)
        self.set_effect(triggerIds=[5013], visible=False)
        self.set_effect(triggerIds=[5014], visible=False)
        self.set_effect(triggerIds=[5015], visible=False)
        self.destroy_monster(spawnIds=[401])


# 시간을 돌려라 퀘스트 가능 상태 이후
class Ready_A(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001275], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001274], stateValue=0):
            return Event_Start_A(self.ctx)


class Event_Start_A(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5011], visible=True)
        self.set_effect(triggerIds=[5012], visible=True)
        self.create_monster(spawnIds=[401], animationEffect=True) # 아빠 유령

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return Event_01_A(self.ctx)


class Event_01_A(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=401, msg='대체 어디 있는거야?', duration=2800, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_02_A(self.ctx)


class Event_02_A(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5013], visible=True)
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_3002')
        self.add_balloon_talk(spawnId=401, msg='분명히 책장 어딘가에 장치가 있었는데...', duration=2800, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_03_A(self.ctx)


class Event_03_A(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=401, msg='어째서 이럴 때 기억나지 않는거야!!!', duration=2800, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_04_A(self.ctx)


class Event_04_A(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5014], visible=True)
        self.add_balloon_talk(spawnId=401, msg='여기였나?', duration=2800, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_05_A(self.ctx)


class Event_05_A(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=401, msg='아니... 생각해보니 소용 없군...', duration=2800, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_06_A(self.ctx)


class Event_06_A(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5015], visible=True)
        self.add_balloon_talk(spawnId=401, msg='어차피 거스를 수 없는 운명인 것을...', duration=2800, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Event_End_A(self.ctx)


class Event_End_A(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5011], visible=False)
        self.set_effect(triggerIds=[5012], visible=False)
        self.set_effect(triggerIds=[5013], visible=False)
        self.set_effect(triggerIds=[5014], visible=False)
        self.set_effect(triggerIds=[5015], visible=False)
        self.destroy_monster(spawnIds=[401])


initial_state = Idle
