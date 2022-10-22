""" trigger/02000378_bf/702_darknesstotem_02round.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313], visible=False, arg3=0, arg4=0, arg5=0) # TotemGround
        set_user_value(key='TotemApp', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='TotemApp', value=1):
            return TotemApp01()


class TotemApp01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2002]) # 전투용 준타
        create_monster(spawnIds=[2302], arg2=False) # 날아라 준타
        set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313], visible=True, arg3=0, arg4=0, arg5=5) # TotemGround
        create_monster(spawnIds=[920], arg2=False) # 암흑 토템

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return JuntaReady01()


class JuntaReady01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2302, script='$02000378_BF__702_DARKNESSTOTEM_02ROUND__0$', arg4=3, arg5=0) # 전투중인 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return JuntaGoUp01()


class JuntaGoUp01(state.State):
    def on_enter(self):
        move_npc(spawnId=2302, patrolName='MS2PatrolData_2302')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return DestoryTotem01()


class DestoryTotem01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2102], arg2=False) # 토템 옆에 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return JuntaReturn01()


class JuntaReturn01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[920]) # 암흑 토템
        destroy_monster(spawnIds=[2302]) # 날아라 준타
        destroy_monster(spawnIds=[2102]) # 토템 옆에 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return JuntaReturn02()


class JuntaReturn02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2202], arg2=False) # Regen_A 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313], visible=False, arg3=0, arg4=0, arg5=5) # TotemGround


