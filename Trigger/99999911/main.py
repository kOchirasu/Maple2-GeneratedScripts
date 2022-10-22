""" trigger/99999911/main.xml """
from common import *
import state


#  플레이어 감지 
class 최초(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=1):
            return 시작조건체크()


class 시작조건체크(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 어나운스0()
        if count_users(boxId=701, boxId=20):
            return 어나운스0()


class 어나운스0(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$99999911__MAIN__0$', arg3='4000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 어나운스1()


class 어나운스1(state.State):
    def on_enter(self):
        show_count_ui(text='$61000004_ME__TRIGGER_01__1$', stage=0, count=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5500):
            set_mesh(triggerIds=[301,302,303], visible=False, arg3=12, arg4=0)
            set_achievement(triggerId=101, type='trigger', achieve='dailyquest_start')
            return idle()


class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True, arg3=1)
        create_monster(spawnIds=[102], arg2=True, arg3=2)
        create_monster(spawnIds=[103], arg2=True, arg3=3)
        create_monster(spawnIds=[104], arg2=True, arg3=4)
        create_monster(spawnIds=[105], arg2=True, arg3=5)
        create_monster(spawnIds=[106], arg2=True, arg3=6)
        create_monster(spawnIds=[107], arg2=True, arg3=7)
        create_monster(spawnIds=[108], arg2=True, arg3=0)
        create_monster(spawnIds=[301], arg2=True, arg3=1)
        create_monster(spawnIds=[302], arg2=True, arg3=2)
        create_monster(spawnIds=[303], arg2=True, arg3=3)
        create_monster(spawnIds=[304], arg2=True, arg3=0)
        create_monster(spawnIds=[305], arg2=True, arg3=1)
        create_monster(spawnIds=[306], arg2=True, arg3=2)
        create_monster(spawnIds=[307], arg2=True, arg3=3)
        create_monster(spawnIds=[308], arg2=True, arg3=0)
        create_monster(spawnIds=[309], arg2=True, arg3=1)
        create_monster(spawnIds=[310], arg2=True, arg3=2)
        create_monster(spawnIds=[311], arg2=True, arg3=3)
        create_monster(spawnIds=[312], arg2=True, arg3=0)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return Round1_Start()


class Round1_Start(state.State):
    def on_enter(self):
        set_user_value(triggerId=991104, key='Round_02', value=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return None # Missing State: random_start


