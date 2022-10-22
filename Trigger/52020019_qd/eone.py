""" trigger/52020019_qd/eone.xml """
from common import *
import state


class Idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[60200010], questStates=[1]):
            return Talk()


class Talk(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='무엄하군요! 저리 가세요!', duration=3000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return Idle()


