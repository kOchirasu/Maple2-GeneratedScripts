""" trigger/52000150_qd/contents_trigger.xml """
from common import *
import state


class 차원의숲전경씬종료(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='52000150', value=1):
            return 웨이브1알림()


#  ########################전투 컨텐츠 시작, 웨이브1########################
class 웨이브1알림(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2400,2401,2402,2403,2404], visible=True, arg3=0, arg4=200) # #####1번 지역 리젠 알림#####
        set_effect(triggerIds=[2606], visible=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10010], questIds=[50001641], questStates=[2]):
            return 컨텐츠종료01()
        if wait_tick(waitTick=2000):
            return 웨이브1생성()


class 웨이브1생성(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[400,401,402,403,404]):
            return 웨이브2알림()


#  #######################웨이브2########################
class 웨이브2알림(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2500,2501,2502,2503,2504], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2606], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 웨이브2생성()


class 웨이브2생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[500,501,502,503,504], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[500,501,502,503,504]):
            return 웨이브3알림()


#  ########################웨이브3########################
class 웨이브3알림(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2600,2601,2602,2603,2604], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2606], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 웨이브3생성()


class 웨이브3생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[600,601,602,603,604], arg2=False)
        set_effect(triggerIds=[2606], visible=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[600,601,602,603,604]):
            return 웨이브4알림()


#  ########################웨이브4########################
class 웨이브4알림(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2300,2301,2302,2303,2304], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2606], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 웨이브4생성()


class 웨이브4생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[300,301,302,303,304], arg2=False)
        set_effect(triggerIds=[2606], visible=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[300,301,302,303,304]):
            return 웨이브5알림()


#  ########################웨이브5, 1번/3번지역 동시 등장########################
class 웨이브5알림(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2400,2401,2402,2403,2404], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2600,2601,2602,2603,2604], visible=True, arg3=0, arg4=200) # #####1번 지역 리젠 알림#####
        set_effect(triggerIds=[2606], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 웨이브5생성()


class 웨이브5생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[600,601,602,603,604], arg2=False)
        create_monster(spawnIds=[400,401,402,403,404], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[600,601,602,603,604,400,401,402,403,404]):
            return 웨이브6알림()


#  ########################웨이브6, 2번/4번지역 동시 등장########################
class 웨이브6알림(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2500,2501,2502,2503,2504], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2300,2301,2302,2303,2304], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2606], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 웨이브6생성()


class 웨이브6생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[500,501,502,503,504], arg2=False)
        create_monster(spawnIds=[300,301,302,303,304], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[300,301,302,303,304,500,501,502,503,504]):
            return 웨이브7알림()


#  ########################웨이브7, 전 지역 동시 등장########################
class 웨이브7알림(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2300,2301,2302,2303,2304], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2400,2401,2402,2403,2404], visible=True, arg3=0, arg4=200) # #####1번 지역 리젠 알림#####
        set_effect(triggerIds=[2500,2501,2502,2503,2504], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2600,2601,2602,2603,2604], visible=True, arg3=0, arg4=200) # #####2번 지역 리젠 알림#####
        set_effect(triggerIds=[2606], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 웨이브7생성()


class 웨이브7생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[300,301,302,303,304], arg2=False)
        create_monster(spawnIds=[400,401,402,403,404], arg2=False)
        create_monster(spawnIds=[500,501,502,503,504], arg2=False)
        create_monster(spawnIds=[600,601,602,603,604], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[300,301,302,303,304,400,401,402,403,404,500,501,502,503,504,600,601,602,603,604]):
            return 컨텐츠종료01()


#  ########################컨텐츠종료01########################
class 컨텐츠종료01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[300,301,302,303,304,400,401,402,403,404,500,501,502,503,504,600,601,602,603,604])
        set_cinematic_ui(type=1)
        set_time_scale(enable=True, startScale=0.1, endScale=0.5, duration=10, interpolator=1) # 2초간 느려지기 시작

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 컨텐츠종료02()


class 컨텐츠종료02(state.State):
    def on_enter(self):
        set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        set_effect(triggerIds=[2607], visible=False)
        destroy_monster(spawnIds=[700])
        create_monster(spawnIds=[202], arg2=False)
        move_npc(spawnId=202, patrolName='MS2PatrolData_caitMove01') # 케이틀린 이동
        set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_A') # 호르헤
        set_npc_emotion_loop(spawnId=200, sequenceName='Event_01_A', duration=999999)
        set_user_value(triggerId=10000, key='52000150monster', value=1) # 통신 : 몬스터 다 잡으면 쏴주는 신호

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 컨텐츠종료03()


class 컨텐츠종료03(state.State):
    def on_enter(self):
        set_onetime_effect(id=20, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        # <action name="연출UI를설정한다" arg1="0"/>
        # <action name="연출UI를설정한다" arg1="2"/>
        set_user_value(triggerId=10000, key='52000150monster', value=0)


