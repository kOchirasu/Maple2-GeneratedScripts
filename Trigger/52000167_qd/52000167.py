""" trigger/52000167_qd/52000167.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1000, visible=False, enable=False, minimapVisible=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 영상재생(self.ctx)


class 영상재생(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='jobChangeStory.swf', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 묘지전경씬01(self.ctx)
        if self.wait_tick(waitTick=85000):
            return 묘지전경씬01(self.ctx)


class 묘지전경씬01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_effect(triggerIds=[700], visible=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 묘지전경씬02_1(self.ctx)


class 묘지전경씬02_1(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_user_path(patrolName='MS2PatrolData_pc')
        self.select_camera_path(pathIds=[4000,4001,4002,4003], returnView=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 묘지전경씬02(self.ctx)


class 묘지전경씬02(common.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$52000167_QD__52000167__0$', desc='$52000167_QD__52000167__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 묘지전경씬03(self.ctx)


class 묘지전경씬03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return Quit02(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


class Quit02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.add_balloon_talk(spawnId=0, msg='$52000167_QD__52000167__2$', duration=6000, delayTick=1000)
        self.show_guide_summary(entityId=52001671, textId=52001671, duration=10000)
        self.create_monster(spawnIds=[400], animationEffect=False) # 조디의무덤

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002369], questStates=[3]):
            return 홀슈타트등장00(self.ctx)


# ########################씬2 케이틀린 등장########################
class 홀슈타트등장00(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.create_monster(spawnIds=[401], animationEffect=False)
        self.create_monster(spawnIds=[402], animationEffect=False)
        self.create_monster(spawnIds=[403], animationEffect=False)
        self.create_monster(spawnIds=[404], animationEffect=False)
        self.create_monster(spawnIds=[405], animationEffect=False)
        self.create_monster(spawnIds=[406], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 홀슈타트등장01(self.ctx)


class 홀슈타트등장01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=20, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[5000,5001,5002,5003,5004], returnView=False)
        self.move_npc(spawnId=402, patrolName='MS2PatrolData_402_hol')
        self.move_npc(spawnId=403, patrolName='MS2PatrolData_403')
        self.move_npc(spawnId=404, patrolName='MS2PatrolData_404')
        self.move_npc(spawnId=405, patrolName='MS2PatrolData_405')
        self.move_npc(spawnId=406, patrolName='MS2PatrolData_406')
        self.move_user_path(patrolName='MS2PatrolData_pc_move')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 홀슈타트등장02_c(self.ctx)


class 홀슈타트등장02_c(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[700], visible=True)
        self.set_time_scale(enable=True, startScale=1, endScale=0.3, duration=3.5, interpolator=2) # 2초간 느려지기 시작
        self.add_balloon_talk(spawnId=0, msg='$52000167_QD__52000167__3$', duration=6000, delayTick=1000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 홀슈타트등장02(self.ctx)


class 홀슈타트등장02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=40, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 홀슈타트등장03(self.ctx)


class 홀슈타트등장03(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=52001672, textId=52001672, duration=10000)
        self.set_onetime_effect(id=40, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002370], questStates=[3]):
            return 홀슈타트등장04(self.ctx)


class 홀슈타트등장04(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=402, sequenceName='Attack_Idle_A', duration=800000)
        self.set_npc_emotion_loop(spawnId=403, sequenceName='Attack_Idle_A', duration=800000)
        self.set_npc_emotion_loop(spawnId=404, sequenceName='Attack_Idle_A', duration=800000)
        self.set_npc_emotion_loop(spawnId=405, sequenceName='Attack_Idle_A', duration=800000)
        self.set_npc_emotion_loop(spawnId=406, sequenceName='Attack_Idle_A', duration=800000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002371], questStates=[3]):
            return 수련장이동01(self.ctx)


class 수련장이동01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=100000, arg3=True)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 수련장이동02(self.ctx)


class 수련장이동02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000168, portalId=80)


initial_state = Wait
