""" trigger/52000052_qd/713_darknesstotem_12round.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3900,3901,3902,3903,3904,3905,3906,3907,3908,3909,3910,3911,3912,3913], visible=False, arg3=0, arg4=0, arg5=0) # TotemGround
        set_user_value(key='TotemApp', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='TotemApp', value=1):
            return TotemApp01()


class TotemApp01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2212]) # Regen_A로 돌아갔던 준타
        create_monster(spawnIds=[2313], arg2=False) # 날아라 준타
        set_mesh(triggerIds=[3900,3901,3902,3903,3904,3905,3906,3907,3908,3909,3910,3911,3912,3913], visible=True, arg3=0, arg4=0, arg5=5) # TotemGround
        create_monster(spawnIds=[926], arg2=False) # 암흑 토템

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return JuntaReady01()


class JuntaReady01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2313, script='$52000052_QD__702_DARKNESSTOTEM_02ROUND__0$', arg4=3, arg5=0) # 전투중인 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return JuntaGoUp01()


class JuntaGoUp01(state.State):
    def on_enter(self):
        move_npc(spawnId=2313, patrolName='MS2PatrolData_2313')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return DestoryTotem01()


class DestoryTotem01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2113], arg2=False) # 토템 옆에 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return JuntaReturn01()


class JuntaReturn01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[926]) # 암흑 토템
        destroy_monster(spawnIds=[2313]) # 날아라 준타
        destroy_monster(spawnIds=[2113]) # 토템 옆에 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return JuntaReturn02()


class JuntaReturn02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2213], arg2=False) # Regen_A 준타

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3900,3901,3902,3903,3904,3905,3906,3907,3908,3909,3910,3911,3912,3913], visible=False, arg3=0, arg4=0, arg5=5) # TotemGround


