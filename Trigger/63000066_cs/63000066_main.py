""" trigger/63000066_cs/63000066_main.xml """
import common


class 준비(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.create_monster(spawnIds=[102], animationEffect=True)
        self.create_monster(spawnIds=[103], animationEffect=True)
        self.create_monster(spawnIds=[104], animationEffect=True)
        self.create_monster(spawnIds=[105], animationEffect=True)
        self.create_monster(spawnIds=[111], animationEffect=True)
        self.create_monster(spawnIds=[112], animationEffect=True)
        self.create_monster(spawnIds=[113], animationEffect=True)
        self.create_monster(spawnIds=[114], animationEffect=True)
        self.create_monster(spawnIds=[115], animationEffect=True)
        self.create_monster(spawnIds=[116], animationEffect=True)
        self.set_effect(triggerIds=[5001,5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[30000351], questStates=[1]):
            return 서랍장안내(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[30000351], questStates=[2]):
            return 사다리안내(self.ctx)
        if self.user_detected(boxIds=[701]):
            return 종료(self.ctx)


class 서랍장안내(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26300661, textId=26300661)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[702], questIds=[30000351], questStates=[2]):
            return 사다리안내(self.ctx)


class 사다리안내(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=26300661)
        self.show_guide_summary(entityId=26300662, textId=26300662)
        self.set_effect(triggerIds=[5001,5002], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[703], questIds=[30000351], questStates=[2]):
            return 암전_01(self.ctx)


class 암전_01(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=26300662)
        self.set_effect(triggerIds=[5001,5002], visible=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 암전_02(self.ctx)


class 암전_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_2001')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 마리엔등장_01(self.ctx)


class 마리엔등장_01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=True)
        self.add_cinematic_talk(npcId=11004293, msg='$63000066_CS__63000066_MAIN__0$', duration=2500, align='right')
        self.set_scene_skip(state=스킵종료, action='exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마리엔등장_02(self.ctx)


class 마리엔등장_02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=800):
            return 마리엔등장_03(self.ctx)


class 마리엔등장_03(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Suprise_A'])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마리엔등장_04(self.ctx)


class 마리엔등장_04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 마리엔등장_05(self.ctx)


class 마리엔등장_05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004293, msg='$63000066_CS__63000066_MAIN__1$', duration=2500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마리엔등장_06(self.ctx)


class 마리엔등장_06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마리엔등장_07(self.ctx)


class 마리엔등장_07(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004293, msg='$63000066_CS__63000066_MAIN__2$', duration=3000, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 마리엔등장_08(self.ctx)


class 마리엔등장_08(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 마리엔등장_09(self.ctx)


class 마리엔등장_09(common.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=0, emotionName='Think_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 마리엔등장_10(self.ctx)


class 마리엔등장_10(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 마리엔등장_11(self.ctx)


class 마리엔등장_11(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004293, msg='$63000066_CS__63000066_MAIN__3$', duration=2500, align='right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 마리엔퇴장_01(self.ctx)


class 마리엔퇴장_01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.destroy_monster(spawnIds=[201])
        self.set_effect(triggerIds=[5003], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 마리엔퇴장_02(self.ctx)


class 마리엔퇴장_02(common.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 종료(self.ctx)


class 스킵종료(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        self.face_emotion(spawnId=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.destroy_monster(spawnIds=[201])

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = 준비
