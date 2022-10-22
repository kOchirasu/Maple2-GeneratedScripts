""" trigger/63000040_cs/main.xml """
from common import *
import state


class ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,103,104], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[40002652], questStates=[3]):
            return start_02()
        if quest_user_detected(boxIds=[701], questIds=[40002652], questStates=[2]):
            return start_02_ready()
        if quest_user_detected(boxIds=[701], questIds=[40002652], questStates=[1]):
            return start()


class start(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25200474, textId=25200474)
        set_effect(triggerIds=[7001], visible=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[40002652], questStates=[2]):
            return start_02_ready()


class start_02_ready(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=25200474)
        set_effect(triggerIds=[7001], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[40002652], questStates=[3]):
            return start_02()


class start_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=103, patrolName='MS2PatrolData_2001') # 연출용 틴차이 이동
        move_user_path(patrolName='MS2PatrolData_2002') # 유저를 이동시킨다
        select_camera_path(pathIds=[8001,8002], returnView=False)
        set_conversation(type=2, spawnId=11001708, script='$63000040_CS__MAIN__0$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return start_03()


class start_03(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=3000)
        set_conversation(type=2, spawnId=11001708, script='$63000040_CS__MAIN__1$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return start_04()


class start_04(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_2003') # 연출용 틴차이 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start_05()


class start_05(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2003') # 연출용 틴차이 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start_06()


class start_06(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2003') # 유저를 이동시킨다

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            select_camera_path(pathIds=[8003], returnView=False)
            return start_07()


class start_07(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return end()


class end(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


