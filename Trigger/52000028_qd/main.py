""" trigger/52000028_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[604], visible=False)
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014], arg2=False)
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3002], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[101], questIds=[20002250], questStates=[1], jobCode=90):
            return 연출시작()
        if quest_user_detected(boxIds=[101], questIds=[20002251], questStates=[1], jobCode=90):
            return NPC이동01()
        if quest_user_detected(boxIds=[101], questIds=[10002931], questStates=[1]):
            return 연출시작()
        if quest_user_detected(boxIds=[101], questIds=[10002932], questStates=[1]):
            return NPC이동01()


class 연출시작(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아시모프이동()


class 아시모프이동(state.State):
    def on_enter(self):
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001_A')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[1001]):
            return 책장변경()


class 책장변경(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3002], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 동영상재상()


class 동영상재상(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='Starlight_expedition.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 이슈라대사01()


class 이슈라대사01(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        set_effect(triggerIds=[601], visible=True)
        set_conversation(type=2, spawnId=11001244, script='$52000028_QD__MAIN__0$', arg4=5, arg5=0) # 음성 코드 00001294

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5500):
            return 이슈라대사02()


class 이슈라대사02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=True)
        set_conversation(type=2, spawnId=11001244, script='$52000028_QD__MAIN__1$', arg4=6, arg5=0) # 음성 코드 00001295

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 아시모프대사01()


class 아시모프대사01(state.State):
    def on_enter(self):
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1001_B')
        set_effect(triggerIds=[603], visible=True)
        set_conversation(type=2, spawnId=11000031, script='$52000028_QD__MAIN__2$', arg4=3, arg5=0) # 음성 코드 00001343

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 아시모프대사02()


class 아시모프대사02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True)
        set_conversation(type=2, spawnId=11000031, script='$52000028_QD__MAIN__3$', arg4=6, arg5=0) # 음성 코드 00001344

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 퀘스트수락대기()

    def on_exit(self):
        set_achievement(triggerId=101, type='trigger', achieve='BackstoryOfRune')
        select_camera(triggerId=301, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 퀘스트수락대기(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[101], questIds=[20002251], questStates=[1], jobCode=90):
            return NPC이동01()
        if quest_user_detected(boxIds=[101], questIds=[10002932], questStates=[1]):
            return NPC이동01()


class NPC이동01(state.State):
    def on_enter(self):
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_A')
        move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_A')
        move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NPC이동02()


class NPC이동02(state.State):
    def on_enter(self):
        move_npc(spawnId=1008, patrolName='MS2PatrolData_1008_A')
        move_npc(spawnId=1013, patrolName='MS2PatrolData_1013_A')
        move_npc(spawnId=1014, patrolName='MS2PatrolData_1014_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 종료()


class 종료(state.State):
    pass


