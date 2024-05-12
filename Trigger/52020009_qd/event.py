""" trigger/52020009_qd/event.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5201], visible=False)
        self.set_effect(triggerIds=[5202], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2003]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101], animationEffect=True) # 이름 없는 유령
        self.set_effect(triggerIds=[5201], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Walk(self.ctx)


class Walk(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Event_Ready_01(self.ctx)


class Event_Ready_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10001267], state=1)
        self.set_interact_object(triggerIds=[10001268], state=1)
        self.set_interact_object(triggerIds=[10001269], state=1)
        self.add_balloon_talk(spawnId=101, msg='이름... 내 이름이 기억나지 않아...', duration=2800, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001267], stateValue=0):
            return Event_A(self.ctx)
        if self.object_interacted(interactIds=[10001268], stateValue=0):
            return Event_B(self.ctx)
        if self.object_interacted(interactIds=[10001269], stateValue=0):
            return Event_C(self.ctx)
        if self.wait_tick(waitTick=4000):
            return Event_Ready_02(self.ctx)


class Event_Ready_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawnId=101, msg='누가 내 이름 좀 찾아줘!', duration=2800, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001267], stateValue=0):
            return Event_A(self.ctx)
        if self.object_interacted(interactIds=[10001268], stateValue=0):
            return Event_B(self.ctx)
        if self.object_interacted(interactIds=[10001269], stateValue=0):
            return Event_C(self.ctx)
        if self.wait_tick(waitTick=4000):
            return Event_Ready_01(self.ctx)


class Event_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawnId=101, msg='아니야! 그건 내 이름이 적힌 책이 아니라고!', duration=2800, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_A_End(self.ctx)


class Event_A_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawnId=101, msg='그건 왕의 비밀병기와 관련된 책이란 말이야!', duration=2800, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Event_Ready_01(self.ctx)


class Event_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawnId=101, msg='$map:02020010$의 거대 병기?', duration=2800, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_B_End(self.ctx)


class Event_B_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawnId=101, msg='그런 책에 내 이름이 적혀 있을 리가 없잖아!', duration=2800, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Event_Ready_01(self.ctx)


class Event_C(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawnId=101, msg='그 책은! 내 일기장!', duration=2800, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Event_C_End(self.ctx)


class Event_C_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawnId=101, msg='그래... 기억났다. 내 이름...', duration=2800, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return New_Event(self.ctx)


class New_Event(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5202], visible=True)
        self.change_monster(removeSpawnId=101, addSpawnId=102)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Event_D(self.ctx)


class Event_D(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawnId=102, msg='내 이름은 $npcName:11003602$.', duration=2800, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_D_End(self.ctx)


class Event_D_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10001267], state=0)
        self.set_interact_object(triggerIds=[10001268], state=0)
        self.set_interact_object(triggerIds=[10001269], state=0)
        self.add_balloon_talk(spawnId=102, msg='크리티아스의 관찰자.', duration=2800, delayTick=0)


initial_state = Idle
