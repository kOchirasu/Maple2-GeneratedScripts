""" trigger/52000139_qd/main.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0) # 유저 이동 하게
        set_cinematic_ui(type=2) # UI 복구
        create_monster(spawnIds=[109], arg2=True)
        create_monster(spawnIds=[110], arg2=True)
        create_monster(spawnIds=[101], arg2=True)
        create_monster(spawnIds=[102], arg2=True)
        create_monster(spawnIds=[104], arg2=True)
        create_monster(spawnIds=[105], arg2=True)
        create_monster(spawnIds=[106], arg2=True)
        create_monster(spawnIds=[107], arg2=True)
        set_effect(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014], visible=False) # 경로 안내

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[40002700], questStates=[3]):
            return 다시검은화면_01()
        if quest_user_detected(boxIds=[701], questIds=[40002700], questStates=[2]):
            return 퀘스트진행_01()
        if quest_user_detected(boxIds=[701], questIds=[40002700], questStates=[1]):
            return 퀘스트수락_02()
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
        play_scene_movie(fileName='common\JobIntro_Priest.usm', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 영상마무리_01()
        if wait_tick(waitTick=53000):
            return 영상마무리_01()


class 영상마무리_01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라연출_01()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 카메라연출_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)
        set_cinematic_ui(type=1) # 유저 이동 못하게

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라연출_02()


class 카메라연출_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001,8002], returnView=False)
        set_pc_emotion_loop(sequenceName='Emotion_Disappoint_Idle_A', duration=14000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 카메라연출_03()


class 카메라연출_03(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$52000139_QD__MAIN__22$', desc='$52000139_QD__MAIN__23$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 검은화면전환_01()


class 검은화면전환_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 검은화면전환_02()


class 검은화면전환_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=3) # 상하 레터박스
        select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 밝은화면전환_01()


class 밝은화면전환_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_pc_emotion_loop(sequenceName='Emotion_Disappoint_Idle_A', duration=2000)
        move_npc(spawnId=101, patrolName='MS2PatrolData_2001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 기사와대화_00()


class 기사와대화_00(state.State):
    def on_enter(self):
        set_scene_skip(state=퀘스트수락_01, arg2='nextState')
        add_cinematic_talk(npcId=11003320, msg='$52000139_QD__MAIN__0$', duration=2500, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 기사와대화_01()


class 기사와대화_01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000139_QD__MAIN__1$', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 기사와대화_02()


class 기사와대화_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003320, msg='$52000139_QD__MAIN__2$', duration=2500, align='left')
        add_cinematic_talk(npcId=11003320, msg='$52000139_QD__MAIN__3$', duration=2500, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5500):
            return 기사와대화_03()


class 기사와대화_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000139_QD__MAIN__4$', duration=2500)
        add_cinematic_talk(npcId=0, msg='$52000139_QD__MAIN__5$', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5500):
            return 기사와대화_04()


class 기사와대화_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003320, msg='$52000139_QD__MAIN__6$', duration=3000, align='left')
        move_npc(spawnId=102, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 기사와대화_05()


class 기사와대화_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000139_QD__MAIN__7$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 기사와대화_06()


class 기사와대화_06(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2003')
        move_user_path(patrolName='MS2PatrolData_2004')
        add_cinematic_talk(npcId=11003321, msg='$52000139_QD__MAIN__8$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 기사와대화_07()


class 기사와대화_07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003320, msg='$52000139_QD__MAIN__9$', duration=2500, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 퀘스트수락_01()


class 퀘스트수락_01(state.State):
    def on_enter(self):
        set_scene_skip()
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=0) # 유저 이동 가능하게
        set_cinematic_ui(type=2) # UI 원상복구
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[103], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 퀘스트수락_02()


class 퀘스트수락_02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25201394, textId=25201394)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[40002700], questStates=[1]):
            return 기지로이동_01()

    def on_exit(self):
        hide_guide_summary(entityId=25201394)


class 기지로이동_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014], visible=True) # 경로 안내
        show_guide_summary(entityId=25201391, textId=25201391)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[702], questIds=[40002700], questStates=[1]):
            return 퀘스트진행_01()

    def on_exit(self):
        hide_guide_summary(entityId=25201391)


class 퀘스트진행_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014], visible=False)
        show_guide_summary(entityId=25201392, textId=25201392)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701,702], questIds=[40002700], questStates=[2]):
            return 퀘스트완료가능_01()

    def on_exit(self):
        destroy_monster(spawnIds=[107])
        create_monster(spawnIds=[108], arg2=False)


class 퀘스트완료가능_01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=25201392)
        show_guide_summary(entityId=25201393, textId=25201393)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[702], questIds=[40002700], questStates=[3]):
            return 다시검은화면_01()


class 다시검은화면_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52000139, portalId=99)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 다시검은화면_02()


class 다시검은화면_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[8004], returnView=False)
        move_user_path(patrolName='MS2PatrolData_2005')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 부상병과대화_01()


class 부상병과대화_01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=25201393)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003327, msg='$52000139_QD__MAIN__13$', duration=3000)
        set_scene_skip(state=마무리, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 부상병과대화_02()


class 부상병과대화_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000139_QD__MAIN__14$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 부상병과대화_03()


class 부상병과대화_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003327, msg='$52000139_QD__MAIN__15$', duration=2500)
        add_cinematic_talk(npcId=11003327, msg='$52000139_QD__MAIN__16$', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5300):
            return 부상병과대화_04()


class 부상병과대화_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000139_QD__MAIN__17$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 부상병과대화_05()


class 부상병과대화_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003327, msg='$52000139_QD__MAIN__18$', duration=2500)
        add_cinematic_talk(npcId=11003327, msg='$52000139_QD__MAIN__19$', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5300):
            return 부상병과대화_06()


class 부상병과대화_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000139_QD__MAIN__20$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 부상병과대화_07()


class 부상병과대화_07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004,8005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2300):
            return 부상병과대화_08()


class 부상병과대화_08(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$52000139_QD__MAIN__21$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
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
        move_user(mapId=52000140, portalId=1)


