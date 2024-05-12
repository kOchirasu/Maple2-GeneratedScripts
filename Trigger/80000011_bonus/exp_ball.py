""" trigger/80000011_bonus/exp_ball.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            self.create_item(spawnIds=[9001])
            return 초5(self.ctx)


class 초5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            self.create_item(spawnIds=[9001])
            return 초10(self.ctx)


class 초10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            self.create_item(spawnIds=[9001])
            return 초15(self.ctx)


class 초15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            self.create_item(spawnIds=[9001])
            return 초20(self.ctx)


class 초20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            self.create_item(spawnIds=[9001])
            return 초25(self.ctx)


class 초25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            self.create_item(spawnIds=[9001])
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    pass


initial_state = 입장
