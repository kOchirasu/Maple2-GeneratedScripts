""" trigger/02000251_bf/end.xml """
from common import *
import state


class 대기(state.State):
    pass


class 어나운스1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=7)
        set_event_ui(type=1, arg2='$02000251_BF__END__0$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 어나운스2()


class 어나운스2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=7)
        set_event_ui(type=1, arg2='$02000251_BF__END__1$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 어나운스3()


class 어나운스3(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=7)
        set_event_ui(type=1, arg2='$02000251_BF__END__2$', arg3='5000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 어나운스4()


class 어나운스4(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=7)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 통과()


class 통과(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=300)


