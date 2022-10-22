""" trigger/80000015_bonus/train_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3200,3210], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3704,3705,3706], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[123]):
            return 아이템체크()


class 아이템체크(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='itemSpawn', value=1):
            return 생성()
        if wait_tick(waitTick=200):
            create_item(spawnIds=[9026,9027,9028,9029,9030,9031], arg5=15)
            set_user_value(key='itemSpawn', value=1)
            return 생성()


class 생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1201], arg2=False)
        set_mesh(triggerIds=[3200], visible=False, arg3=500, arg4=0, arg5=0)
        add_buff(boxIds=[1201], skillId=60170051, level=1, arg4=True, arg5=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 삼()


class 삼(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3706], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 이()


class 이(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3706], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3705], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 일()


class 일(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3705], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3704], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 출발()


class 출발(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3704], visible=False, arg3=0, arg4=0, arg5=0)
        move_npc(spawnId=1201, patrolName='MS2PatrolData1201A')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=124, spawnIds=[1201]):
            return 소멸()


class 소멸(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            destroy_monster(spawnIds=[1201])
            return 딜레이()


class 딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 대기()


class 종료(state.State):
    pass


