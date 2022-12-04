""" trigger/63000042_cs/wakeup02.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=7001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[60100005,60100006,60100007,60100008,60100009,60100010], questStates=[2]):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[102])
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.move_user(mapId=63000042, portalId=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return talk_01(self.ctx)


class talk_01(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$63000042_CS__WAKEUP02__0$', duration=3000)
        self.set_scene_skip(state=sitready, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return talk_02(self.ctx)


class talk_02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$63000042_CS__WAKEUP02__1$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return talk_03(self.ctx)


class talk_03(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$63000042_CS__WAKEUP02__2$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return talk_04(self.ctx)


class talk_04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003145, msg='$63000042_CS__WAKEUP02__3$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return talk_05(self.ctx)


class talk_05(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$63000042_CS__WAKEUP02__4$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return talk_06(self.ctx)


class talk_06(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$63000042_CS__WAKEUP02__5$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return talk_07(self.ctx)


class talk_07(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$63000042_CS__WAKEUP02__6$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return talk_08(self.ctx)


class talk_08(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003145, msg='$63000042_CS__WAKEUP02__7$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return talk_09(self.ctx)


class talk_09(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='$63000042_CS__WAKEUP02__8$', duration=3000)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return sitready(self.ctx)


class sitready(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=13000)
        self.set_sound(triggerId=7002, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return fadein(self.ctx)


class fadein(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.create_monster(spawnIds=[103], animationEffect=False) # 프레이 스폰

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return praymove_01(self.ctx)


class praymove_01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_103')
        self.add_cinematic_talk(npcId=11003165, illustId='Fray_normal', msg='$63000042_CS__WAKEUP02__9$', duration=3000, align='Left')
        self.set_scene_skip(state=end, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return praytalk_02(self.ctx)


class praytalk_02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003165, msg='$63000042_CS__WAKEUP02__10$', duration=3000)
        self.select_camera_path(pathIds=[502], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return pray(self.ctx)


class pray(trigger_api.Trigger):
    def on_enter(self):
        self.show_caption(scale=2.5, type='NameCaption', title='$63000042_CS__WAKEUP02__11$', desc='$63000042_CS__WAKEUP02__12$', align='centerRight', offsetRateX=0.5, duration=4000)
        self.select_camera_path(pathIds=[502,503], returnView=False)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=100)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[60100010], questStates=[1]):
            return warp(self.ctx)


class warp(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000033, portalId=1)


initial_state = idle
