""" trigger/52010069_qd/52010069.xml """
import trigger_api


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[50100680], questStates=[3]):
            return NPC소멸(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[50100680], questStates=[2]):
            return 아이오브라펜타로(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[50100680], questStates=[1]):
            return 전경씬_04(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[50100670], questStates=[2]):
            return 전경씬(self.ctx)


class 전경씬(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전경씬_02(self.ctx)


class 전경씬_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[4000,4001], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전경씬_03(self.ctx)


class 전경씬_03(trigger_api.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$52010069_QD__52010069__0$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 전경씬_03_01(self.ctx)


class 전경씬_03_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전경씬_03_02(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전경씬_03_02(self.ctx)


class 전경씬_03_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=20, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[50100680], questStates=[1]):
            return 전경씬_04(self.ctx)


class 전경씬_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[101], arg2=False)
        self.destroy_monster(spawnIds=[102], arg2=False)
        self.destroy_monster(spawnIds=[103], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전경씬_04_01(self.ctx)


class 전경씬_04_01(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52010069, portalId=6001)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.create_monster(spawnIds=[103], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.select_camera_path(pathIds=[4002], returnView=False)
        self.set_pc_emotion_loop(sequenceName='Object_React_H', duration=12000)
        self.add_cinematic_talk(npcId=0, msg='$52010069_QD__52010069__1$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 조사중_01(self.ctx)


class 조사중_01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003,4004], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 조사중_02(self.ctx)


class 조사중_02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52010069_QD__52010069__2$', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='$52010069_QD__52010069__3$', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='$52010069_QD__52010069__4$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=11000):
            return 조사중_03(self.ctx)


class 조사중_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 재회_01(self.ctx)


class 재회_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52010069_QD__52010069__5$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 재회_02(self.ctx)


class 재회_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4006,4007], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 재회_03(self.ctx)


class 재회_03(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$52010069_QD__52010069__6$', duration=2800)
        self.move_user(mapId=52010069, portalId=6002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 재회_04(self.ctx)


class 재회_04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData1')
        self.add_cinematic_talk(npcId=0, msg='$52010069_QD__52010069__7$', duration=3000)
        self.add_cinematic_talk(npcId=11001229, align='left', illustId='Ishura_Dark_Idle', msg='$52010069_QD__52010069__8$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52010069_QD__52010069__9$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52010069_QD__52010069__10$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=12000):
            return 재회_05(self.ctx)


class 재회_05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4009,4010], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52010069_QD__52010069__11$', duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 재회정리(self.ctx)


class 재회정리(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 재회정리_02(self.ctx)


class 재회정리_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 재회정리_03(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52010069, portalId=6002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 재회정리_03(self.ctx)


class 재회정리_03(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[50100680], questStates=[2]):
            return 아이오브라펜타로(self.ctx)


class 아이오브라펜타로(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아이오브라펜타로_01(self.ctx)


class 아이오브라펜타로_01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101], arg2=False)
        self.destroy_monster(spawnIds=[102], arg2=False)
        self.destroy_monster(spawnIds=[103], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 아이오브라펜타로_02(self.ctx)


class 아이오브라펜타로_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000496, portalId=5)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101], arg2=False)
        self.destroy_monster(spawnIds=[102], arg2=False)
        self.destroy_monster(spawnIds=[103], arg2=False)


initial_state = wait_01
