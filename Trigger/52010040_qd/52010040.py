""" trigger/52010040_qd/52010040.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[91000013], questStates=[2]):
            return 도입부연출01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000015], questStates=[3]):
            return 엔딩연출01(self.ctx)


class 도입부연출01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[200], animationEffect=False) # 블리체
        self.create_monster(spawnIds=[300], animationEffect=False) # 블랙아이
        self.create_monster(spawnIds=[301], animationEffect=False) # 알론
        self.create_monster(spawnIds=[302], animationEffect=False) # 프레이
        self.create_monster(spawnIds=[303], animationEffect=False) # 오스칼
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 도입부연출02(self.ctx)


class 도입부연출02(trigger_api.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$52010040_QD__52010040__0$', desc='$52010040_QD__52010040__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=7000, scale=2.5)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[2000,2001,2002], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 도입부연출03_b(self.ctx)


class 도입부연출03_b(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_blicheCome') # 블리체 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 도입부연출03(self.ctx)


class 도입부연출03(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 도입부연출04(self.ctx)


class 도입부연출04(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9002]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


# ########################튜토리얼 종료씬########################
class 엔딩연출01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[200], animationEffect=False) # 블리체
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 엔딩연출02(self.ctx)


class 엔딩연출02(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=quit, action='nextState')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.add_cinematic_talk(npcId=11003536, illustId='Neirin_normal', msg='$52010040_QD__52010040__2$', duration=6200, align='right')
        self.select_camera_path(pathIds=[2012,2013], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_blicheCome')
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_bliche_front') # 블리체 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 엔딩연출03(self.ctx)


class 엔딩연출03(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003533, illustId='Bliche_normal', msg='$52010040_QD__52010040__3$', duration=4000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 엔딩연출04(self.ctx)


class 엔딩연출04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003533, illustId='Bliche_normal', msg='$52010040_QD__52010040__4$', duration=5400, align='right')
        self.select_camera_path(pathIds=[2010,2011,2014], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 엔딩연출05(self.ctx)


class 엔딩연출05(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003533, illustId='Bliche_normal', msg='$52010040_QD__52010040__5$', duration=4000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4100):
            return 엔딩연출06_b(self.ctx)


class 엔딩연출06_b(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003533, illustId='Bliche_normal', msg='$52010040_QD__52010040__6$', duration=4000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return 엔딩연출06(self.ctx)


class 엔딩연출06(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 엔딩연출07(self.ctx)


class 엔딩연출07(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return quit(self.ctx)


class quit(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000422, portalId=3)


initial_state = Wait
