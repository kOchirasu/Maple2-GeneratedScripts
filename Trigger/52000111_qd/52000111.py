""" trigger/52000111_qd/52000111.xml """
from common import *
import state


class 입장(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10011]):
            return START()


class START(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8000], visible=False)
        set_effect(triggerIds=[8001], visible=False)
        set_effect(triggerIds=[8002], visible=False)
        set_effect(triggerIds=[8003], visible=False)
        set_effect(triggerIds=[8004], visible=False)
        set_effect(triggerIds=[8005], visible=False)
        set_effect(triggerIds=[8006], visible=False)
        set_effect(triggerIds=[8007], visible=False)
        set_effect(triggerIds=[8008], visible=False)
        set_effect(triggerIds=[8009], visible=False)
        set_effect(triggerIds=[8010], visible=False)
        set_effect(triggerIds=[8011], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002315], questStates=[2]):
            return 어쌔신탈출02()
        if quest_user_detected(boxIds=[10011], questIds=[20002313], questStates=[2]):
            return PC대탈출01()
        if quest_user_detected(boxIds=[10011], questIds=[20002313], questStates=[3]):
            return PC대탈출01()
        if quest_user_detected(boxIds=[10011], questIds=[20002314], questStates=[2]):
            return PC대탈출01()
        if not quest_user_detected(boxIds=[10011], questIds=[20002313], questStates=[2]):
            return Wait()
        if quest_user_detected(boxIds=[10011], questIds=[20002312], questStates=[3]):
            return PC대탈출01()


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[5300], visible=False)
        set_effect(triggerIds=[5301], visible=False)
        set_effect(triggerIds=[5302], visible=False)
        set_effect(triggerIds=[5303], visible=False)
        set_effect(triggerIds=[5304], visible=False)
        set_effect(triggerIds=[5305], visible=False)
        set_effect(triggerIds=[5306], visible=False)
        set_effect(triggerIds=[5307], visible=False)
        set_effect(triggerIds=[5308], visible=False)
        set_effect(triggerIds=[5309], visible=False)
        set_effect(triggerIds=[5310], visible=False)
        set_effect(triggerIds=[5311], visible=False)
        set_effect(triggerIds=[5312], visible=False)
        set_effect(triggerIds=[5313], visible=False)
        set_effect(triggerIds=[5314], visible=False)
        set_effect(triggerIds=[5315], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10011]):
            return 영상준비_01()


