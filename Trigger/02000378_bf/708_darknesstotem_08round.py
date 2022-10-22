""" trigger/02000378_bf/708_darknesstotem_08round.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3700,3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713], visible=False, arg3=0, arg4=0, arg5=0) # TotemGround
        set_user_value(key='TotemApp', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='TotemApp', value=1):
            return TotemApp01()


class TotemApp01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2008]) # 전투용 준타
        create_monster(spawnIds=[2308], arg2=False) # 날아라 준타
        set_mesh(triggerIds=[3700,3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713], visible=True, arg3=0, arg4=0, arg5=5) # TotemGround
        create_monster(spawnIds=[924], arg2=False) # 암흑 토템

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return JuntaReady01()


class JuntaReady01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2308, script='$02000378_BF__708_DARKNESSTOTEM_08ROUND__0$', arg4=3, arg5=0) # 전투중인 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return JuntaGoUp01()


class JuntaGoUp01(state.State):
    def on_enter(self):
        move_npc(spawnId=2308, patrolName='MS2PatrolData_2308')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return DestoryTotem01()


class DestoryTotem01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2108], arg2=False) # 토템 옆에 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return JuntaReturn01()


class JuntaReturn01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[924]) # 암흑 토템
        destroy_monster(spawnIds=[2308]) # 날아라 준타
        destroy_monster(spawnIds=[2108]) # 토템 옆에 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return JuntaReturn02()


class JuntaReturn02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2208], arg2=False) # Regen_A 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3700,3701,3702,3703,3704,3705,3706,3707,3708,3709,3710,3711,3712,3713], visible=False, arg3=0, arg4=0, arg5=5) # TotemGround


