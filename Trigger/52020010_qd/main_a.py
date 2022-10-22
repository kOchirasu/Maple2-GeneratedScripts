""" trigger/52020010_qd/main_a.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_actor(triggerId=8001, visible=False, initialSequence='Event_01_A')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200045], questStates=[2]):
            return Event_01()


class Event_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Event_02()


class Event_02(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=0, msg='!!!', duration=1000, delayTick=0)
        set_effect(triggerIds=[5001], visible=True)
        set_actor(triggerId=8001, visible=True, initialSequence='Event_03_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Event_End()


class Event_End(state.State):
    def on_enter(self):
        set_actor(triggerId=8001, visible=False, initialSequence='Event_03_A')
        reset_camera(interpolationTime=1)


