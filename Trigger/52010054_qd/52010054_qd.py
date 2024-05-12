""" trigger/52010054_qd/52010054_qd.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(isVisible=False) # 유저 투명 처리
        self.create_monster(spawnIds=[2000], animationEffect=False) # 인페르녹
        self.create_monster(spawnIds=[2001], animationEffect=False) # 크림슨 발록
        self.create_monster(spawnIds=[2002], animationEffect=False) # 크림슨 발록
        self.create_monster(spawnIds=[2003], animationEffect=False) # 크림슨 발록

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return CameraEffect01(self.ctx)


class CameraEffect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect02(self.ctx)


class CameraEffect02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=quit02, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[4000,4001], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=14000):
            return CameraEffect03(self.ctx)


class CameraEffect03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return CameraEffect04(self.ctx)


class CameraEffect04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.add_cinematic_talk(npcId=11003793, msg='$52010054_QD__52010054_QD__0$', duration=7000, align='right')
        self.select_camera_path(pathIds=[4002,4003], returnView=False)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return CameraEffect05(self.ctx)


class CameraEffect05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003793, msg='$52010054_QD__52010054_QD__1$', duration=5000, align='right')
        self.select_camera_path(pathIds=[4004,4005], returnView=False)
        self.set_npc_emotion_sequence(spawnId=2001, sequenceName='Attack_01_C,Attack_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return CameraEffect06(self.ctx)


class CameraEffect06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003793, msg='$52010054_QD__52010054_QD__2$', duration=4000, align='right')
        self.select_camera_path(pathIds=[4006,4007], returnView=False)
        self.set_npc_emotion_sequence(spawnId=2002, sequenceName='Attack_01_B,Attack_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return CameraEffect07(self.ctx)


class CameraEffect07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003793, msg='$52010054_QD__52010054_QD__3$', duration=4000, align='right')
        self.select_camera_path(pathIds=[4008,4009,4013,4014], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return CameraEffect08(self.ctx)


class CameraEffect08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return CameraEffect09(self.ctx)


class CameraEffect09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[2001], arg2=False) # 크림슨 발록
        self.destroy_monster(spawnIds=[2002], arg2=False) # 크림슨 발록
        self.destroy_monster(spawnIds=[2003], arg2=False) # 크림슨 발록

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=0):
            return CameraEffect10(self.ctx)


class CameraEffect10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.select_camera_path(pathIds=[4010,4011], returnView=False)
        self.set_time_scale(enable=True, startScale=1, endScale=0.1, duration=12, interpolator=1) # 10초간 느려지기 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=12000):
            return CameraEffect11(self.ctx)


class CameraEffect11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return CameraEffect12(self.ctx)


class CameraEffect12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=200):
            return CameraEffect13(self.ctx)


class CameraEffect13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=2000, sequenceName='Attack_01_B,Attack_01_B')
        self.set_time_scale(enable=True, startScale=0.5, endScale=0.1, duration=12, interpolator=1) # 10초간 느려지기 시작
        self.select_camera_path(pathIds=[4012,4015], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return quit01(self.ctx)


class quit01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return quit02(self.ctx)


class quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.move_user(mapId=2000422, portalId=5)


initial_state = start
