""" trigger/52020027_qd/52020027_boss.xml """
from common import *
import state


class 감지(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Boss', value=1):
            return 페이즈1()


class 페이즈1(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SerihaAI', value=1):
            return 도약()


class 도약(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=903, spawnIds=[111]):
            return 페이즈2()


class 페이즈2(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=111, script='조심하는 게 좋을걸?', arg4=4)
        create_monster(spawnIds=[112], arg2=True)
        create_monster(spawnIds=[113], arg2=True)
        create_monster(spawnIds=[114], arg2=True)
        create_monster(spawnIds=[115], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NPC애니세팅()


class NPC애니세팅(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=114, sequenceName='Attack_01_A', duration=2000)
        set_npc_emotion_loop(spawnId=115, sequenceName='Attack_01_A', duration=2000)


