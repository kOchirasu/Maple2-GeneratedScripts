""" trigger/02020031_bf/1000052_npctalk.xml """
import common


class Wait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='NPCTalk', value=1):
            return NPCTalkOnWait(self.ctx)


class NPCTalkOnWait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return NPCTalkOn(self.ctx)


class NPCTalkOn(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=15501, msg='$02020031_BF__1000052_NPCTALK__0$', duration=3000, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return TalkDelay(self.ctx)


class TalkDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=17000):
            return NPCTalkOn(self.ctx)
        if self.user_value(key='NPCTalk', value=0):
            return None # Missing State: NPCTalkOff


class PortalOff(common.Trigger):
    def on_enter(self):
        self.remove_balloon_talk(spawnId=15501)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
