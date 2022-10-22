""" trigger/02100000_bf/timer.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=19, visible=False, enabled=False, minimapVisible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[106]):
            return 타이머시작()


class 타이머시작(state.State):
    def on_enter(self):
        set_timer(timerId='10000', seconds=360, clearAtZero=True, display=True, arg5=0)

    def on_tick(self) -> state.State:
        if true():
            return 유저감지_2()


class 유저감지_2(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 몬스터등장_보스()


class 몬스터등장_보스(state.State):
    def on_enter(self):
        create_monster(spawnIds=[82001], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료선택()


class 종료선택(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[82001]):
            return 성공()
        if time_expired(timerId='10000'):
            return 실패()

    def on_exit(self):
        reset_timer(timerId='10000')


class 성공(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        set_achievement(triggerId=9900, type='trigger', achieve='Find02100000')
        set_event_ui(type=7, arg2='$02100000_BF__TIMER__1$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            dungeon_clear()
            return 종료()


class 실패(state.State):
    def on_enter(self):
        set_event_ui(type=5, arg2='$02100000_BF__TIMER__0$', arg3='2000', arg4='0')
        destroy_monster(spawnIds=[-1])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            dungeon_fail()
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_portal(portalId=19, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True)


