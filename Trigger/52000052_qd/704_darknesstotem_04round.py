""" trigger/52000052_qd/704_darknesstotem_04round.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513], visible=False, arg3=0, arg4=0, arg5=0) # TotemGround
        set_user_value(key='TotemApp', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='TotemApp', value=1):
            return TotemApp01()


class TotemApp01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2004]) # 전투용 준타
        create_monster(spawnIds=[2304], arg2=False) # 날아라 준타
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513], visible=True, arg3=0, arg4=0, arg5=5) # TotemGround
        create_monster(spawnIds=[922], arg2=False) # 암흑 토템

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return JuntaReady01()


class JuntaReady01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2304, script='$52000052_QD__702_DARKNESSTOTEM_02ROUND__0$', arg4=3, arg5=0) # 전투중인 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return JuntaGoUp01()


class JuntaGoUp01(state.State):
    def on_enter(self):
        move_npc(spawnId=2304, patrolName='MS2PatrolData_2304')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return DestoryTotem01()


class DestoryTotem01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2104], arg2=False) # 토템 옆에 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return JuntaReturn01()


class JuntaReturn01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[922]) # 암흑 토템
        destroy_monster(spawnIds=[2304]) # 날아라 준타
        destroy_monster(spawnIds=[2104]) # 토템 옆에 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return JuntaReturn02()


class JuntaReturn02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2204], arg2=False) # Regen_A 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3500,3501,3502,3503,3504,3505,3506,3507,3508,3509,3510,3511,3512,3513], visible=False, arg3=0, arg4=0, arg5=5) # TotemGround


