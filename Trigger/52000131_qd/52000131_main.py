""" trigger/52000131_qd/52000131_main.xml """
from common import *
import state


class 준비(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return 침대로이동()


class 침대로이동(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_0sec.xml')
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=52000131, portalId=99)
        set_cinematic_ui(type=1)
        # <action name="연출UI를설정한다" arg1="3"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라이동_01()


class 카메라이동_01(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=80000)
        face_emotion(spawnId=0, emotionName='Think_A')
        select_camera_path(pathIds=[8001], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_0sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 페이드인1_01()


class 페이드인1_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 독백_01()


class 독백_01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$52000131_QD__52000131_MAIN__0$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카메라이동1_01()


class 카메라이동1_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 버튼등장_01()


class 버튼등장_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 버튼등장_02()


class 버튼등장_02(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 버튼등장_03()


class 버튼등장_03(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 버튼과대화_01()


class 버튼과대화_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 버튼과대화_02()


class 버튼과대화_02(state.State):
    def on_enter(self):
        set_scene_skip(state=마무리, arg2='exit')
        add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__1$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 버튼과대화_03()


class 버튼과대화_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        face_emotion(spawnId=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 버튼과대화_04()


class 버튼과대화_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000131_QD__52000131_MAIN__2$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 버튼과대화_05()


class 버튼과대화_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 버튼과대화_06()


class 버튼과대화_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__3$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 버튼과대화_07()


class 버튼과대화_07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 버튼과대화_08()


class 버튼과대화_08(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000131_QD__52000131_MAIN__4$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 버튼과대화_09()


class 버튼과대화_09(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 버튼과대화_10()


class 버튼과대화_10(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__5$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 버튼과대화_11()


class 버튼과대화_11(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 버튼과대화_12()


class 버튼과대화_12(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000131_QD__52000131_MAIN__6$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 버튼과대화_13()


class 버튼과대화_13(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 버튼과대화_14()


class 버튼과대화_14(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__7$', duration=4000, align='right')
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 버튼과대화_15()


class 버튼과대화_15(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000131_QD__52000131_MAIN__8$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 버튼과대화_16()


class 버튼과대화_16(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__9$', duration=4000, align='right')
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 버튼과대화_17()


class 버튼과대화_17(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000131_QD__52000131_MAIN__10$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 버튼과대화_18()


class 버튼과대화_18(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__11$', duration=3000, align='right')
        add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__12$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 버튼과대화_19()


class 버튼과대화_19(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__13$', duration=3000, align='right')
        add_cinematic_talk(npcId=11001540, msg='$52000131_QD__52000131_MAIN__14$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 버튼과대화_20()


class 버튼과대화_20(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 버튼과대화_21()


class 버튼과대화_21(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000131_QD__52000131_MAIN__15$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 마무리()


class 마무리(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 강제이동()


class 강제이동(state.State):
    def on_enter(self):
        move_user(mapId=2000062, portalId=13)


