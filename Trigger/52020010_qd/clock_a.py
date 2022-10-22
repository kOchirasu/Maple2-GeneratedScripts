""" trigger/52020010_qd/clock_a.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2002]):
            return Ready()


class Ready(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001271], arg2=0):
            return Event_Start()


class Event_Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True)
        create_monster(spawnIds=[101], arg2=True) # 아빠 유령
        create_monster(spawnIds=[102], arg2=True) # 애기 유령
        create_monster(spawnIds=[103], arg2=True) # 엄마 유령

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Event_01()


class Event_01(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=102, msg='엄마! 나 이 빵 먹어도 돼요?', duration=2500, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_02()


class Event_02(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=103, msg='안돼! 금방 밥먹을거야.', duration=2500, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_03()


class Event_03(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=102, msg='힝... 아빠 나 이거 먹으면 안돼요?', duration=2500, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_04()


class Event_04(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='허허... 녀석 참. 그럼 한개만 먹는거다?', duration=2500, delayTick=0)
        add_balloon_talk(spawnId=103, msg='여보!', duration=2500, delayTick=500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_05()


class Event_05(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=103, msg='그보다 요즘 한다는 일은 잘 되가요?', duration=2500, delayTick=1500)
        add_balloon_talk(spawnId=102, msg='와! 신난다!', duration=2500, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_06()


class Event_06(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='당연하지! 왕국 제일의 기술자인 내가 못할 일은 없어!', duration=2800, delayTick=1500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_07()


class Event_07(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='그런데 말이야. 일이 끝나갈 수록 기분이 영 찝찝해.', duration=2800, delayTick=1500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_08()


class Event_08(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='도대체 왕은 무슨 생각을 하고 있는건지...', duration=3000, delayTick=1500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Event_End()


class Event_End(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=False)
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[102])
        destroy_monster(spawnIds=[103])


