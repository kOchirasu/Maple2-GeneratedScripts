""" trigger/52000106_qd/52000106.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002323], questStates=[1]):
            return 그림자의침략01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002323], questStates=[2]):
            return 그림자의침략완료02(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002325], questStates=[2]):
            return 리엔을떠나다01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002323], questStates=[3]):
            return 그림자의침략완료02(self.ctx)


# ########################그림자의침략 도입부 연출########################
class 그림자의침략01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 그림자의침략02(self.ctx)


class 그림자의침략02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[1000,1001], returnView=False)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 그림자의침략03(self.ctx)


class 그림자의침략03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[1002,1003], returnView=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_ririn_Turn')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 그림자의침략04(self.ctx)


class 그림자의침략04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[700,701,702,703], animationEffect=False)
        self.set_effect(triggerIds=[901], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 그림자의침략05(self.ctx)


class 그림자의침략05(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[704,705,706,707], animationEffect=False)
        self.set_effect(triggerIds=[901], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 그림자의침략06(self.ctx)


class 그림자의침략06(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[708,709,710,711], animationEffect=False)
        self.set_effect(triggerIds=[901], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 그림자의침략07(self.ctx)


class 그림자의침략07(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[712,713,714,715], animationEffect=False)
        self.set_effect(triggerIds=[901], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 그림자의침략08(self.ctx)


class 그림자의침략08(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[716,717,718,719], animationEffect=False)
        self.set_effect(triggerIds=[901], visible=True)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 그림자의침략09(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_ririn_Turn')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.reset_camera(interpolationTime=0.5)
        self.create_monster(spawnIds=[700,701,702,703], animationEffect=False)
        self.create_monster(spawnIds=[704,705,706,707], animationEffect=False)
        self.create_monster(spawnIds=[708,709,710,711], animationEffect=False)
        self.create_monster(spawnIds=[712,713,714,715], animationEffect=False)
        self.create_monster(spawnIds=[716,717,718,719], animationEffect=False)
        self.create_monster(spawnIds=[716,717,718,719], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 그림자의침략09(self.ctx)


# ########################그림자의침략 플레이 진행########################
class 그림자의침략09(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[10011], skillId=70000109, level=1, isPlayer=False, isSkillSet=False) # 초생회
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0.5)
        self.show_guide_summary(entityId=25201061, textId=25201061, duration=5000)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_ririn_go')
        self.add_balloon_talk(spawnId=0, msg='$52000106_QD__52000106__0$', duration=6000, delayTick=1000)
        self.add_balloon_talk(spawnId=101, msg='$52000106_QD__52000106__1$', duration=6000, delayTick=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002323], questStates=[2]):
            return 그림자의침략완료01(self.ctx)


# ########################그림자의침략 마무리########################
class 그림자의침략완료01(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=0, msg='$52000106_QD__52000106__2$', duration=6000, delayTick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 그림자의침략완료02(self.ctx)


class 그림자의침략완료02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 그림자의침략완료03(self.ctx)


class 그림자의침략완료03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0.5)
        self.set_onetime_effect(id=20, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.move_user(mapId=52000106, portalId=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002324], questStates=[1]):
            return 할아버지의물품조사01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002324], questStates=[2]):
            return 할아버지의물품조사01(self.ctx)
        if self.quest_user_detected(boxIds=[10011], questIds=[20002324], questStates=[3]):
            return 할아버지의물품조사01(self.ctx)


# ########################할아버지의 물품 조사########################
class 할아버지의물품조사01(trigger_api.Trigger):
    def on_enter(self):
        self.create_item(spawnIds=[200])
        self.show_guide_summary(entityId=25201062, textId=25201062, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[10011], questIds=[20002325], questStates=[2]):
            return 리엔을떠나다01(self.ctx)


# ########################PC,리엔을 떠나다########################
class 리엔을떠나다01(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=리엔을떠나다09, action='exit')
        self.destroy_monster(spawnIds=[102])
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_ririn_goodBye_0')
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 리엔을떠나다02(self.ctx)


class 리엔을떠나다02(trigger_api.Trigger):
    def on_enter(self):
        self.visible_my_pc(isVisible=False) # 유저 투명 처리
        self.set_onetime_effect(id=30, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[1004,1005], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 리엔을떠나다03(self.ctx)


class 리엔을떠나다03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11003174, msg='$52000106_QD__52000106__3$', duration=4000, align='right')
        self.select_camera_path(pathIds=[1006,1007], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 리엔을떠나다04(self.ctx)


class 리엔을떠나다04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003174, msg='$52000106_QD__52000106__4$', duration=5000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 리엔을떠나다05(self.ctx)


class 리엔을떠나다05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[1008,1009], returnView=False)
        self.add_cinematic_talk(npcId=11003174, illustId='Ririn_normal', msg='$52000106_QD__52000106__5$', duration=4000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 리엔을떠나다06(self.ctx)


class 리엔을떠나다06(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003174, illustId='Ririn_normal', msg='$52000106_QD__52000106__6$', duration=4000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 리엔을떠나다07(self.ctx)


class 리엔을떠나다07(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=40, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 리엔을떠나다08(self.ctx)


class 리엔을떠나다08(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.show_caption(type='VerticalCaption', title='$52000106_QD__52000106__7$', desc='$52000106_QD__52000106__8$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=10000, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 리엔을떠나다08_1(self.ctx)


class 리엔을떠나다08_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 리엔을떠나다09(self.ctx)


class 리엔을떠나다09(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000115, portalId=1)


initial_state = Wait
