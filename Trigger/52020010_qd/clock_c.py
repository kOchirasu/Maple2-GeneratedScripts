""" trigger/52020010_qd/clock_c.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5007], visible=False)
        set_effect(triggerIds=[5008], visible=False)
        set_effect(triggerIds=[5009], visible=False)
        set_effect(triggerIds=[5010], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2004]):
            return Ready()


class Ready(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001273], arg2=0):
            return Event_Start()


class Event_Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5007], visible=True)
        create_monster(spawnIds=[301], arg2=True) # 엄마 유령
        create_monster(spawnIds=[302], arg2=True) # 애기 유령

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return Event_01()


class Event_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5008], visible=True)
        set_npc_emotion_loop(spawnId=302, sequenceName='Bore_B', duration=18000)
        add_balloon_talk(spawnId=302, msg='엄마 무서워...', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_02()


class Event_02(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=301, msg='울지마렴... 조금 있으면 괜찮아 질거야...', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_03()


class Event_03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5009], visible=True)
        add_balloon_talk(spawnId=301, msg='여보? 어디 간 거에요!', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_04()


class Event_04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5010], visible=True)
        add_balloon_talk(spawnId=301, msg='여보!!!', duration=2800, delayTick=1000)
        add_balloon_talk(spawnId=302, msg='엄마... 아빠... 무서워...', duration=2800, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Event_End()


class Event_End(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5007], visible=False)
        set_effect(triggerIds=[5008], visible=False)
        set_effect(triggerIds=[5009], visible=False)
        set_effect(triggerIds=[5010], visible=False)
        destroy_monster(spawnIds=[301])
        destroy_monster(spawnIds=[302])


