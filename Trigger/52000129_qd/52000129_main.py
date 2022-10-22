""" trigger/52000129_qd/52000129_main.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True)
        create_monster(spawnIds=[102], arg2=True)
        create_monster(spawnIds=[103], arg2=True)
        create_monster(spawnIds=[104], arg2=True)
        set_effect(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[40002691], questStates=[1]):
            return 퀘스트진행_01()
        if quest_user_detected(boxIds=[701], questIds=[40002691], questStates=[2]):
            return 퀘스트완료가능_01()
        if quest_user_detected(boxIds=[701], questIds=[40002691], questStates=[3]):
            return 페이드아웃_01()
        if user_detected(boxIds=[701]):
            return 잠시대기()


class 잠시대기(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라이동_01()


class 카메라이동_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 카메라이동_02()


class 카메라이동_02(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$52000129_QD__52000129_MAIN__0$', desc='$52000129_QD__52000129_MAIN__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 카메라리셋_01()


class 카메라리셋_01(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 계단타고이동_01()


class 계단타고이동_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        show_guide_summary(entityId=25201291, textId=25201291)
        set_effect(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702]):
            return 퀘스트받기_01()


class 퀘스트받기_01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=25201291)
        set_effect(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011], visible=False)
        show_guide_summary(entityId=25201292, textId=25201292)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[702], questIds=[40002691], questStates=[1]):
            return 퀘스트진행_01()


class 퀘스트진행_01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=25201291)
        hide_guide_summary(entityId=25201292)
        show_guide_summary(entityId=25201293, textId=25201293)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[702], questIds=[40002691], questStates=[2]):
            return 퀘스트완료가능_01()


class 퀘스트완료가능_01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=25201291)
        hide_guide_summary(entityId=25201292)
        hide_guide_summary(entityId=25201293)
        show_guide_summary(entityId=25201294, textId=25201294)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[702], questIds=[40002691], questStates=[3]):
            return 페이드아웃_01()


class 페이드아웃_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        hide_guide_summary(entityId=25201291)
        hide_guide_summary(entityId=25201292)
        hide_guide_summary(entityId=25201293)
        hide_guide_summary(entityId=25201294)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 페이드아웃_02()


class 페이드아웃_02(state.State):
    def on_enter(self):
        move_user(mapId=52000129, portalId=99)
        create_monster(spawnIds=[105], arg2=True)
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 페이드인_01()


class 페이드인_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMaskEff_fadein_1sec.xml')
        set_pc_emotion_sequence(sequenceNames=['Talk_A'])
        set_scene_skip(state=마무리, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 감시_01()


class 감시_01(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Talk_A'])
        set_conversation(type=1, spawnId=101, script='$52000129_QD__52000129_MAIN__2$', arg4=2, arg5=0)
        move_npc(spawnId=105, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 감시_02()


class 감시_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002,8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 감시_03()


class 감시_03(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2002')
        set_conversation(type=1, spawnId=102, script='$52000129_QD__52000129_MAIN__3$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 마무리()


class 마무리(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_0sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 강제이동()


class 강제이동(state.State):
    def on_enter(self):
        move_user(mapId=52000130, portalId=1)


