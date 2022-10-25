""" trigger/80000009_bonus/exp_ball.xml """
import common


class 입장(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[402]):
            self.create_item(spawnIds=[9001,9002,9003,9004,9005])
            return 초5(self.ctx)


class 초5(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            self.create_item(spawnIds=[9001])
            return 초10(self.ctx)


class 초10(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            self.create_item(spawnIds=[9001])
            return 초15(self.ctx)


class 초15(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            self.create_item(spawnIds=[9001])
            return 초20(self.ctx)


class 초20(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            self.create_item(spawnIds=[9001])
            return 초25(self.ctx)


class 초25(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            self.create_item(spawnIds=[9001])
            return 완료(self.ctx)


class 완료(common.Trigger):
    pass


initial_state = 입장
