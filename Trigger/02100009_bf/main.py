""" trigger/02100009_bf/main.xml """
from common import *
import state


class 유저감지(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 타이머설정()


class 타이머설정(state.State):
    def on_enter(self):
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=True)
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True)
        set_timer(timerId='10000', seconds=300, clearAtZero=True, display=True, arg5=0)

    def on_tick(self) -> state.State:
        if true():
            return 끝()


class 끝(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 성공()
        if time_expired(timerId='10000'):
            return 실패()

    def on_exit(self):
        reset_timer(timerId='10000')


class 성공(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 성공_2()

    def on_exit(self):
        set_event_ui(type=1, arg2='$02100009_BF__text__0$', arg3='4000')


class 성공_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5500):
            dungeon_clear()
            return 성공_3()

    def on_exit(self):
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)


class 성공_3(state.State):
    def on_enter(self):
        add_buff(boxIds=[101], skillId=50000230, level=1, arg4=False, arg5=False)
        destroy_monster(spawnIds=[-1])
        set_achievement(triggerId=9900, type='trigger', achieve='Find02100009')
        set_event_ui(type=7, arg2='$02100009_BF__MAIN__1$', arg3='2000', arg4='0')
        set_achievement(triggerId=9900, type='trigger', achieve='02100009_2')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            dungeon_clear()
            return 종료()


class 실패(state.State):
    def on_enter(self):
        add_buff(boxIds=[101], skillId=50000230, level=1, arg4=False, arg5=False)
        set_event_ui(type=5, arg2='$02100009_BF__MAIN__0$', arg3='2000', arg4='0')
        destroy_monster(spawnIds=[-1])
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            dungeon_fail()
            return 종료()


class 종료(state.State):
    pass


