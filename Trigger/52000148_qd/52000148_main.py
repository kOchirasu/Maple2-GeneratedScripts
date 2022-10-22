""" trigger/52000148_qd/52000148_main.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return 잠시대기_01()


class 잠시대기_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 잠시대기_02()


class 잠시대기_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        move_user(mapId=52000148, portalId=99)
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 잠시대기_03()


class 잠시대기_03(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=130000)
        face_emotion(spawnId=0, emotionName='Think_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 시작_01()


class 시작_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000148_QD__52000148_MAIN__0$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 시작_02()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 시작_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 시작_03()


class 시작_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 오스카와대화_01()


class 오스카와대화_01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__1$', duration=2500, align='right')
        move_npc(spawnId=101, patrolName='MS2PatrolData_2001')
        set_scene_skip(state=오스카퇴장_02, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 오스카와대화_02()


class 오스카와대화_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__2$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 오스카와대화_03()


class 오스카와대화_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__3$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 오스카와대화_04()


class 오스카와대화_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__4$', duration=3000, align='left')
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 오스카와대화_05()


class 오스카와대화_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__5$', duration=4000, align='left')
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 오스카와대화_06()


class 오스카와대화_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__6$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 오스카와대화_07()


class 오스카와대화_07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__7$', duration=3000, align='left')
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__8$', duration=4000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 오스카와대화_08()


class 오스카와대화_08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 오스카와대화_09()


class 오스카와대화_09(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__9$', duration=3000, align='right')
        add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__10$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 오스카와대화_10()


class 오스카와대화_10(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 오스카와대화_11()


class 오스카와대화_11(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__11$', duration=2500, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 오스카와대화_12()


class 오스카와대화_12(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__12$', duration=3000, align='right')
        add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__13$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 오스카와대화_13()


class 오스카와대화_13(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__14$', duration=3500, illustId='Oskhal_normal', align='left')
        add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__15$', duration=3500, illustId='Oskhal_normal', align='left')
        add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__16$', duration=2500, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16613):
            return 오스카와대화_14()


class 오스카와대화_14(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__17$', duration=2500, align='right')
        add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__18$', duration=4000, align='right')
        add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__19$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 오스카와대화_15()


class 오스카와대화_15(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__20$', duration=3000, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 오스카와대화_16()


class 오스카와대화_16(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__21$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 오스카와대화_17()


class 오스카와대화_17(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__22$', duration=3000, illustId='Oskhal_normal', align='left')
        add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__23$', duration=3000, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 오스카와대화_18()


class 오스카와대화_18(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__24$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 오스카와대화_19()


class 오스카와대화_19(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003380, msg='$52000148_QD__52000148_MAIN__25$', duration=3000, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 오스카퇴장_01()


class 오스카퇴장_01(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 오스카퇴장_02()


class 오스카퇴장_02(state.State):
    def on_enter(self):
        set_scene_skip()
        move_npc(spawnId=101, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 독백_01()


class 독백_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 독백_02()


class 독백_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__26$', duration=2500, align='right')
        set_scene_skip(state=마무리_01, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 독백_03()


class 독백_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)
        set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 독백_04()


class 독백_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__27$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 독백_05()


class 독백_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 독백_06()


class 독백_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000148_QD__52000148_MAIN__28$', duration=3500, align='right')
        face_emotion(spawnId=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 마무리_01()


class 마무리_01(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 마무리_02()


class 마무리_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000148_QD__52000148_MAIN__29$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 강제이동()


class 강제이동(state.State):
    def on_enter(self):
        move_user(mapId=2000062, portalId=13)


