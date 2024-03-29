""" trigger/99999874/1000052_npctalk.xml """
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
        self.add_balloon_talk(spawnId=15501, msg='(뭐지... 왜 빤히 보는거지...엎드리지만 않았으면...)', duration=3000, delayTick=0)

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
        self.remove_balloon_talk(spawnId=15501)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
