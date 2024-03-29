""" trigger/02020009_bf/1000051_npctalk.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NPCTalk', value=1):
            return NPCTalkOnWait(self.ctx)


class NPCTalkOnWait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return NPCTalkOn(self.ctx)


class NPCTalkOn(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=15401, msg='$02020009_BF__1000051_NPCTALK__0$', duration=3000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TalkDelay(self.ctx)


class TalkDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=17000):
            return NPCTalkOn(self.ctx)
        if self.user_value(key='NPCTalk', value=0):
            return None # Missing State: NPCTalkOff


class PortalOff(trigger_api.Trigger):
    def on_enter(self):
        self.remove_balloon_talk(spawnId=15401)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
