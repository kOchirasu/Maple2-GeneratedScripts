""" trigger/52000052_qd/712_darknesstotem_12round.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3800,3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813], visible=False, arg3=0, arg4=0, arg5=0) # TotemGround
        set_user_value(key='TotemApp', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='TotemApp', value=1):
            return TotemApp01()


class TotemApp01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2012]) # 전투용 준타
        create_monster(spawnIds=[2312], arg2=False) # 날아라 준타
        set_mesh(triggerIds=[3800,3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813], visible=True, arg3=0, arg4=0, arg5=5) # TotemGround
        create_monster(spawnIds=[925], arg2=False) # 암흑 토템

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return JuntaReady01()


class JuntaReady01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2312, script='$52000052_QD__702_DARKNESSTOTEM_02ROUND__0$', arg4=3, arg5=0) # 전투중인 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return JuntaGoUp01()


class JuntaGoUp01(state.State):
    def on_enter(self):
        move_npc(spawnId=2312, patrolName='MS2PatrolData_2312')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return DestoryTotem01()


class DestoryTotem01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2112], arg2=False) # 토템 옆에 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return JuntaReturn01()


class JuntaReturn01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[925]) # 암흑 토템
        destroy_monster(spawnIds=[2312]) # 날아라 준타
        destroy_monster(spawnIds=[2112]) # 토템 옆에 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return JuntaReturn02()


class JuntaReturn02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2212], arg2=False) # Regen_A 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3800,3801,3802,3803,3804,3805,3806,3807,3808,3809,3810,3811,3812,3813], visible=False, arg3=0, arg4=0, arg5=5) # TotemGround


