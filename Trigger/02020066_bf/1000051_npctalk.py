""" trigger/02020066_bf/1000051_npctalk.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='NPCTalk', value=1):
            return NPCTalkOnWait()


class NPCTalkOnWait(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return NPCTalkOn()


class NPCTalkOn(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=15401, msg='$02020031_BF__1000051_NPCTALK__0$', duration=3000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TalkDelay()


class TalkDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=17000):
            return NPCTalkOn()
        if user_value(key='NPCTalk', value=0):
            return None # Missing State: NPCTalkOff


class PortalOff(state.State):
    def on_enter(self):
        remove_balloon_talk(spawnId=15401)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


