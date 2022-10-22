""" trigger/52020010_qd/clock_b.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)
        set_effect(triggerIds=[5005], visible=False)
        set_effect(triggerIds=[5006], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2003]):
            return Ready()


class Ready(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001272], arg2=0):
            return Event_Start()


class Event_Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5003], visible=True)
        create_monster(spawnIds=[201], arg2=True) # 아빠 유령
        create_monster(spawnIds=[202], arg2=True) # 엄마 유령
        create_monster(spawnIds=[203], arg2=True) # 애기 유령

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Event_01()


class Event_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5004], visible=True)
        move_npc(spawnId=203, patrolName='MS2PatrolData_3001')
        add_balloon_talk(spawnId=203, msg='와! 쾅쾅한다!', duration=2500, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_02()


class Event_02(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=202, msg='여보... 우리 어쩌면 좋아요?', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_03()


class Event_03(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=201, msg='일이 이렇게 되어버릴 줄은...', duration=2800, delayTick=0)
        add_balloon_talk(spawnId=202, msg='우리 도망 못가는거죠?', duration=2800, delayTick=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_04()


class Event_04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5005], visible=True)
        add_balloon_talk(spawnId=203, msg='쾅쾅! 쾅쾅!', duration=2000, delayTick=0)
        add_balloon_talk(spawnId=201, msg='난 대체 무얼 위해...', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_05()


class Event_05(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=202, msg='여보!', duration=2800, delayTick=0)
        add_balloon_talk(spawnId=201, msg='!!!', duration=2000, delayTick=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_06()


class Event_06(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=201, msg='여보, 내 딸... 모두 미안하오...', duration=2000, delayTick=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_07()


class Event_07(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5006], visible=True)
        add_balloon_talk(spawnId=202, msg='여보...', duration=2000, delayTick=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Event_End()


class Event_End(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)
        set_effect(triggerIds=[5005], visible=False)
        set_effect(triggerIds=[5006], visible=False)
        destroy_monster(spawnIds=[201])
        destroy_monster(spawnIds=[202])
        destroy_monster(spawnIds=[203])


