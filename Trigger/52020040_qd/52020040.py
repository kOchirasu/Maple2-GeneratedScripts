""" trigger/52020040_qd/52020040.xml """
import trigger_api


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2001]):
            return wait_02(self.ctx)


class wait_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_effect(triggerIds=[6000], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return wait_03(self.ctx)


class wait_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.move_user(mapId=52020040, portalId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 크리티아스로(self.ctx)


class 크리티아스로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[4001,4002], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 크리티아스로_02(self.ctx)


class 크리티아스로_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4003,4004,4005], returnView=False)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Talk_B', duration=1E+11)
        self.add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='left', msg='$52020040_QD__52020040__0$', duration=3000)
        self.add_cinematic_talk(npcId=11004437, illustId='Neirin_smile', align='right', msg='$52020040_QD__52020040__1$', duration=3000)
        self.add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='left', msg='$52020040_QD__52020040__2$', duration=3000)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return 크리티아스로_02_01(self.ctx)


class 크리티아스로_02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4006], returnView=False)
        self.show_caption(type='HorizonCaption', title='$52020040_QD__52020040__3$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 크리티아스로_03(self.ctx)


class 크리티아스로_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4007], returnView=False)
        self.add_cinematic_talk(npcId=11004436, illustId='Schatten_smile', align='left', msg='$52020040_QD__52020040__4$', duration=3000)
        self.add_cinematic_talk(npcId=11004438, illustId='Mason_closeEye', align='right', msg='$52020040_QD__52020040__5$', duration=3000)
        self.add_cinematic_talk(npcId=11004435, illustId='Conder_smile', align='left', msg='$52020040_QD__52020040__6$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return 크리티아스로_04(self.ctx)


class 크리티아스로_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=[232,92,53])
        self.set_directional_light(diffuseColor=[41,21,18], specularColor=[130,130,130])
        self.add_cinematic_talk(npcId=11004435, illustId='Conder_normal', align='left', msg='$52020040_QD__52020040__7$', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 경보(self.ctx)


class 경보(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6000], visible=True)
        self.set_actor(triggerId=201, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=202, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=203, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 경보_01(self.ctx)


class 경보_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__8$', duration=2500)
        self.add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__9$', duration=2800)
        self.add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='right', msg='$52020040_QD__52020040__10$', duration=2800)
        self.add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__11$', duration=2800)
        self.add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='right', msg='$52020040_QD__52020040__12$', duration=2400)
        self.add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__13$', duration=2800)
        self.add_cinematic_talk(npcId=11004434, illustId='Bliche_mad', align='right', msg='$52020040_QD__52020040__14$', duration=2800)
        self.add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__15$', duration=2400)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=21300):
            return 경보_02(self.ctx)


class 경보_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4009,4010], returnView=False)
        self.set_effect(triggerIds=[6000], visible=False)
        self.add_cinematic_talk(npcId=11004440, msg='$52020040_QD__52020040__16$', duration=3000)
        self.add_cinematic_talk(npcId=11004440, msg='$52020040_QD__52020040__17$', duration=5000)
        self.add_cinematic_talk(npcId=11004440, msg='$52020040_QD__52020040__18$', duration=2600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10200):
            return 경보끝_01(self.ctx)


class 경보끝_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_ambient_light(primary=[131,160,209])
        self.set_directional_light(diffuseColor=[134,160,143], specularColor=[130,130,130])
        self.set_actor(triggerId=201, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=202, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=203, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.add_cinematic_talk(npcId=11004435, illustId='Conder_normal', align='right', msg='$52020040_QD__52020040__19$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 경보끝_02_01(self.ctx)


class 경보끝_02_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 경보끝_02_02(self.ctx)


class 경보끝_02_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 경보끝_02(self.ctx)


class 경보끝_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4012], returnView=False)
        self.add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__20$', duration=2800)
        self.add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__21$', duration=2800)
        self.add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__22$', duration=3000)
        self.add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='right', msg='$52020040_QD__52020040__23$', duration=3000)
        self.add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='right', msg='$52020040_QD__52020040__24$', duration=3000)
        self.add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__25$', duration=3000)
        self.add_cinematic_talk(npcId=11004435, illustId='Conder_normal', align='right', msg='$52020040_QD__52020040__26$', duration=3000)
        self.add_cinematic_talk(npcId=11004436, illustId='Schatten_surprise', align='left', msg='$52020040_QD__52020040__27$', duration=3000)
        self.add_cinematic_talk(npcId=11004435, illustId='Conder_normal', align='right', msg='$52020040_QD__52020040__28$', duration=2500)
        self.add_cinematic_talk(npcId=11004438, illustId='Mason_normal', align='left', msg='$52020040_QD__52020040__29$', duration=3000)
        self.add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='right', msg='$52020040_QD__52020040__30$', duration=2500)
        self.add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='right', msg='$52020040_QD__52020040__31$', duration=3000)
        self.add_cinematic_talk(npcId=11004438, illustId='Mason_normal', align='left', msg='$52020040_QD__52020040__32$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52020040_QD__52020040__33$', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=37800):
            return 경보끝_03(self.ctx)


class 경보끝_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4011,4013], returnView=False)
        # self.set_pc_emotion_loop(sequenceName='Talk_A', duration=1E+13)
        self.add_cinematic_talk(npcId=11004438, illustId='Mason_normal', msg='$52020040_QD__52020040__34$', align='left', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52020040_QD__52020040__35$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52020040_QD__52020040__36$', duration=3000)
        self.add_cinematic_talk(npcId=11004436, illustId='Schatten_surprise', align='left', msg='$52020040_QD__52020040__37$', duration=3500)
        self.add_cinematic_talk(npcId=11004437, illustId='Neirin_normal', align='right', msg='$52020040_QD__52020040__38$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52020040_QD__52020040__39$', duration=3000)
        self.add_cinematic_talk(npcId=11004434, illustId='Bliche_closeEye', align='left', msg='$52020040_QD__52020040__40$', duration=2800)
        self.add_cinematic_talk(npcId=11004437, illustId='Neirin_normal', align='right', msg='$52020040_QD__52020040__41$', duration=3000)
        self.add_cinematic_talk(npcId=11004434, illustId='Bliche_closeEye', align='left', msg='$52020040_QD__52020040__42$', duration=3000)
        self.add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='left', msg='$52020040_QD__52020040__43$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52020040_QD__52020040__44$', duration=3000)
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=33200):
            return 이동(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 이동_02(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 이동_02(self.ctx)


class 이동_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=2020029, portalId=2)


initial_state = wait_01
