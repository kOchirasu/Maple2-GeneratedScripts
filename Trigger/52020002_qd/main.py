""" trigger/52020002_qd/main.xml """
from common import *
import state


class start(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4001,4002], visible=True)
        destroy_monster(spawnIds=[120,121])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 퀘스트조건체크()


class 퀘스트조건체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001779], questStates=[3]):
            return 진행이후_기본()
        if quest_user_detected(boxIds=[9000], questIds=[50001775,50001776,50001777,50001778,50001779], questStates=[1,2]):
            return 제이든보고연출_완료()
        if quest_user_detected(boxIds=[9000], questIds=[50001774], questStates=[3]):
            return 제이든보고연출_완료()
        if quest_user_detected(boxIds=[9000], questIds=[50001774], questStates=[2]):
            return 제이든보고연출_완료()
        if quest_user_detected(boxIds=[9000], questIds=[50001774], questStates=[1]):
            return 제이든보고연출_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001773], questStates=[3]):
            return 기본()


class 기본(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 진행이후_기본(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4001,4002], visible=False)
        destroy_monster(spawnIds=[120,121])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 제이든보고연출_대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[120], arg2=False)
        set_mesh(triggerIds=[4001,4002], visible=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 연출준비()


class 연출준비(state.State):
    def on_enter(self):
        move_user(mapId=52020002, portalId=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        visible_my_pc(isVisible=False) # 유저 투명 처리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        set_scene_skip(state=제이든보고_스킵완료, arg2='nextState') # setsceneskip set

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 제이든등장()


class 제이든등장(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003540, illustId='Jaiden_normal', msg='안녕하세요? 제가 나타났습니다.\n연출은 제작 중이니 기다려 주세요.', duration=3000)
        set_npc_emotion_loop(spawnId=120, sequenceName='Talk_A', duration=3000)
        set_skip(state=skip01)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 제이든보고_스킵완료()


class skip01(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 제이든보고_스킵완료()


class 제이든보고_스킵완료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        destroy_monster(spawnIds=[120])
        create_monster(spawnIds=[121], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_achievement(triggerId=9000, type='trigger', achieve='JaidenReportstoRadin')
        reset_camera(interpolationTime=2)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        visible_my_pc(isVisible=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 제이든보고연출_완료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[120])
        create_monster(spawnIds=[121], arg2=False)
        set_mesh(triggerIds=[4001,4002], visible=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출종료()


class 종료(state.State):
    pass


