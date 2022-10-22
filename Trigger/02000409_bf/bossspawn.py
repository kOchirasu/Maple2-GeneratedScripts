""" trigger/02000409_bf/bossspawn.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1,2,3,4,5], visible=True, arg3=0, arg4=0, arg5=0)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[999], arg2=False) # 이벤트
        create_monster(spawnIds=[99], arg2=False) # 핑크빈
        create_monster(spawnIds=[90], arg2=False)
        create_monster(spawnIds=[91], arg2=False)
        create_monster(spawnIds=[92], arg2=False)
        create_monster(spawnIds=[93], arg2=False)
        create_monster(spawnIds=[94], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return 종료딜레이()
        if dungeon_time_out():
            return 던전실패()
        if dungeon_check_state(checkState='Fail'):
            return 던전실패()


class 종료딜레이(state.State):
    def on_enter(self):
        set_user_value(triggerId=9999998, key='BattleEnd', value=1)
        set_mesh(triggerIds=[3002], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
            dungeon_clear()
            return 종료()


class 던전실패(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        set_user_value(triggerId=9999998, key='BattleEnd', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
            dungeon_fail()
            return 종료()


class 종료(state.State):
    def on_enter(self):
        dungeon_enable_give_up(isEnable='0')


