""" trigger/83000003_colosseum/timer.xml """
from common import *
import state


#  <라운드 시작하면서 5분 시간 제한 타이머> 
class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Timer', value=1):
            return 스테이지1()
        if user_value(key='Timer', value=2):
            return 스테이지2()
        if user_value(key='Timer', value=3):
            return 스테이지3()
        if user_value(key='Timer', value=4):
            return 스테이지4()
        if user_value(key='Timer', value=5):
            return 스테이지5()
        if user_value(key='Timer', value=6):
            return 스테이지6()
        if user_value(key='Timer', value=7):
            return 스테이지7()
        if user_value(key='Timer', value=8):
            return 스테이지8()
        if user_value(key='Timer', value=9):
            return 스테이지9()
        if user_value(key='Timer', value=10):
            return 스테이지10()


class 스테이지1(state.State):
    def on_enter(self):
        set_timer(timerId='LimitTimer', seconds=180, clearAtZero=True)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="101" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> state.State:
        if true():
            return 타이머체크1()


class 타이머체크1(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='LimitTimer'):
            set_user_value(triggerId=900001, key='Fail', value=1)
            return 종료()
        if monster_dead(boxIds=[101]):
            set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료()


class 스테이지2(state.State):
    def on_enter(self):
        set_timer(timerId='LimitTimer2', seconds=180, clearAtZero=True)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="102" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> state.State:
        if true():
            return 타이머체크2()


class 타이머체크2(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='LimitTimer'):
            set_user_value(triggerId=900001, key='Fail', value=1)
            return 종료()
        if monster_dead(boxIds=[102]):
            set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료()


class 스테이지3(state.State):
    def on_enter(self):
        set_timer(timerId='LimitTimer3', seconds=180, clearAtZero=True)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="103" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> state.State:
        if true():
            return 타이머체크3()


class 타이머체크3(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='LimitTimer'):
            set_user_value(triggerId=900001, key='Fail', value=1)
            return 종료()
        if monster_dead(boxIds=[103]):
            set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료()


class 스테이지4(state.State):
    def on_enter(self):
        set_timer(timerId='LimitTimer4', seconds=180, clearAtZero=True)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="104" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> state.State:
        if true():
            return 타이머체크4()


class 타이머체크4(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='LimitTimer'):
            return 종료()
        if monster_dead(boxIds=[104]):
            set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료()


class 스테이지5(state.State):
    def on_enter(self):
        set_timer(timerId='LimitTimer5', seconds=180, clearAtZero=True)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="105" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> state.State:
        if true():
            return 타이머체크5()


class 타이머체크5(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='LimitTimer'):
            return 종료()
        if monster_dead(boxIds=[105]):
            set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료()


class 스테이지6(state.State):
    def on_enter(self):
        set_timer(timerId='LimitTimer6', seconds=180, clearAtZero=True)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="106" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> state.State:
        if true():
            return 타이머체크6()


class 타이머체크6(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='LimitTimer'):
            return 종료()
        if monster_dead(boxIds=[106]):
            set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료()


class 스테이지7(state.State):
    def on_enter(self):
        set_timer(timerId='LimitTimer7', seconds=180, clearAtZero=True)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="107" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> state.State:
        if true():
            return 타이머체크7()


class 타이머체크7(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='LimitTimer'):
            return 종료()
        if monster_dead(boxIds=[107]):
            set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료()


class 스테이지8(state.State):
    def on_enter(self):
        set_timer(timerId='LimitTimer8', seconds=300, clearAtZero=True)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="108" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> state.State:
        if true():
            return 타이머체크8()


class 타이머체크8(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='LimitTimer'):
            return 종료()
        if monster_dead(boxIds=[108]):
            set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료()


class 스테이지9(state.State):
    def on_enter(self):
        set_timer(timerId='LimitTimer9', seconds=300, clearAtZero=True)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="109" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> state.State:
        if true():
            return 타이머체크9()


class 타이머체크9(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='LimitTimer'):
            return 종료()
        if monster_dead(boxIds=[109]):
            set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료()


class 스테이지10(state.State):
    def on_enter(self):
        set_timer(timerId='LimitTimer10', seconds=300, clearAtZero=True)
        # <action name="SetNpcDuelHpBar" isOpen="true" spawnPointID="110" durationTick="180000" npcHpStep="100" />

    def on_tick(self) -> state.State:
        if true():
            return 타이머체크10()


class 타이머체크10(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='LimitTimer'):
            return 종료()
        if monster_dead(boxIds=[110]):
            set_user_value(triggerId=900001, key='Nextmonster', value=1)
            return 종료()


class 종료(state.State):
    def on_enter(self):
        reset_timer(timerId='LimitTimer')
        reset_timer(timerId='LimitTimer2')
        reset_timer(timerId='LimitTimer3')
        reset_timer(timerId='LimitTimer4')
        reset_timer(timerId='LimitTimer5')
        reset_timer(timerId='LimitTimer6')
        reset_timer(timerId='LimitTimer7')
        reset_timer(timerId='LimitTimer8')
        reset_timer(timerId='LimitTimer9')
        reset_timer(timerId='LimitTimer10')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대기()


