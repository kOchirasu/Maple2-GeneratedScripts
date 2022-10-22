""" trigger/02000064_tw_triatown02/massive_door_2.xml """
from common import *
import state


class 클로즈대기중(state.State):
    pass


class 클로즈5초전(state.State):
    def on_enter(self):
        set_timer(timerId='115', seconds=115)

    def on_tick(self) -> state.State:
        if time_expired(timerId='115'):
            return 클로즈중1()

    def on_exit(self):
        reset_timer(timerId='115')


class 클로즈중1(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 클로즈중2()

    def on_exit(self):
        reset_timer(timerId='5')


class 클로즈중2(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 클로즈대기중()

    def on_exit(self):
        reset_timer(timerId='6')


