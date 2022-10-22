""" trigger/52000130_qd/52000130_main.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return 잠시대기()


class 잠시대기(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PC이동_01()


class PC이동_01(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카일과대화_01()


class 카일과대화_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카일과대화_02()


class 카일과대화_02(state.State):
    def on_enter(self):
        set_scene_skip(state=카일이동_01, arg2='nextState')
        add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__0$', duration=3000, align='right')
        # <action name="SetNpcEmotionSequence" arg1="101" arg2="Talk_A" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 카일과대화_03()


class 카일과대화_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카일과대화_04()


class 카일과대화_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000130_QD__52000130_MAIN__1$', duration=3500, align='right')
        set_pc_emotion_sequence(sequenceNames=['Talk_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 카일과대화_05()


class 카일과대화_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카일과대화_06()


class 카일과대화_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__2$', duration=3000, align='right')
        # <action name="SetNpcEmotionSequence" arg1="101" arg2="Talk_A" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3300):
            return 카일이동_01()


class 카일이동_01(state.State):
    def on_enter(self):
        set_scene_skip()
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카일이동_02()


class 카일이동_02(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카일공격_01()


class 카일공격_01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_B')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카일공격_02()


class 카일공격_02(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Emotion_Failure_A', duration=30000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 습격후대화_01()


class 습격후대화_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 습격후대화_02()


class 습격후대화_02(state.State):
    def on_enter(self):
        set_scene_skip(state=씬스킵_01, arg2='exit')
        add_cinematic_talk(npcId=0, msg='$52000130_QD__52000130_MAIN__3$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 습격후대화_03()


class 습격후대화_03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__4$', duration=3500, align='right')
        add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__5$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 습격후대화_04()


class 습격후대화_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000130_QD__52000130_MAIN__6$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 습격후대화_05()


class 습격후대화_05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__7$', duration=3500, align='right')
        add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__8$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 습격후대화_06()


class 습격후대화_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000130_QD__52000130_MAIN__9$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 습격후대화_07()


class 습격후대화_07(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__10$', duration=3500, align='right')
        add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__11$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7500):
            return 습격후대화_08()


class 습격후대화_08(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000130_QD__52000130_MAIN__12$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 페이드아웃_01()


class 페이드아웃_01(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 페이드아웃_02()


class 페이드아웃_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003371, msg='$52000130_QD__52000130_MAIN__13$', duration=5000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 강제이동()


class 씬스킵_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 강제이동()


class 강제이동(state.State):
    def on_enter(self):
        move_user(mapId=52000131, portalId=1)


