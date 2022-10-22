""" trigger/52000145_qd/52000145_main.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        create_monster(spawnIds=[101], arg2=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[40002711], questStates=[3]):
            return 퀘스트2완료_01()
        if quest_user_detected(boxIds=[701], questIds=[40002711], questStates=[2]):
            return 퀘스트2진행_01()
        if quest_user_detected(boxIds=[701], questIds=[40002711], questStates=[1]):
            return 퀘스트2시작_01()
        if quest_user_detected(boxIds=[701], questIds=[40002710], questStates=[3]):
            return 퀘스트1완료가능_01()
        if quest_user_detected(boxIds=[701], questIds=[40002710], questStates=[2]):
            return 퀘스트1진행_01()
        if quest_user_detected(boxIds=[701], questIds=[40002710], questStates=[1]):
            return 퀘스트1수락_02()
        if user_detected(boxIds=[701]):
            return 영상준비_01()


class 영상준비_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 영상재생_01()


class 영상재생_01(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='common\JobIntro_Ranger.usm', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 독백_01()
        if wait_tick(waitTick=45000):
            return 독백_01()


class 독백_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000145_QD__52000145_MAIN__0$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 시작_01()


class 시작_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        # <action name="연출UI를설정한다" arg1="0"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 시작_02()

    def on_exit(self):
        set_cinematic_ui(type=2)


class 시작_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52000145, portalId=99)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 하스터숙면_01()


class 하스터숙면_01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000145_QD__52000145_MAIN__1$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 하스터숙면_02()


class 하스터숙면_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000145_QD__52000145_MAIN__2$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 하스터숙면_03()


class 하스터숙면_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 하스터숙면_04()


class 하스터숙면_04(state.State):
    def on_enter(self):
        set_scene_skip(state=퀘스트1수락_01, arg2='nextState')
        set_pc_emotion_loop(sequenceName='Talk_A', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52000145_QD__52000145_MAIN__3$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 하스터숙면_05()


class 하스터숙면_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__4$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 하스터숙면_06()


class 하스터숙면_06(state.State):
    def on_enter(self):
        face_emotion(spawnId=0, emotionName='Think_A')
        add_cinematic_talk(npcId=0, msg='$52000145_QD__52000145_MAIN__5$', duration=3000, align='right')
        # <action name="AddCinematicTalk" npcID="0" msg="$52000145_QD__52000145_MAIN__6$" duration="3000" align="right" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 퀘스트1수락_01()


class 퀘스트1수락_01(state.State):
    def on_enter(self):
        set_scene_skip()
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 퀘스트1수락_02()


class 퀘스트1수락_02(state.State):
    def on_enter(self):
        face_emotion(spawnId=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        show_guide_summary(entityId=25201456, textId=25201456)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701,702], questIds=[40002710], questStates=[1]):
            return 퀘스트1진행_00()

    def on_exit(self):
        hide_guide_summary(entityId=25201456)


class 퀘스트1진행_00(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 퀘스트1진행_01()


class 퀘스트1진행_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25201451, textId=25201451)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701,702], questIds=[40002710], questStates=[2]):
            return 퀘스트1완료가능_00()

    def on_exit(self):
        hide_guide_summary(entityId=25201451)


class 퀘스트1완료가능_00(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 퀘스트1완료가능_01()


class 퀘스트1완료가능_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25201452, textId=25201452)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701,702], questIds=[40002710], questStates=[3]):
            return 퀘스트1완료_01()

    def on_exit(self):
        hide_guide_summary(entityId=25201452)


class 퀘스트1완료_01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 퀘스트2시작_01()


class 퀘스트2시작_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25201453, textId=25201453)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701,702], questIds=[40002711], questStates=[1]):
            return 퀘스트2진행_00()

    def on_exit(self):
        hide_guide_summary(entityId=25201453)


class 퀘스트2진행_00(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 퀘스트2진행_01()


class 퀘스트2진행_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25201454, textId=25201454)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701,703], questIds=[40002711], questStates=[2]):
            return 퀘스트2완료가능_00()

    def on_exit(self):
        hide_guide_summary(entityId=25201454)


class 퀘스트2완료가능_00(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 퀘스트2완료가능_01()


class 퀘스트2완료가능_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25201455, textId=25201455)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701,702], questIds=[40002711], questStates=[3]):
            return 퀘스트2완료_01()


class 퀘스트2완료_01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=25201455)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 퀘스트2완료_02()


class 퀘스트2완료_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002], returnView=False)
        move_user(mapId=52000145, portalId=99)
        create_monster(spawnIds=[103], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 오스칼등장_01()


class 오스칼등장_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_pc_emotion_sequence(sequenceNames=['Emotion_Troubled_A'])
        move_npc(spawnId=103, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 오스칼등장_02()


class 오스칼등장_02(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Emotion_Suprise_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 오스칼등장_03()


class 오스칼등장_03(state.State):
    def on_enter(self):
        set_scene_skip(state=마무리, arg2='exit')
        face_emotion(spawnId=0, emotionName='Think_A')
        add_cinematic_talk(npcId=0, msg='$52000145_QD__52000145_MAIN__7$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 오스칼등장_04()


class 오스칼등장_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__8$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 오스칼등장_05()


class 오스칼등장_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000145_QD__52000145_MAIN__9$', duration=3000, align='right')
        add_cinematic_talk(npcId=0, msg='$52000145_QD__52000145_MAIN__10$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 오스칼등장_06()


class 오스칼등장_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__11$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5485):
            return 오스칼등장_07()


class 오스칼등장_07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 오스칼등장_08()


class 오스칼등장_08(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__12$', duration=3000, align='left')
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)
        set_npc_emotion_loop(spawnId=102, sequenceName='Sit_Down_A', duration=70000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 오스칼등장_08_1()


class 오스칼등장_08_1(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__13$', duration=2500, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 오스칼등장_09()


class 오스칼등장_09(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 오스칼등장_10()


class 오스칼등장_10(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__14$', duration=4000, illustId='Hastur_normal', align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 오스칼등장_11()


class 오스칼등장_11(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__15$', duration=3000, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 오스칼등장_12()


class 오스칼등장_12(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__16$', duration=3500, illustId='Hastur_normal', align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 오스칼등장_13()


class 오스칼등장_13(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__17$', duration=2500, illustId='Oskhal_normal', align='left')
        add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__18$', duration=3500, illustId='Oskhal_normal', align='left')
        add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__19$', duration=3000, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9500):
            return 오스칼등장_14()


class 오스칼등장_14(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__20$', duration=3000, illustId='Hastur_normal', align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 오스칼등장_15()


class 오스칼등장_15(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__21$', duration=3500, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5172):
            return 오스칼등장_16()


class 오스칼등장_16(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__22$', duration=3000, illustId='Hastur_normal', align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 오스칼등장_17()


class 오스칼등장_17(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__23$', duration=2500, illustId='Oskhal_normal', align='left')
        add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__24$', duration=3500, illustId='Oskhal_normal', align='left')
        add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__25$', duration=2500, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9742):
            return 오스칼등장_18()


class 오스칼등장_18(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__26$', duration=3000, illustId='Hastur_normal', align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 오스칼등장_19()


class 오스칼등장_19(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003380, msg='$52000145_QD__52000145_MAIN__27$', duration=3000, illustId='Oskhal_normal', align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3631):
            return 오스칼등장_20()


class 오스칼등장_20(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003189, msg='$52000145_QD__52000145_MAIN__28$', duration=3500, illustId='Hastur_normal', align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 오스칼등장_21()


class 오스칼등장_21(state.State):
    def on_enter(self):
        face_emotion(spawnId=0)
        add_cinematic_talk(npcId=0, msg='$52000145_QD__52000145_MAIN__29$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 마무리()


class 마무리(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 강제이동()


class 강제이동(state.State):
    def on_enter(self):
        move_user(mapId=52000146, portalId=1)


