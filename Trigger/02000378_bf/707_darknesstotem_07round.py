""" trigger/02000378_bf/707_darknesstotem_07round.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3600,3601,3602,3603,3604,3605,3606,3607,3608,3609,3610,3611,3612,3613], visible=False, arg3=0, arg4=0, arg5=0) # TotemGround
        set_user_value(key='TotemApp', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='TotemApp', value=1):
            return TotemApp01()


class TotemApp01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2007]) # 전투용 준타
        create_monster(spawnIds=[2307], arg2=False) # 날아라 준타
        set_mesh(triggerIds=[3600,3601,3602,3603,3604,3605,3606,3607,3608,3609,3610,3611,3612,3613], visible=True, arg3=0, arg4=0, arg5=5) # TotemGround
        create_monster(spawnIds=[923], arg2=False) # 암흑 토템

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return JuntaReady01()


class JuntaReady01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2307, script='$02000378_BF__707_DARKNESSTOTEM_07ROUND__0$', arg4=3, arg5=0) # 전투중인 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return JuntaGoUp01()


class JuntaGoUp01(state.State):
    def on_enter(self):
        move_npc(spawnId=2307, patrolName='MS2PatrolData_2307')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return DestoryTotem01()


class DestoryTotem01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2107], arg2=False) # 토템 옆에 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return JuntaReturn01()


class JuntaReturn01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[923]) # 암흑 토템
        destroy_monster(spawnIds=[2307]) # 날아라 준타
        destroy_monster(spawnIds=[2107]) # 토템 옆에 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return JuntaReturn02()


class JuntaReturn02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2207], arg2=False) # Regen_A 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3600,3601,3602,3603,3604,3605,3606,3607,3608,3609,3610,3611,3612,3613], visible=False, arg3=0, arg4=0, arg5=5) # TotemGround


