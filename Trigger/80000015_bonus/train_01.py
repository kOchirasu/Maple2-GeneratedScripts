""" trigger/80000015_bonus/train_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3100], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3701,3702,3703], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[121]):
            return 아이템체크()


class 아이템체크(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='itemSpawn', value=1):
            return 생성()
        if wait_tick(waitTick=200):
            create_item(spawnIds=[9020,9021,9022,9023,9024,9025], arg5=15)
            set_user_value(key='itemSpawn', value=1)
            return 생성()


class 생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1200], arg2=False)
        set_mesh(triggerIds=[3100], visible=False, arg3=500, arg4=0, arg5=0)
        add_buff(boxIds=[1200], skillId=60170051, level=1, arg4=True, arg5=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 삼()


class 삼(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3703], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 이()


class 이(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3703], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3702], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 일()


class 일(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3702], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3701], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 출발()


class 출발(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3701], visible=False, arg3=0, arg4=0, arg5=0)
        move_npc(spawnId=1200, patrolName='MS2PatrolData1200A')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=122, spawnIds=[1200]):
            return 소멸()


class 소멸(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            destroy_monster(spawnIds=[1200])
            return 딜레이()


class 딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 대기()


class 종료(state.State):
    pass


