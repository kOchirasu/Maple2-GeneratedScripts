""" trigger/02000066_bf/pato.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=103, spawnIds=[1299]):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        add_buff(boxIds=[103], skillId=70000107, level=1, arg4=False, arg5=False)
        select_camera(triggerId=301, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[1601], arg2=False)
        create_monster(spawnIds=[1602], arg2=False)
        create_monster(spawnIds=[1603], arg2=False)
        create_monster(spawnIds=[1604], arg2=False)
        set_skip(state=연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 연출진행()


class 연출진행(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000068, script='$02000066_BF__PATO__0$', arg4=2)
        set_skip(state=연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2429):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        remove_buff(boxId=103, skillId=70000107)
        select_camera(triggerId=301, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


