""" trigger/02000486_bf/107_text.xml """
import trigger_api


class 유저감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9901]):
            return 알림(self.ctx)


class 알림(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_npc_hp(spawnId=900, compare='lowerEqual', value=30, isRelative=True) or self.check_npc_hp(spawnId=901, compare='lowerEqual', value=30, isRelative=True):
            return 텍스트(self.ctx)


class 텍스트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000486_BF__107_TEXT__0$', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            pass


initial_state = 유저감지
