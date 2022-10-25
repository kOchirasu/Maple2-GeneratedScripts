""" trigger/02000251_bf/end.xml """
import common


class 대기(common.Trigger):
    pass


class 어나운스1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=7)
        self.set_event_ui(type=1, arg2='$02000251_BF__END__0$', arg3='5000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 어나운스2(self.ctx)


class 어나운스2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=7)
        self.set_event_ui(type=1, arg2='$02000251_BF__END__1$', arg3='5000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 어나운스3(self.ctx)


class 어나운스3(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=7)
        self.set_event_ui(type=1, arg2='$02000251_BF__END__2$', arg3='5000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 어나운스4(self.ctx)


class 어나운스4(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=7)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 통과(self.ctx)


class 통과(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=300)


initial_state = 대기
