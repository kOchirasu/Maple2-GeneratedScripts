""" trigger/61000009_me/timer.xml """
import trigger_api


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=100, text_id=40012) # 잠시 후에 시작합니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return ready(self.ctx)
        if self.user_value(key='timer', value=1):
            return Ready_Idle(self.ctx)


class Ready_Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=100)
        self.set_timer(timer_id='1200', seconds=1200, start_delay=0, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1200'):
            return endGame(self.ctx)


class endGame(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=5, arg2='$61000004_ME__TRIGGER_01__2$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.move_user(map_id=0, portal_id=0)
            return end(self.ctx)


class end(trigger_api.Trigger):
    pass


initial_state = ready
