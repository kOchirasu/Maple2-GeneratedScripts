""" trigger/52000067_qd/sub_event_03.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[591,592], arg2=True) # 시민

    def on_tick(self) -> state.State:
        if count_users(boxId=705, boxId=1):
            return ready()


class ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[537,538,539], arg2=True) # 몬스터
        set_npc_emotion_loop(spawnId=591, sequenceName='Emotion_Failure_Idle_A', duration=600000)
        set_npc_emotion_loop(spawnId=592, sequenceName='Emotion_Failure_Idle_A', duration=600000)
        set_conversation(type=1, spawnId=591, script='$52000067_QD__SUB_EVENT_03__0$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=592, script='$52000067_QD__SUB_EVENT_03__1$', arg4=3, arg5=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[537,538,539]):
            return end()


class end(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=591, sequenceName='Talk_A')
        set_npc_emotion_sequence(spawnId=592, sequenceName='Idle_A')
        set_conversation(type=1, spawnId=591, script='$52000067_QD__SUB_EVENT_03__2$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return ending()


class ending(state.State):
    def on_enter(self):
        move_npc(spawnId=591, patrolName='MS2PatrolData_5010')
        move_npc(spawnId=592, patrolName='MS2PatrolData_5010')


