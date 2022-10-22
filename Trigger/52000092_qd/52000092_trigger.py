""" trigger/52000092_qd/52000092_trigger.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_gravity(gravity=-39)
        create_monster(spawnIds=[800], arg2=False) # 오르데 소환
        set_mesh(triggerIds=[900], visible=False)
        set_effect(triggerIds=[901], visible=False)
        set_effect(triggerIds=[902], visible=False)
        set_effect(triggerIds=[903], visible=False)
        set_effect(triggerIds=[904], visible=False)
        set_effect(triggerIds=[905], visible=False)
        set_effect(triggerIds=[906], visible=False)
        set_effect(triggerIds=[907], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 중력감지메시지()


class 퀘스트체크50100520(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[50100520], questStates=[3]):
            return 이동52000091()
        if quest_user_detected(boxIds=[9001], questIds=[50100520], questStates=[2]):
            return 이동52000091()
        if quest_user_detected(boxIds=[9001], questIds=[50100520], questStates=[1]):
            return 이동52000091()


class 중력감지메시지(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25200921, textId=25200921, duration=10000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[50100510], questStates=[1]):
            return 진행중일때20002276()
        if quest_user_detected(boxIds=[9001], questIds=[20002276], questStates=[1]):
            return 진행중일때20002276()


class 진행중일때20002276(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[900], visible=True, arg3=0, arg4=0, arg5=5000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[50100510], questStates=[2]):
            return 완료가능할때20002276()
        if quest_user_detected(boxIds=[9001], questIds=[20002276], questStates=[2]):
            return 완료가능할때20002276()


class 완료가능할때20002276(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[900], visible=False, arg3=0, arg4=0, arg5=100)
        set_effect(triggerIds=[901], visible=True)
        set_effect(triggerIds=[902], visible=True)
        set_effect(triggerIds=[903], visible=True)
        set_effect(triggerIds=[904], visible=True)
        set_effect(triggerIds=[905], visible=True)
        set_effect(triggerIds=[906], visible=True)
        set_effect(triggerIds=[907], visible=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[50100520], questStates=[2]):
            return 완료시01_50100520()
        if quest_user_detected(boxIds=[9001], questIds=[20002277], questStates=[2]):
            return None # Missing State: 완료시01_20002277


#  챕터10 [20002277]완료 시 연출, 오르데가 마법을 발동시킨다.
class 완료시01_50100520(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return None # Missing State: 완료시02_50100520


class 완료시02_20002277(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 완료시03_20002277()


class 완료시03_20002277(state.State):
    def on_enter(self):
        move_npc(spawnId=800, patrolName='MS2PatrolData_ordeMove') # 오르데 이동
        select_camera_path(pathIds=[2000,2001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 완료시04_20002277()


class 완료시04_20002277(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2002,2003,2004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 완료시05_20002277()


class 완료시05_20002277(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2005,2006], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 완료시06_20002277()


class 완료시06_20002277(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2007,2008], returnView=False)
        set_npc_emotion_sequence(spawnId=800, sequenceName='IceSphere_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 완료시07_20002277()


class 완료시07_20002277(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2009,2010], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 완료시08_20002277()


class 완료시08_20002277(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 완료20002277()


class 완료20002277(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=52000092, portalId=0)


class 이동52000091(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=52000091, portalId=0)


