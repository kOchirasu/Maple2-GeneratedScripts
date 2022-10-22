""" trigger/52010018_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[100], questIds=[10002852], questStates=[1]):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1002,1003,1004,1006], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_A')
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_A')
        move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_A')
        move_npc(spawnId=1006, patrolName='MS2PatrolData_1006_A')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[1002]):
            return 둔바대사01()
        if npc_detected(boxId=102, spawnIds=[1003]):
            return 둔바대사01()


class 둔바대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001217, script='$52010018_QD__MAIN__0$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 에레브대사01()


class 에레브대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52010018_QD__MAIN__1$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 미카대사01()


class 미카대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001285, script='$52010018_QD__MAIN__2$', arg4=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 미카이동01()


class 미카이동01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=301, enable=False)
        move_npc(spawnId=1006, patrolName='MS2PatrolData_1006_B')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=103, spawnIds=[1006]):
            return 동영상재생대기()


class 동영상재생대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 동영상재생()


class 동영상재생(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='awaken.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 동영상종료대기()


class 동영상종료대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 업적발생()


class 업적발생(state.State):
    def on_enter(self):
        set_achievement(triggerId=100, type='trigger', achieve='ChangeMika')
        destroy_monster(spawnIds=[1006])
        create_monster(spawnIds=[1005], arg2=False)


