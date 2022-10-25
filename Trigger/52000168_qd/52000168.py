""" trigger/52000168_qd/52000168.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 영상재생(self.ctx)


class 영상재생(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[401], animationEffect=False) # 바사라첸
        self.create_monster(spawnIds=[402], animationEffect=False) # 바사라첸
        self.create_monster(spawnIds=[403], animationEffect=False) # 바사라첸
        self.create_monster(spawnIds=[404], animationEffect=False) # 바사라첸
        self.create_monster(spawnIds=[405], animationEffect=False) # 바사라첸
        self.create_monster(spawnIds=[406], animationEffect=False) # 바사라첸
        self.move_user(mapId=52000168, portalId=80)
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='jobChange_RBlader.swf', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 전경씬01(self.ctx)
        if self.wait_tick(waitTick=8000):
            return 전경씬01(self.ctx)


class 전경씬01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_pc_emotion_loop(sequenceName='Push_A', duration=10000, arg3=True)
        self.set_npc_emotion_loop(spawnId=402, sequenceName='Attack_Idle_A', duration=1000000)
        self.set_npc_emotion_loop(spawnId=403, sequenceName='Dead_A', duration=800000)
        self.set_npc_emotion_loop(spawnId=404, sequenceName='Dead_A', duration=800000)
        self.set_npc_emotion_loop(spawnId=405, sequenceName='Dead_A', duration=800000)
        self.set_npc_emotion_loop(spawnId=406, sequenceName='Dead_A', duration=800000)
        self.select_camera_path(pathIds=[4000,4001,4003], returnView=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 전경씬02(self.ctx)


class 전경씬02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit01(self.ctx)


class Quit01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
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
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.show_guide_summary(entityId=52001681, textId=52001681, duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002373], questStates=[3]):
            return 전직이펙트_01(self.ctx)


class 전직이펙트_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전직이펙트_02(self.ctx)


class 전직이펙트_02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[402])
        self.destroy_monster(spawnIds=[403])
        self.destroy_monster(spawnIds=[404])
        self.destroy_monster(spawnIds=[405])
        self.destroy_monster(spawnIds=[406])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전직이펙트_03(self.ctx)


class 전직이펙트_03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit03(self.ctx)


# ########################퀘스트 종료########################
class Quit03(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[402])
        self.destroy_monster(spawnIds=[403])
        self.destroy_monster(spawnIds=[404])
        self.destroy_monster(spawnIds=[405])
        self.destroy_monster(spawnIds=[406])
        self.create_monster(spawnIds=[500], animationEffect=False)
        self.create_monster(spawnIds=[501], animationEffect=False)
        self.create_monster(spawnIds=[502], animationEffect=False)
        self.move_npc(spawnId=500, patrolName='MS2PatrolData_500')
        self.move_npc(spawnId=501, patrolName='MS2PatrolData_501')
        self.move_npc(spawnId=502, patrolName='MS2PatrolData_502')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002374], questStates=[3]):
            return 칼리브요새로01(self.ctx)


class 칼리브요새로01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 칼리브요새로02(self.ctx)


class 칼리브요새로02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000169, portalId=1)


initial_state = Wait
