""" trigger/52000120_qd/02_rightshieldbarrier.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3200], visible=True, arg3=0, arg4=0, arg5=0) # Invisible_Barrier
        destroy_monster(spawnIds=[980,981,982,983,984,985])
        set_skill(triggerIds=[7000], isEnable=False) # Push

    def on_tick(self) -> state.State:
        if check_user():
            return ActivateShiled01()


class ActivateShiled01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[980,981,982,983,984,985], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9200]):
            return Push01()


class Push01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=980, sequenceName='Attack_01_A')
        set_npc_emotion_sequence(spawnId=981, sequenceName='Attack_01_A')
        set_npc_emotion_sequence(spawnId=982, sequenceName='Attack_01_A')
        set_npc_emotion_sequence(spawnId=983, sequenceName='Attack_01_A')
        set_npc_emotion_sequence(spawnId=984, sequenceName='Attack_01_A')
        set_npc_emotion_sequence(spawnId=985, sequenceName='Attack_01_A')
        set_skill(triggerIds=[7000], isEnable=True) # Push

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1333):
            return Reset01()


class Reset01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9200]):
            return Push01()


