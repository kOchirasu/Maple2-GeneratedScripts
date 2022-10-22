""" trigger/52020010_qd/clock_d.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5011], visible=False)
        set_effect(triggerIds=[5012], visible=False)
        set_effect(triggerIds=[5013], visible=False)
        set_effect(triggerIds=[5014], visible=False)
        set_effect(triggerIds=[5015], visible=False)
        set_interact_object(triggerIds=[10001275], state=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2005], questIds=[60200050], questStates=[1]):
            return Ready()
        if quest_user_detected(boxIds=[2005], questIds=[60200050], questStates=[2]):
            return Ready_A()
        if quest_user_detected(boxIds=[2005], questIds=[60200050], questStates=[3]):
            return Ready_A()


class Ready(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001275], state=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001274], arg2=0):
            return Event_Start()


class Event_Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5011], visible=True)
        set_effect(triggerIds=[5012], visible=True)
        create_monster(spawnIds=[401], arg2=True) # 아빠 유령

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return Event_01()


class Event_01(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=401, msg='대체 어디 있는거야?', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_02()


class Event_02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5013], visible=True)
        move_npc(spawnId=401, patrolName='MS2PatrolData_3002')
        add_balloon_talk(spawnId=401, msg='분명히 책장 어딘가에 장치가 있었는데...', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_03()


class Event_03(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=401, msg='어째서 이럴 때 기억나지 않는거야!!!', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_04()


class Event_04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5014], visible=True)
        add_balloon_talk(spawnId=401, msg='여기였나?', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_05()


class Event_05(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=401, msg='아니... 생각해보니 소용 없군...', duration=2800, delayTick=0)
        set_interact_object(triggerIds=[10001275], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_06()


class Event_06(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5015], visible=True)
        add_balloon_talk(spawnId=401, msg='어차피 거스를 수 없는 운명인 것을...', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Event_End()


class Event_End(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5011], visible=False)
        set_effect(triggerIds=[5012], visible=False)
        set_effect(triggerIds=[5013], visible=False)
        set_effect(triggerIds=[5014], visible=False)
        set_effect(triggerIds=[5015], visible=False)
        destroy_monster(spawnIds=[401])


#  시간을 돌려라 퀘스트 가능 상태 이후 
class Ready_A(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001275], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001274], arg2=0):
            return Event_Start_A()


class Event_Start_A(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5011], visible=True)
        set_effect(triggerIds=[5012], visible=True)
        create_monster(spawnIds=[401], arg2=True) # 아빠 유령

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return Event_01_A()


class Event_01_A(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=401, msg='대체 어디 있는거야?', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_02_A()


class Event_02_A(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5013], visible=True)
        move_npc(spawnId=401, patrolName='MS2PatrolData_3002')
        add_balloon_talk(spawnId=401, msg='분명히 책장 어딘가에 장치가 있었는데...', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_03_A()


class Event_03_A(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=401, msg='어째서 이럴 때 기억나지 않는거야!!!', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_04_A()


class Event_04_A(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5014], visible=True)
        add_balloon_talk(spawnId=401, msg='여기였나?', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_05_A()


class Event_05_A(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=401, msg='아니... 생각해보니 소용 없군...', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_06_A()


class Event_06_A(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5015], visible=True)
        add_balloon_talk(spawnId=401, msg='어차피 거스를 수 없는 운명인 것을...', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Event_End_A()


class Event_End_A(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5011], visible=False)
        set_effect(triggerIds=[5012], visible=False)
        set_effect(triggerIds=[5013], visible=False)
        set_effect(triggerIds=[5014], visible=False)
        set_effect(triggerIds=[5015], visible=False)
        destroy_monster(spawnIds=[401])


