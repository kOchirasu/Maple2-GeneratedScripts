""" trigger/52000183_qd/52000183.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 영상재생(self.ctx)


class 영상재생(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[500], animationEffect=False)
        self.create_monster(spawnIds=[501], animationEffect=False)
        self.create_monster(spawnIds=[502], animationEffect=False)
        self.create_monster(spawnIds=[503], animationEffect=False)
        self.create_monster(spawnIds=[504], animationEffect=False)
        self.create_monster(spawnIds=[505], animationEffect=False)
        self.create_monster(spawnIds=[506], animationEffect=False)
        self.create_monster(spawnIds=[507], animationEffect=False)
        self.create_monster(spawnIds=[508], animationEffect=False)
        self.create_monster(spawnIds=[509], animationEffect=False)
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='jobChange_priest.swf', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 전경씬01(self.ctx)
        if self.wait_tick(waitTick=8000):
            return 전경씬01(self.ctx)


class 전경씬01(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000183, portalId=80)
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')
        self.select_camera_path(pathIds=[4000,4001,4002], returnView=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전경씬02_b(self.ctx)


class 전경씬02_b(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Priest_HeavensPray3_A'])
        self.set_npc_emotion_loop(spawnId=500, sequenceName='Bore_A', duration=8000)
        self.set_npc_emotion_loop(spawnId=501, sequenceName='Idle_A', duration=8000)
        self.set_npc_emotion_loop(spawnId=502, sequenceName='Idle_A', duration=8000)
        self.set_npc_emotion_loop(spawnId=503, sequenceName='Bore_A', duration=8000)
        self.set_npc_emotion_loop(spawnId=504, sequenceName='Idle_A', duration=8000)
        self.set_npc_emotion_loop(spawnId=505, sequenceName='Bore_A', duration=8000)
        self.set_npc_emotion_loop(spawnId=506, sequenceName='Idle_A', duration=8000)
        self.set_npc_emotion_loop(spawnId=507, sequenceName='Bore_A', duration=8000)

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
        self.move_npc(spawnId=502, patrolName='MS2PatrolData_502')
        self.move_npc(spawnId=503, patrolName='MS2PatrolData_503')
        self.move_npc(spawnId=505, patrolName='MS2PatrolData_505')
        self.move_npc(spawnId=506, patrolName='MS2PatrolData_506')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.show_guide_summary(entityId=52001831, textId=52001831, duration=10000)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002341], questStates=[3]):
            return 전직이펙트_01(self.ctx)


class 전직이펙트_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전직이펙트_02(self.ctx)


class 전직이펙트_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002342], questStates=[3]):
            return 가브란트퇴장01(self.ctx)


# ########################전원 퇴장########################
class 가브란트퇴장01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=509, patrolName='MS2PatrolData_gabExit')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9002, spawnIds=[509]):
            return NPC소멸(self.ctx)


class NPC소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[509])

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002343], questStates=[3]):
            return 전원퇴장01(self.ctx)


class 전원퇴장01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=10, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전원퇴장01_b(self.ctx)


class 전원퇴장01_b(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000183, portalId=81)
        self.destroy_monster(spawnIds=[500])
        self.destroy_monster(spawnIds=[501])
        self.destroy_monster(spawnIds=[502])
        self.destroy_monster(spawnIds=[502])
        self.destroy_monster(spawnIds=[503])
        self.destroy_monster(spawnIds=[504])
        self.destroy_monster(spawnIds=[505])
        self.destroy_monster(spawnIds=[506])
        self.destroy_monster(spawnIds=[507])
        self.destroy_monster(spawnIds=[508])
        self.destroy_monster(spawnIds=[509])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전원퇴장02(self.ctx)


class 전원퇴장02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=10, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.show_guide_summary(entityId=52001832, textId=52001832, duration=10000)
        self.create_monster(spawnIds=[510], animationEffect=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002345], questStates=[3]):
            return 프론티아재단으로01(self.ctx)


# ########################퀘스트 종료########################
class 프론티아재단으로01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 프론티아재단으로02(self.ctx)


class 프론티아재단으로02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000186, portalId=1)


initial_state = Wait
