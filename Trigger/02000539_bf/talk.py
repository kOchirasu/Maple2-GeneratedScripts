""" trigger/02000539_bf/talk.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[703], jobCode=0):
            return 말풍선1()
        if user_detected(boxIds=[704], jobCode=0):
            return 말풍선2()


class 말풍선1(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=201, msg='$02000539_BF__TALK__0$', duration=3500, delayTick=0)
        add_balloon_talk(spawnId=201, msg='$02000539_BF__TALK__1$', duration=3500, delayTick=3500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return idle()


class 말풍선2(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=202, msg='$02000539_BF__TALK__2$', duration=3500, delayTick=0)
        add_balloon_talk(spawnId=202, msg='$02000539_BF__TALK__3$', duration=3500, delayTick=3500)
        add_balloon_talk(spawnId=202, msg='$02000539_BF__TALK__4$', duration=3500, delayTick=7000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return idle()


