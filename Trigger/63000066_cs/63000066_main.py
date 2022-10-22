""" trigger/63000066_cs/63000066_main.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True)
        create_monster(spawnIds=[102], arg2=True)
        create_monster(spawnIds=[103], arg2=True)
        create_monster(spawnIds=[104], arg2=True)
        create_monster(spawnIds=[105], arg2=True)
        create_monster(spawnIds=[111], arg2=True)
        create_monster(spawnIds=[112], arg2=True)
        create_monster(spawnIds=[113], arg2=True)
        create_monster(spawnIds=[114], arg2=True)
        create_monster(spawnIds=[115], arg2=True)
        create_monster(spawnIds=[116], arg2=True)
        set_effect(triggerIds=[5001,5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[30000351], questStates=[1]):
            return 서랍장안내()
        if quest_user_detected(boxIds=[701], questIds=[30000351], questStates=[2]):
            return 사다리안내()
        if user_detected(boxIds=[701]):
            return 종료()


class 서랍장안내(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26300661, textId=26300661)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[702], questIds=[30000351], questStates=[2]):
            return 사다리안내()


class 사다리안내(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=26300661)
        show_guide_summary(entityId=26300662, textId=26300662)
        set_effect(triggerIds=[5001,5002], visible=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[703], questIds=[30000351], questStates=[2]):
            return 암전_01()


class 암전_01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=26300662)
        set_effect(triggerIds=[5001,5002], visible=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 암전_02()


class 암전_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        move_user_path(patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 마리엔등장_01()


class 마리엔등장_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True)
        add_cinematic_talk(npcId=11004293, msg='$63000066_CS__63000066_MAIN__0$', duration=2500, align='right')
        set_scene_skip(state=스킵종료, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 마리엔등장_02()


class 마리엔등장_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 마리엔등장_03()


class 마리엔등장_03(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Emotion_Suprise_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마리엔등장_04()


class 마리엔등장_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 마리엔등장_05()


class 마리엔등장_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004293, msg='$63000066_CS__63000066_MAIN__1$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 마리엔등장_06()


class 마리엔등장_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 마리엔등장_07()


class 마리엔등장_07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004293, msg='$63000066_CS__63000066_MAIN__2$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 마리엔등장_08()


class 마리엔등장_08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 마리엔등장_09()


class 마리엔등장_09(state.State):
    def on_enter(self):
        face_emotion(spawnId=0, emotionName='Think_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 마리엔등장_10()


class 마리엔등장_10(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 마리엔등장_11()


class 마리엔등장_11(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004293, msg='$63000066_CS__63000066_MAIN__3$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 마리엔퇴장_01()


class 마리엔퇴장_01(state.State):
    def on_enter(self):
        set_scene_skip()
        destroy_monster(spawnIds=[201])
        set_effect(triggerIds=[5003], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 마리엔퇴장_02()


class 마리엔퇴장_02(state.State):
    def on_enter(self):
        face_emotion(spawnId=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 스킵종료(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        face_emotion(spawnId=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        destroy_monster(spawnIds=[201])

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_scene_skip()
        set_effect(triggerIds=[5003], visible=False)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


