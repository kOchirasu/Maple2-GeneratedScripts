""" trigger/52000111_qd/52000111.xml """
import common


class 입장(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[10011]):
            return START(self.ctx)


class START(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8000], visible=False)
        self.set_effect(triggerIds=[8001], visible=False)
        self.set_effect(triggerIds=[8002], visible=False)
        self.set_effect(triggerIds=[8003], visible=False)
        self.set_effect(triggerIds=[8004], visible=False)
        self.set_effect(triggerIds=[8005], visible=False)
        self.set_effect(triggerIds=[8006], visible=False)
        self.set_effect(triggerIds=[8007], visible=False)
        self.set_effect(triggerIds=[8008], visible=False)
        self.set_effect(triggerIds=[8009], visible=False)
        self.set_effect(triggerIds=[8010], visible=False)
        self.set_effect(triggerIds=[8011], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002315], questStates=[2]):
            return 어쌔신탈출02(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002313], questStates=[2]):
            return PC대탈출01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002313], questStates=[3]):
            return PC대탈출01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002314], questStates=[2]):
            return PC대탈출01(self.ctx)
        if not self.quest_user_detected(boxIds=[10011], questIds=[20002313], questStates=[2]):
            return Wait(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002312], questStates=[3]):
            return PC대탈출01(self.ctx)


class Wait(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[5300], visible=False)
        self.set_effect(triggerIds=[5301], visible=False)
        self.set_effect(triggerIds=[5302], visible=False)
        self.set_effect(triggerIds=[5303], visible=False)
        self.set_effect(triggerIds=[5304], visible=False)
        self.set_effect(triggerIds=[5305], visible=False)
        self.set_effect(triggerIds=[5306], visible=False)
        self.set_effect(triggerIds=[5307], visible=False)
        self.set_effect(triggerIds=[5308], visible=False)
        self.set_effect(triggerIds=[5309], visible=False)
        self.set_effect(triggerIds=[5310], visible=False)
        self.set_effect(triggerIds=[5311], visible=False)
        self.set_effect(triggerIds=[5312], visible=False)
        self.set_effect(triggerIds=[5313], visible=False)
        self.set_effect(triggerIds=[5314], visible=False)
        self.set_effect(triggerIds=[5315], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[10011]):
            return 영상준비_01(self.ctx)


class 영상준비_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52000111, portalId=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 영상재생(self.ctx)


