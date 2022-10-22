""" trigger/52020009_qd/event.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5201], visible=False)
        set_effect(triggerIds=[5202], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2003]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True) # 이름 없는 유령
        set_effect(triggerIds=[5201], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Walk()


class Walk(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_3001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Event_Ready_01()


class Event_Ready_01(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001267], state=1)
        set_interact_object(triggerIds=[10001268], state=1)
        set_interact_object(triggerIds=[10001269], state=1)
        add_balloon_talk(spawnId=101, msg='이름... 내 이름이 기억나지 않아...', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001267], arg2=0):
            return Event_A()
        if object_interacted(interactIds=[10001268], arg2=0):
            return Event_B()
        if object_interacted(interactIds=[10001269], arg2=0):
            return Event_C()
        if wait_tick(waitTick=4000):
            return Event_Ready_02()


class Event_Ready_02(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='누가 내 이름 좀 찾아줘!', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001267], arg2=0):
            return Event_A()
        if object_interacted(interactIds=[10001268], arg2=0):
            return Event_B()
        if object_interacted(interactIds=[10001269], arg2=0):
            return Event_C()
        if wait_tick(waitTick=4000):
            return Event_Ready_01()


class Event_A(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='아니야! 그건 내 이름이 적힌 책이 아니라고!', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_A_End()


class Event_A_End(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='그건 왕의 비밀병기와 관련된 책이란 말이야!', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Event_Ready_01()


class Event_B(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='$map:02020010$의 거대 병기?', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_B_End()


class Event_B_End(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='그런 책에 내 이름이 적혀 있을 리가 없잖아!', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Event_Ready_01()


class Event_C(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='그 책은! 내 일기장!', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Event_C_End()


class Event_C_End(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='그래... 기억났다. 내 이름...', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return New_Event()


class New_Event(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5202], visible=True)
        change_monster(removeSpawnId=101, addSpawnId=102)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Event_D()


class Event_D(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=102, msg='내 이름은 $npcName:11003602$.', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_D_End()


class Event_D_End(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001267], state=0)
        set_interact_object(triggerIds=[10001268], state=0)
        set_interact_object(triggerIds=[10001269], state=0)
        add_balloon_talk(spawnId=102, msg='크리티아스의 관찰자.', duration=2800, delayTick=0)


