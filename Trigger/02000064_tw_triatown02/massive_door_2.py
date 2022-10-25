""" trigger/02000064_tw_triatown02/massive_door_2.xml """
import common


class 클로즈대기중(common.Trigger):
    pass


class 클로즈5초전(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='115', seconds=115)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='115'):
            return 클로즈중1(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='115')


class 클로즈중1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='5'):
            return 클로즈중2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='5')


class 클로즈중2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='6', seconds=60)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='6'):
            return 클로즈대기중(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='6')


initial_state = 클로즈대기중
