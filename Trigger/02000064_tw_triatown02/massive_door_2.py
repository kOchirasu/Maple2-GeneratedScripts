""" trigger/02000064_tw_triatown02/massive_door_2.xml """
import trigger_api


class 클로즈대기중(trigger_api.Trigger):
    pass


class 클로즈5초전(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='115', seconds=115)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='115'):
            return 클로즈중1(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='115')


class 클로즈중1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 클로즈중2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='5')


class 클로즈중2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='6', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 클로즈대기중(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='6')


initial_state = 클로즈대기중
