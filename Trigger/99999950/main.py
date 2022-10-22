""" trigger/99999950/main.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 시작대기()


class 시작대기(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            set_event_ui(type=1, arg2='$99999950__MAIN__0$', arg3='2000', arg4='0')
            return 라운드1()


class 라운드1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101001], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101001]):
            return 라운드02_1()


class 라운드02_1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101001], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101001]):
            return 라운드대기2()


class 라운드대기2(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            set_event_ui(type=1, arg2='$99999950__MAIN__1$', arg3='2000', arg4='0')
            return 라운드2()


class 라운드2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101002], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101002]):
            return 라운드02_2()


class 라운드02_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101002], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101002]):
            return 라운드대기3()


class 라운드대기3(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            set_event_ui(type=1, arg2='$99999950__MAIN__2$', arg3='2000', arg4='0')
            return 라운드3()


class 라운드3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101003], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101003]):
            return 라운드02_3()


class 라운드02_3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101003], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101003]):
            return 라운드대기4()


class 라운드대기4(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            set_event_ui(type=1, arg2='$99999950__MAIN__3$', arg3='2000', arg4='0')
            return 라운드4()


class 라운드4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101004], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101004]):
            return 라운드02_4()


class 라운드02_4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101004], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101004]):
            return 라운드03_4()


class 라운드03_4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101004], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101004]):
            return 라운드대기5()


class 라운드대기5(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            set_event_ui(type=1, arg2='$99999950__MAIN__4$', arg3='2000', arg4='0')
            return 라운드5()


class 라운드5(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101005], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101005]):
            return None # Missing State: 라운드대기6