class 영상재생(common.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='common\JobIntro_Assassin.usm', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 커닝시티전경씬01(self.ctx)
        if self.wait_tick(waitTick=55000):
            return 커닝시티전경씬01(self.ctx)


class 커닝시티전경씬01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.select_camera_path(pathIds=[1000,1001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 커닝시티전경씬01_B(self.ctx)


class 커닝시티전경씬01_B(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[1002,1003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 커닝시티전경씬02(self.ctx)


class 커닝시티전경씬02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[1004,1005], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 커닝시티전경씬03(self.ctx)


class 커닝시티전경씬03(common.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$52000111_QD__52000111__0$', desc='$52000111_QD__52000111__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=7000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 커닝시티전경씬04(self.ctx)


class 커닝시티전경씬04(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit01(self.ctx)


class Quit01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit01_1(self.ctx)


class Quit01_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


class Quit02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.set_effect(triggerIds=[5300], visible=True)
        self.set_effect(triggerIds=[5301], visible=True)
        self.set_effect(triggerIds=[5302], visible=True)
        self.set_effect(triggerIds=[5303], visible=True)
        self.set_effect(triggerIds=[5304], visible=True)
        self.set_effect(triggerIds=[5305], visible=True)
        self.set_effect(triggerIds=[5306], visible=True)
        self.set_effect(triggerIds=[5307], visible=True)
        self.set_effect(triggerIds=[5308], visible=True)
        self.set_effect(triggerIds=[5309], visible=True)
        self.set_effect(triggerIds=[5310], visible=True)
        self.set_effect(triggerIds=[5311], visible=True)
        self.set_effect(triggerIds=[5312], visible=True)
        self.set_effect(triggerIds=[5313], visible=True)
        self.set_effect(triggerIds=[5314], visible=True)
        self.set_effect(triggerIds=[5315], visible=True)
        self.add_balloon_talk(spawnId=0, msg='$52000111_QD__52000111__2$', duration=6000, delayTick=1000)
        self.show_guide_summary(entityId=25201111, textId=25201111, duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[10012]):
            return 쉐도우클로등장씬01(self.ctx)


# ########################씬2 쉐도우클로 등장########################
class 쉐도우클로등장씬01(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=9000, enable=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 쉐도우클로등장씬02(self.ctx)


class 쉐도우클로등장씬02(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawnId=2000, patrolName='MS2PatrolData_pcFront')
        self.add_balloon_talk(spawnId=0, msg='$52000111_QD__52000111__3$', duration=6000, delayTick=1000)
        self.set_pc_emotion_loop(sequenceName='Assassin_Bore_A', duration=25000)
        self.select_camera_path(pathIds=[1006,1007], returnView=False)
        self.move_user(mapId=52000111, portalId=10)
        self.set_effect(triggerIds=[5300], visible=False)
        self.set_effect(triggerIds=[5301], visible=False)
        self.set_effect(triggerIds=[5302], visible=False)
        self.set_effect(triggerIds=[5303], visible=False)
        self.set_effect(triggerIds=[5304], visible=False)
        self.set_effect(triggerIds=[5305], visible=False)
        self.set_effect(triggerIds=[5306], visible=False)
        self.set_effect(triggerIds=[5307], visible=False)
        self.set_effect(triggerIds=[5308], visible=False)
        self.set_effect(triggerIds=[5309], visible=False)
        self.set_effect(triggerIds=[5310], visible=False)
        self.set_effect(triggerIds=[5311], visible=False)
        self.set_effect(triggerIds=[5312], visible=False)
        self.set_effect(triggerIds=[5313], visible=False)
        self.set_effect(triggerIds=[5314], visible=False)
        self.set_effect(triggerIds=[5315], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 쉐도우클로등장씬04(self.ctx)


class 쉐도우클로등장씬04(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Assassin_Bore_A'])
        self.add_balloon_talk(spawnId=0, msg='$52000111_QD__52000111__4$', duration=6000, delayTick=1000)
        self.select_camera_path(pathIds=[1012,1013], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 쉐도우클로등장씬05(self.ctx)


class 쉐도우클로등장씬05(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8000], visible=True)
        self.set_effect(triggerIds=[8001], visible=True)
        self.set_effect(triggerIds=[8002], visible=True)
        self.set_effect(triggerIds=[8003], visible=True)
        self.set_effect(triggerIds=[8004], visible=True)
        self.set_effect(triggerIds=[8005], visible=True)
        self.set_effect(triggerIds=[8006], visible=True)
        self.set_effect(triggerIds=[8007], visible=True)
        self.set_effect(triggerIds=[8008], visible=True)
        self.set_effect(triggerIds=[8009], visible=True)
        self.select_camera_path(pathIds=[1014,1015], returnView=False)
        self.spawn_npc_range(rangeIds=[202,203,204,205,206,207,208,209,210,211], isAutoTargeting=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 쉐도우클로등장씬06(self.ctx)


class 쉐도우클로등장씬06(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8010], visible=True)
        self.create_monster(spawnIds=[200], animationEffect=False)
        self.select_camera_path(pathIds=[1016,1017], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 쉐도우클로등장씬07(self.ctx)


class 쉐도우클로등장씬07(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=200, sequenceName='Sit_Down_A', duration=4000)
        self.select_camera_path(pathIds=[1018,1019], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 쉐도우클로등장씬09(self.ctx)


class 쉐도우클로등장씬09(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=200, sequenceName='Bore_A')
        self.select_camera_path(pathIds=[1020,1021], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 쉐도우클로등장씬11(self.ctx)


class 쉐도우클로등장씬11(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[1022,1023], returnView=False)
        self.show_caption(type='NameCaption', title='$52000111_QD__52000111__5$', desc='$52000111_QD__52000111__6$', align='center', offsetRateX=-0.15, offsetRateY=0.15, duration=10000, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 쉐도우클로등장씬11_1(self.ctx)


class 쉐도우클로등장씬11_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 쉐도우클로등장씬12(self.ctx)


class Skip_2(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_npc(spawnId=2000, patrolName='MS2PatrolData_pcFront')
        self.move_user(mapId=52000111, portalId=10)
        self.set_effect(triggerIds=[5300], visible=False)
        self.set_effect(triggerIds=[5301], visible=False)
        self.set_effect(triggerIds=[5302], visible=False)
        self.set_effect(triggerIds=[5303], visible=False)
        self.set_effect(triggerIds=[5304], visible=False)
        self.set_effect(triggerIds=[5305], visible=False)
        self.set_effect(triggerIds=[5306], visible=False)
        self.set_effect(triggerIds=[5307], visible=False)
        self.set_effect(triggerIds=[5308], visible=False)
        self.set_effect(triggerIds=[5309], visible=False)
        self.set_effect(triggerIds=[5310], visible=False)
        self.set_effect(triggerIds=[5311], visible=False)
        self.set_effect(triggerIds=[5312], visible=False)
        self.set_effect(triggerIds=[5313], visible=False)
        self.set_effect(triggerIds=[5314], visible=False)
        self.set_effect(triggerIds=[5315], visible=False)
        self.set_effect(triggerIds=[8000], visible=True)
        self.set_effect(triggerIds=[8001], visible=True)
        self.set_effect(triggerIds=[8002], visible=True)
        self.set_effect(triggerIds=[8003], visible=True)
        self.set_effect(triggerIds=[8004], visible=True)
        self.set_effect(triggerIds=[8005], visible=True)
        self.set_effect(triggerIds=[8006], visible=True)
        self.set_effect(triggerIds=[8007], visible=True)
        self.set_effect(triggerIds=[8008], visible=True)
        self.set_effect(triggerIds=[8009], visible=True)
        self.spawn_npc_range(rangeIds=[202,203,204,205,206,207,208,209,210,211], isAutoTargeting=False)
        self.destroy_monster(spawnIds=[200])
        self.create_monster(spawnIds=[200], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 쉐도우클로등장씬12(self.ctx)


class 쉐도우클로등장씬12(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_effect(triggerIds=[8010], visible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)
        self.set_effect(triggerIds=[5300], visible=False)
        self.set_effect(triggerIds=[5301], visible=False)
        self.set_effect(triggerIds=[5302], visible=False)
        self.set_effect(triggerIds=[5303], visible=False)
        self.set_effect(triggerIds=[5304], visible=False)
        self.set_effect(triggerIds=[5305], visible=False)
        self.set_effect(triggerIds=[5306], visible=False)
        self.set_effect(triggerIds=[5307], visible=False)
        self.set_effect(triggerIds=[5308], visible=False)
        self.set_effect(triggerIds=[5309], visible=False)
        self.set_effect(triggerIds=[5310], visible=False)
        self.set_effect(triggerIds=[5312], visible=False)
        self.set_effect(triggerIds=[5313], visible=False)
        self.set_effect(triggerIds=[5314], visible=False)
        self.destroy_monster(spawnIds=[200])
        self.create_monster(spawnIds=[201], animationEffect=False)
        self.show_guide_summary(entityId=25201112, textId=25201112, duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002306], questStates=[1]):
            return 쉐도우클로와떠남01(self.ctx)


# ########################씬3 쉐도우클로와pc, 재즈바로########################
class 쉐도우클로와떠남01(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.show_guide_summary(entityId=25201113, textId=25201113, duration=5000)


# ########################씬4 PC, 대탈출########################
class PC대탈출01(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=9001, enable=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.create_monster(spawnIds=[300,301,302], animationEffect=False)
        self.move_user(mapId=52000111, portalId=11)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return PC대탈출02(self.ctx)


class PC대탈출02(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_3, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[1008,1009], returnView=False)
        self.set_pc_emotion_loop(sequenceName='Push_A', duration=8000)
        self.face_emotion(spawnId=0, emotionName='PC_Pain_86000')
        self.set_npc_emotion_loop(spawnId=300, sequenceName='Sit_Down_A', duration=17500)
        self.set_npc_emotion_loop(spawnId=301, sequenceName='Sit_Down_A', duration=17500)
        self.set_npc_emotion_loop(spawnId=302, sequenceName='Sit_Down_A', duration=17500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7800):
            return PC대탈출03(self.ctx)


class PC대탈출03(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_PC_GO')
        self.select_camera_path(pathIds=[1010,1011], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return PC대탈출03_1(self.ctx)


class PC대탈출03_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC대탈출04(self.ctx)


class Skip_3(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_user_path(patrolName='MS2PatrolData_PC_GO')
        self.set_pc_emotion_loop(sequenceName='Idle_A', duration=500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC대탈출04(self.ctx)


class PC대탈출04(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.add_balloon_talk(spawnId=0, msg='$52000111_QD__52000111__7$', duration=6000, delayTick=1000)
        self.show_guide_summary(entityId=25201114, textId=25201114, duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002314], questStates=[3]):
            return 어쌔신탈출01(self.ctx)


# ########################어쌔신 탈출########################
class 어쌔신탈출01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 어쌔신탈출02(self.ctx)


class 어쌔신탈출02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000113, portalId=0)


initial_state = 입장
