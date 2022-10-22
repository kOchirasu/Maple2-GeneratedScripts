""" trigger/52010056_qd/eventsection_b.xml """
from common import *
import state


class Idle(state.State):
    def on_tick(self) -> state.State:
        if true():
            return Ready()


class Ready(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2004]):
            return 연출준비_A()


class 연출준비_A(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        add_buff(boxIds=[2001], skillId=70000085, level=1, arg4=False, arg5=True) # 연출용 무적 버프
        add_buff(boxIds=[2001], skillId=70000085, level=1, arg4=False, arg5=False) # 연출용 무적 버프

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 연출준비_B()


class 연출준비_B(state.State):
    def on_enter(self):
        create_monster(spawnIds=[999], arg2=False) # 크림슨 스피어: 29000386
        select_camera_path(pathIds=[4004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 경비병_스폰()


class 경비병_스폰(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_sequence(spawnId=121, sequenceName='Attack_01_B')
        add_cinematic_talk(npcId=11003816, msg='$52010056_QD__EventSection_B__0$', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 경비병_이동시작()


class 경비병_이동시작(state.State):
    def on_enter(self):
        move_npc(spawnId=999, patrolName='MS2PatrolData_3008')
        select_camera_path(pathIds=[4005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 조작_시작()


class 조작_시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)
        remove_buff(boxId=2001, skillId=70000107)
        set_event_ui(type=1, arg2='$52010056_QD__EventSection_B__1$', arg3='3000', arg4='0')

    def on_exit(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_sound(triggerId=7001, arg2=False)


