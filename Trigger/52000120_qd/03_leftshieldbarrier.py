""" trigger/52000120_qd/03_leftshieldbarrier.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3201], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_Barrier
        destroy_monster(spawnIds=[990,991,992,993,994,995])
        set_skill(triggerIds=[7001], isEnable=False) # Push

    def on_tick(self) -> state.State:
        if check_user():
            return ActivateShiled01()


class ActivateShiled01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[990,991,992,993,994,995], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9201]):
            return Push01()


class Push01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=990, sequenceName='Attack_01_A')
        set_npc_emotion_sequence(spawnId=991, sequenceName='Attack_01_A')
        set_npc_emotion_sequence(spawnId=992, sequenceName='Attack_01_A')
        set_npc_emotion_sequence(spawnId=993, sequenceName='Attack_01_A')
        set_npc_emotion_sequence(spawnId=994, sequenceName='Attack_01_A')
        set_npc_emotion_sequence(spawnId=995, sequenceName='Attack_01_A')
        set_skill(triggerIds=[7001], isEnable=True) # Push

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1333):
            return Reset01()


class Reset01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9201]):
            return Push01()


