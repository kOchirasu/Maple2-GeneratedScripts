""" trigger/02000532_bf/talk.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[703], jobCode=0):
            return ready()


class ready(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=216, msg='$02000532_BF__TALK__0$', duration=3500, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return None # Missing State: 


