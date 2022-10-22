""" trigger/52000073_qd/losteve.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9900]):
            return 퀘스트조건체크()


class 퀘스트조건체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[50001683], questStates=[3]):
            return 기본상태()
        if quest_user_detected(boxIds=[9900], questIds=[50001683], questStates=[2]):
            return 대원있음()
        if quest_user_detected(boxIds=[9900], questIds=[50001683], questStates=[1]):
            return 대원있음()
        if quest_user_detected(boxIds=[9900], questIds=[50001682], questStates=[3]):
            return 대원있음()
        if quest_user_detected(boxIds=[9900], questIds=[50001682], questStates=[2]):
            return 대원있음()
        if quest_user_detected(boxIds=[9900], questIds=[50001682], questStates=[1]):
            return 대원있음()
        if quest_user_detected(boxIds=[9900], questIds=[50001681], questStates=[3]):
            return 대원있음()
        if quest_user_detected(boxIds=[9900], questIds=[50001681], questStates=[2]):
            return 대원등장()
        if quest_user_detected(boxIds=[9900], questIds=[50001681], questStates=[1]):
            return 대원등장()
        if quest_user_detected(boxIds=[9900], questIds=[50001680], questStates=[3]):
            return 기본상태()
        if quest_user_detected(boxIds=[9900], questIds=[50001680], questStates=[2]):
            return 기본상태()
        if quest_user_detected(boxIds=[9900], questIds=[50001680], questStates=[1]):
            return 기본상태()


class 기본상태(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[401])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9900]):
            return 퀘스트조건체크()


class 대원있음(state.State):
    def on_enter(self):
        create_monster(spawnIds=[401], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return None # Missing State: 종료


class 대원등장(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[401]) # 윈 스틸던의 시체

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 대원대사()


class 대원대사(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_pcTurn')
        select_camera_path(pathIds=[8003,8004], returnView=False)
        move_npc(spawnId=401, patrolName='MS2PatrolData_2001')
        add_cinematic_talk(npcId=11003446, illustId='0', msg='$52000073_QD__LOSTEVE__0$', duration=4000, align='right') # 호르헤 대사
        face_emotion(spawnId=101, emotionName='Upset')
        set_scene_skip(state=연출종료, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 카트반대사()


class 카트반대사(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11000044, illustId='0', msg='$52000073_QD__LOSTEVE__1$', duration=4000, align='right') # 호르헤 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_scene_skip()
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return None # Missing State: 종료


