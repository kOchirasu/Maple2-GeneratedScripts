""" trigger/02000207_bf/bossspawn.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)
        set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3002], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 소환()


class 소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2001], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='ZakumDungeonEnd', value=1):
            return 종료딜레이()
        if dungeon_time_out():
            return 던전실패()
        if dungeon_check_state(checkState='Fail'):
            return 던전실패()


class 종료딜레이(state.State):
    def on_enter(self):
        set_user_value(triggerId=999103, key='BattleEnd', value=1)
        set_user_value(triggerId=999102, key='BattleEnd2', value=1) # 자쿰 팔 제거때 용암 올라오게 하는 트리거 xml 담당, 999102_Lavaflow.xml
        set_user_value(triggerId=999108, key='BattleEnd2', value=1) # 계약의 토템에 의해 왼쪽 용암 올라오게 하는 트리거 xml 담당, 999108_Lavaflow.xm
        set_user_value(triggerId=999109, key='BattleEnd2', value=1) # 계약의 토템에 의해 오른쪽 용암 올라오게 하는 트리거 xml 담당, 999109_Lavaflow.xml
        set_mesh(triggerIds=[3002], visible=False, arg3=0, arg4=0, arg5=0) # 자쿰 몸통 아래쪽 부위를 둘러싸고 있는 트리거 박스 제거하기
        set_mesh(triggerIds=[3003], visible=False, arg3=0, arg4=0, arg5=0) # 자쿰 몸통 위쪽 부위를 둘러싸고 있는 트리거 박스 제거하기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
            dungeon_clear()
            return 종료()


class 던전실패(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        set_user_value(triggerId=999103, key='BattleEnd', value=1)
        set_mesh(triggerIds=[3002], visible=False, arg3=0, arg4=0, arg5=0) # 자쿰 몸통 아래쪽 부위를 둘러싸고 있는 트리거 박스 제거하기
        set_mesh(triggerIds=[3003], visible=False, arg3=0, arg4=0, arg5=0) # 자쿰 몸통 위쪽 부위를 둘러싸고 있는 트리거 박스 제거하기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
            dungeon_fail()
            return 종료()


class 종료(state.State):
    def on_enter(self):
        dungeon_enable_give_up(isEnable='0')


