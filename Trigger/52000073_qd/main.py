""" trigger/52000073_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[60100115], questStates=[1]):
            return 레논등장()


class 레논등장(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG\weather\Eff_monochrome_03.xml') # 연출 3 : 레터박스 
			연출 1 : 플레이어 조작 뺏기
        set_sound(triggerId=7001, arg2=True)
        destroy_monster(spawnIds=[101])
        visible_my_pc(isVisible=False)
        set_ambient_light(primary=[0,0,0])
        set_ambient_light(primary=[1,1,1])
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[302]) # 윈 스틸던의 시체
        create_monster(spawnIds=[301]) # 레논
        select_camera_path(pathIds=[8001,8002], returnView=False)
        set_scene_skip(state=다크윈드통로, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 계단이동()


class 계단이동(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003,8004], returnView=False)
        move_npc(spawnId=301, patrolName='MS2PatrolData_2001')
        set_conversation(type=1, spawnId=301, script='$52000073_QD__MAIN__0$', arg4=3, arg5=0) # 레논 계단 올라가며 하는 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 시체발견()


class 시체발견(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=301, script='$52000073_QD__MAIN__1$', arg4=2, arg5=0)
        move_npc(spawnId=301, patrolName='MS2PatrolData_2002')
        select_camera_path(pathIds=[8005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 의문()


class 의문(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=301, script='$52000073_QD__MAIN__2$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 상황파악()


class 상황파악(state.State):
    def on_enter(self):
        set_sound(triggerId=7002, arg2=True)
        select_camera_path(pathIds=[8006], returnView=False) # 카메라 레논 얼굴로
        set_conversation(type=1, spawnId=301, script='$52000073_QD__MAIN__3$', arg4=3, arg5=0)
        set_npc_emotion_loop(spawnId=301, sequenceName='Sit_down_A', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 현장목격()


class 현장목격(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8007], returnView=False) # 레논 뒤편으로
        create_monster(spawnIds=[303]) # 다크윈드 대원 좌
        create_monster(spawnIds=[304]) # 다크윈드 대원 우
        set_conversation(type=1, spawnId=303, script='$52000073_QD__MAIN__4$', arg4=3, arg5=0)
        set_npc_emotion_loop(spawnId=303, sequenceName='Attack_Idle_A', duration=1500) # 다크윈드 대원 좌 모션
        set_npc_emotion_loop(spawnId=304, sequenceName='Attack_Idle_A', duration=1500) # 다크윈드 대원 우 모션
        move_npc(spawnId=301, patrolName='MS2PatrolData_2005')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 오해1()


class 오해1(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=303, script='$52000073_QD__MAIN__5$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=304, script='$52000073_QD__MAIN__6$', arg4=3, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 오해2()


class 오해2(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=303, script='$52000073_QD__MAIN__7$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=301, script='$52000073_QD__MAIN__8$', arg4=3, arg5=1)
        set_npc_emotion_loop(spawnId=303, sequenceName='Attack_01_A', duration=2000) # 다크윈드 대원 좌 모션
        set_npc_emotion_loop(spawnId=301, sequenceName='Talk_A', duration=3000) # 레논 대화 모션

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 오해3()


class 오해3(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=303, script='$52000073_QD__MAIN__9$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=304, script='$52000073_QD__MAIN__10$', arg4=3, arg5=2)
        move_npc(spawnId=303, patrolName='MS2PatrolData_2003')
        move_npc(spawnId=304, patrolName='MS2PatrolData_2004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 오해4()


class 오해4(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=303, sequenceName='Attack_Idle_A', duration=5000) # 다크윈드 대원 좌 모션
        set_conversation(type=1, spawnId=303, script='$52000073_QD__MAIN__11$', arg4=3, arg5=0)
        set_npc_emotion_loop(spawnId=304, sequenceName='Attack_Idle_A', duration=5000) # 다크윈드 대원 우 모션

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 오해5()


class 오해5(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=301, script='$52000073_QD__MAIN__12$', arg4=5, arg5=0)
        move_npc(spawnId=301, patrolName='MS2PatrolData_2006')
        set_npc_emotion_loop(spawnId=303, sequenceName='Attack_Idle_A', duration=6000) # 다크윈드 대원 좌 모션
        set_npc_emotion_loop(spawnId=304, sequenceName='Attack_Idle_A', duration=6000) # 다크윈드 대원 우 모션

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 쓰러짐()


class 쓰러짐(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=303, sequenceName='Down_Idle_A', duration=500000) # 다크윈드 대원 좌 모션
        set_npc_emotion_loop(spawnId=304, sequenceName='Down_Idle_A', duration=500000) # 다크윈드 대원 우 모션

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 탈출()


class 탈출(state.State):
    def on_enter(self):
        move_npc(spawnId=301, patrolName='MS2PatrolData_2007')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 레논탈출()


class 레논탈출(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[301])
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라시점변경_ready()


class 카메라시점변경_ready(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카메라시점변경()


class 카메라시점변경(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[8008], returnView=False) # 공중뷰

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카트반등장()


class 카트반등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[305]) # 카트반

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카트반이동()


class 카트반이동(state.State):
    def on_enter(self):
        move_npc(spawnId=305, patrolName='MS2PatrolData_2008')
        set_conversation(type=1, spawnId=305, script='$52000073_QD__MAIN__13$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 의미심장()


class 의미심장(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11001024, msg='$52000073_QD__MAIN__14$', duration=3000, align='center')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 다크윈드통로()


class 다크윈드통로(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=True)
        create_monster(spawnIds=[101])
        destroy_monster(spawnIds=[301,302,303,304,305])
        set_cinematic_ui(type=2)
        move_user(mapId=52000138, portalId=0)


