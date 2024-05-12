""" trigger/02000486_bf/103_timer.xml """
import trigger_api


class 전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[900]) or self.monster_in_combat(boxIds=[901]):
            return 타이머(self.ctx)


class 타이머(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='999', seconds=240, startDelay=1, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 설명(self.ctx)


class 설명(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000486_BF__103_TIMER__0$', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=239000):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[900]) and self.monster_dead(boxIds=[901]):
            return 타이머종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000486_BF__103_TIMER__1$', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            pass


class 타이머종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timerId='999')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            pass


initial_state = 전투시작