class 영상준비_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        move_user(mapId=52000111, portalId=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 영상재생()


class 영상재생(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='common\JobIntro_Assassin.usm', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 커닝시티전경씬01()
        if wait_tick(waitTick=55000):
            return 커닝시티전경씬01()


class 커닝시티전경씬01(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_1, arg2='nextState')
        select_camera_path(pathIds=[1000,1001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 커닝시티전경씬01_B()


class 커닝시티전경씬01_B(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1002,1003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 커닝시티전경씬02()


class 커닝시티전경씬02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1004,1005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 커닝시티전경씬03()


class 커닝시티전경씬03(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$52000111_QD__52000111__0$', desc='$52000111_QD__52000111__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=7000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 커닝시티전경씬04()


class 커닝시티전경씬04(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit01()


class Quit01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit01_1()


class Quit01_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit02()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit02()


class Quit02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        set_effect(triggerIds=[5300], visible=True)
        set_effect(triggerIds=[5301], visible=True)
        set_effect(triggerIds=[5302], visible=True)
        set_effect(triggerIds=[5303], visible=True)
        set_effect(triggerIds=[5304], visible=True)
        set_effect(triggerIds=[5305], visible=True)
        set_effect(triggerIds=[5306], visible=True)
        set_effect(triggerIds=[5307], visible=True)
        set_effect(triggerIds=[5308], visible=True)
        set_effect(triggerIds=[5309], visible=True)
        set_effect(triggerIds=[5310], visible=True)
        set_effect(triggerIds=[5311], visible=True)
        set_effect(triggerIds=[5312], visible=True)
        set_effect(triggerIds=[5313], visible=True)
        set_effect(triggerIds=[5314], visible=True)
        set_effect(triggerIds=[5315], visible=True)
        add_balloon_talk(spawnId=0, msg='$52000111_QD__52000111__2$', duration=6000, delayTick=1000)
        show_guide_summary(entityId=25201111, textId=25201111, duration=10000)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10012]):
            return 쉐도우클로등장씬01()


#  ########################씬2 쉐도우클로 등장########################
class 쉐도우클로등장씬01(state.State):
    def on_enter(self):
        set_sound(triggerId=9000, arg2=True)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 쉐도우클로등장씬02()


class 쉐도우클로등장씬02(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_2, arg2='nextState')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_npc(spawnId=2000, patrolName='MS2PatrolData_pcFront')
        add_balloon_talk(spawnId=0, msg='$52000111_QD__52000111__3$', duration=6000, delayTick=1000)
        set_pc_emotion_loop(sequenceName='Assassin_Bore_A', duration=25000)
        select_camera_path(pathIds=[1006,1007], returnView=False)
        move_user(mapId=52000111, portalId=10)
        set_effect(triggerIds=[5300], visible=False)
        set_effect(triggerIds=[5301], visible=False)
        set_effect(triggerIds=[5302], visible=False)
        set_effect(triggerIds=[5303], visible=False)
        set_effect(triggerIds=[5304], visible=False)
        set_effect(triggerIds=[5305], visible=False)
        set_effect(triggerIds=[5306], visible=False)
        set_effect(triggerIds=[5307], visible=False)
        set_effect(triggerIds=[5308], visible=False)
        set_effect(triggerIds=[5309], visible=False)
        set_effect(triggerIds=[5310], visible=False)
        set_effect(triggerIds=[5311], visible=False)
        set_effect(triggerIds=[5312], visible=False)
        set_effect(triggerIds=[5313], visible=False)
        set_effect(triggerIds=[5314], visible=False)
        set_effect(triggerIds=[5315], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 쉐도우클로등장씬04()


class 쉐도우클로등장씬04(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Assassin_Bore_A'])
        add_balloon_talk(spawnId=0, msg='$52000111_QD__52000111__4$', duration=6000, delayTick=1000)
        select_camera_path(pathIds=[1012,1013], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 쉐도우클로등장씬05()


class 쉐도우클로등장씬05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8000], visible=True)
        set_effect(triggerIds=[8001], visible=True)
        set_effect(triggerIds=[8002], visible=True)
        set_effect(triggerIds=[8003], visible=True)
        set_effect(triggerIds=[8004], visible=True)
        set_effect(triggerIds=[8005], visible=True)
        set_effect(triggerIds=[8006], visible=True)
        set_effect(triggerIds=[8007], visible=True)
        set_effect(triggerIds=[8008], visible=True)
        set_effect(triggerIds=[8009], visible=True)
        select_camera_path(pathIds=[1014,1015], returnView=False)
        spawn_npc_range(rangeIds=[202,203,204,205,206,207,208,209,210,211], isAutoTargeting=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 쉐도우클로등장씬06()


class 쉐도우클로등장씬06(state.State):
    def on_enter(self):
        set_effect(triggerIds=[8010], visible=True)
        create_monster(spawnIds=[200], arg2=False)
        select_camera_path(pathIds=[1016,1017], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 쉐도우클로등장씬07()


class 쉐도우클로등장씬07(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=200, sequenceName='Sit_Down_A', duration=4000)
        select_camera_path(pathIds=[1018,1019], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 쉐도우클로등장씬09()


class 쉐도우클로등장씬09(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=200, sequenceName='Bore_A')
        select_camera_path(pathIds=[1020,1021], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 쉐도우클로등장씬11()


class 쉐도우클로등장씬11(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[1022,1023], returnView=False)
        show_caption(type='NameCaption', title='$52000111_QD__52000111__5$', desc='$52000111_QD__52000111__6$', align='center', offsetRateX=-0.15, offsetRateY=0.15, duration=10000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 쉐도우클로등장씬11_1()


class 쉐도우클로등장씬11_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 쉐도우클로등장씬12()


class Skip_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_npc(spawnId=2000, patrolName='MS2PatrolData_pcFront')
        move_user(mapId=52000111, portalId=10)
        set_effect(triggerIds=[5300], visible=False)
        set_effect(triggerIds=[5301], visible=False)
        set_effect(triggerIds=[5302], visible=False)
        set_effect(triggerIds=[5303], visible=False)
        set_effect(triggerIds=[5304], visible=False)
        set_effect(triggerIds=[5305], visible=False)
        set_effect(triggerIds=[5306], visible=False)
        set_effect(triggerIds=[5307], visible=False)
        set_effect(triggerIds=[5308], visible=False)
        set_effect(triggerIds=[5309], visible=False)
        set_effect(triggerIds=[5310], visible=False)
        set_effect(triggerIds=[5311], visible=False)
        set_effect(triggerIds=[5312], visible=False)
        set_effect(triggerIds=[5313], visible=False)
        set_effect(triggerIds=[5314], visible=False)
        set_effect(triggerIds=[5315], visible=False)
        set_effect(triggerIds=[8000], visible=True)
        set_effect(triggerIds=[8001], visible=True)
        set_effect(triggerIds=[8002], visible=True)
        set_effect(triggerIds=[8003], visible=True)
        set_effect(triggerIds=[8004], visible=True)
        set_effect(triggerIds=[8005], visible=True)
        set_effect(triggerIds=[8006], visible=True)
        set_effect(triggerIds=[8007], visible=True)
        set_effect(triggerIds=[8008], visible=True)
        set_effect(triggerIds=[8009], visible=True)
        spawn_npc_range(rangeIds=[202,203,204,205,206,207,208,209,210,211], isAutoTargeting=False)
        destroy_monster(spawnIds=[200])
        create_monster(spawnIds=[200], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 쉐도우클로등장씬12()


class 쉐도우클로등장씬12(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_effect(triggerIds=[8010], visible=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)
        set_effect(triggerIds=[5300], visible=False)
        set_effect(triggerIds=[5301], visible=False)
        set_effect(triggerIds=[5302], visible=False)
        set_effect(triggerIds=[5303], visible=False)
        set_effect(triggerIds=[5304], visible=False)
        set_effect(triggerIds=[5305], visible=False)
        set_effect(triggerIds=[5306], visible=False)
        set_effect(triggerIds=[5307], visible=False)
        set_effect(triggerIds=[5308], visible=False)
        set_effect(triggerIds=[5309], visible=False)
        set_effect(triggerIds=[5310], visible=False)
        set_effect(triggerIds=[5312], visible=False)
        set_effect(triggerIds=[5313], visible=False)
        set_effect(triggerIds=[5314], visible=False)
        destroy_monster(spawnIds=[200])
        create_monster(spawnIds=[201], arg2=False)
        show_guide_summary(entityId=25201112, textId=25201112, duration=10000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002306], questStates=[1]):
            return 쉐도우클로와떠남01()


#  ########################씬3 쉐도우클로와pc, 재즈바로########################
class 쉐도우클로와떠남01(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        show_guide_summary(entityId=25201113, textId=25201113, duration=5000)


#  ########################씬4 PC, 대탈출########################
class PC대탈출01(state.State):
    def on_enter(self):
        set_sound(triggerId=9001, arg2=True)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[300,301,302], arg2=False)
        move_user(mapId=52000111, portalId=11)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return PC대탈출02()


class PC대탈출02(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_3, arg2='nextState')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[1008,1009], returnView=False)
        set_pc_emotion_loop(sequenceName='Push_A', duration=8000)
        face_emotion(spawnId=0, emotionName='PC_Pain_86000')
        set_npc_emotion_loop(spawnId=300, sequenceName='Sit_Down_A', duration=17500)
        set_npc_emotion_loop(spawnId=301, sequenceName='Sit_Down_A', duration=17500)
        set_npc_emotion_loop(spawnId=302, sequenceName='Sit_Down_A', duration=17500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7800):
            return PC대탈출03()


class PC대탈출03(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_PC_GO')
        select_camera_path(pathIds=[1010,1011], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return PC대탈출03_1()


class PC대탈출03_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC대탈출04()


class Skip_3(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        move_user_path(patrolName='MS2PatrolData_PC_GO')
        set_pc_emotion_loop(sequenceName='Idle_A', duration=500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC대탈출04()


class PC대탈출04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        add_balloon_talk(spawnId=0, msg='$52000111_QD__52000111__7$', duration=6000, delayTick=1000)
        show_guide_summary(entityId=25201114, textId=25201114, duration=10000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[10011], questIds=[20002314], questStates=[3]):
            return 어쌔신탈출01()


#  ########################어쌔신 탈출########################
class 어쌔신탈출01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 어쌔신탈출02()


class 어쌔신탈출02(state.State):
    def on_enter(self):
        move_user(mapId=52000113, portalId=0)


