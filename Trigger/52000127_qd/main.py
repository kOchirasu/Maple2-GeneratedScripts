""" trigger/52000127_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.visible_my_pc(isVisible=False)
        self.set_sound(triggerId=7001, enable=False)
        self.set_sound(triggerId=7002, enable=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60100215,60100216,60100217,60100218,60100219,60100220], questStates=[2]):
            return ready(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60100220,60100221,60100222,60100223,60100224,60100225,60100226,60100227,60100228,60100229,60100230], questStates=[2]):
            return open(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.create_monster(spawnIds=[101], animationEffect=True) # 조디

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return setting(self.ctx)


class setting(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.visible_my_pc(isVisible=True)
        self.select_camera_path(pathIds=[4002], returnView=False)
        self.move_user(mapId=52000127, portalId=6001)
        self.set_sound(triggerId=7001, enable=True)
        self.set_scene_skip(state=end, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return dreamscene_01(self.ctx)


# PC 꿈
class dreamscene_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000127_QD__MAIN__0$', arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return dreamscene_02(self.ctx)


class dreamscene_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000127_QD__MAIN__1$', arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return dreamscene_03(self.ctx)


class dreamscene_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000127_QD__MAIN__2$', arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return dreamscene_04(self.ctx)


class dreamscene_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000127_QD__MAIN__3$', arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return dreamscene_05(self.ctx)


class dreamscene_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000127_QD__MAIN__4$', arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return dreamscene_06(self.ctx)


class dreamscene_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000127_QD__MAIN__5$', arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return dreamscene_07(self.ctx)


class dreamscene_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='$52000127_QD__MAIN__6$', arg3=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_01(self.ctx)


# 연출
class scene_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_sound(triggerId=7001, enable=False)
        self.set_sound(triggerId=7002, enable=True)
        self.set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=21000)
        self.face_emotion(spawnId=0, emotionName='Stun')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=0, emotionName='Stun')
        self.show_caption(type='VerticalCaption', title='$52000127_QD__MAIN__12$', desc='$52000127_QD__MAIN__13$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=0, emotionName='Stun')
        self.add_cinematic_talk(npcId=11003218, msg='$52000127_QD__MAIN__7$', duration=3000, illustId='Jordy_normal', align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.face_emotion(spawnId=0, emotionName='Stun')
        self.add_cinematic_talk(npcId=11003218, msg='$52000127_QD__MAIN__8$', duration=3000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.add_cinematic_talk(npcId=11003218, msg='$52000127_QD__MAIN__9$', duration=3000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.face_emotion(spawnId=0, emotionName='calm')
        self.add_cinematic_talk(npcId=0, msg='$52000127_QD__MAIN__10$', duration=3000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.face_emotion(spawnId=0, emotionName='Ride_Sp_Run_005')
        self.add_cinematic_talk(npcId=11003218, msg='$52000127_QD__MAIN__11$', duration=3000, align='Right')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)


class open(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.visible_my_pc(isVisible=True)
        self.create_monster(spawnIds=[101], animationEffect=True) # 조디

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return open2(self.ctx)


class open2(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
