""" trigger/52000186_qd/52000186.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9002]):
            return 영상재생(self.ctx)


class 영상재생(common.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='common\jp\Lapenta_Frontier.usm', movieId=1)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 묘지전경씬01(self.ctx)
        if self.wait_tick(waitTick=110000):
            return 묘지전경씬01(self.ctx)


class 묘지전경씬01(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[8000,8001,8002,8003], returnView=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return 묘지전경씬02(self.ctx)


class 묘지전경씬02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004,8005], returnView=False)
        self.show_caption(type='VerticalCaption', title='$52000186_QD__52000186__0$', desc='$52000186_QD__52000186__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=7000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 묘지전경씬03(self.ctx)


class 묘지전경씬03(common.Trigger):
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
        self.add_balloon_talk(spawnId=0, msg='$52000186_QD__52000186__2$', duration=6000, delayTick=1000)
        self.show_guide_summary(entityId=25201861, textId=25201861, duration=10000)
        self.create_monster(spawnIds=[4000], animationEffect=False)
        self.create_monster(spawnIds=[4001], animationEffect=False)
        self.create_monster(spawnIds=[4002], animationEffect=False)
        self.create_monster(spawnIds=[4003], animationEffect=False)
        self.create_monster(spawnIds=[4004], animationEffect=False)
        self.create_monster(spawnIds=[4005], animationEffect=False)
        self.create_monster(spawnIds=[4006], animationEffect=False)
        self.create_monster(spawnIds=[4007], animationEffect=False)
        self.create_monster(spawnIds=[4008], animationEffect=False)
        self.create_monster(spawnIds=[4009], animationEffect=False)
        self.create_monster(spawnIds=[4010], animationEffect=False)
        self.create_monster(spawnIds=[2000], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[40002777], questStates=[3]):
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[40002778], questStates=[3]):
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[40002779], questStates=[3]):
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[40002780], questStates=[3]):
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[40002781], questStates=[3]):
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[40002782], questStates=[3]):
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[40002783], questStates=[3]):
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[40002784], questStates=[3]):
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[40002785], questStates=[3]):
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[40002786], questStates=[3]):
            return 출범연설시작01(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[40002787], questStates=[3]):
            return 출범연설시작01(self.ctx)


# ########################씬2 케이틀린 등장########################
class 출범연설시작01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=10, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 출범연설시작02(self.ctx)


class 출범연설시작02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000186, portalId=20)
        self.destroy_monster(spawnIds=[4000])
        self.destroy_monster(spawnIds=[4001])
        self.destroy_monster(spawnIds=[4002])
        self.destroy_monster(spawnIds=[4003])
        self.destroy_monster(spawnIds=[4004])
        self.destroy_monster(spawnIds=[4005])
        self.destroy_monster(spawnIds=[4006])
        self.destroy_monster(spawnIds=[4007])
        self.destroy_monster(spawnIds=[4008])
        self.destroy_monster(spawnIds=[4009])
        self.destroy_monster(spawnIds=[4010])
        self.create_monster(spawnIds=[5000], animationEffect=False)
        self.create_monster(spawnIds=[5001], animationEffect=False)
        self.create_monster(spawnIds=[5002], animationEffect=False)
        self.create_monster(spawnIds=[5003], animationEffect=False)
        self.create_monster(spawnIds=[5004], animationEffect=False)
        self.create_monster(spawnIds=[5005], animationEffect=False)
        self.create_monster(spawnIds=[5006], animationEffect=False)
        self.create_monster(spawnIds=[5007], animationEffect=False)
        self.create_monster(spawnIds=[5008], animationEffect=False)
        self.create_monster(spawnIds=[5009], animationEffect=False)
        self.create_monster(spawnIds=[5010], animationEffect=False)
        self.create_monster(spawnIds=[3000], animationEffect=False)
        self.create_monster(spawnIds=[3001], animationEffect=False)
        self.create_monster(spawnIds=[3002], animationEffect=False)
        self.create_monster(spawnIds=[3003], animationEffect=False)
        self.create_monster(spawnIds=[3004], animationEffect=False)
        self.create_monster(spawnIds=[3005], animationEffect=False)
        self.create_monster(spawnIds=[3006], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 출범연설시작03(self.ctx)


class 출범연설시작03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=10, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002388], questStates=[3]):
            return 베아트리체움직임01(self.ctx)


class 베아트리체움직임01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=3000, patrolName='MS2PatrolData_bche_Run')
        self.move_npc(spawnId=3001, patrolName='MS2PatrolData_alf_Run')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[20002389], questStates=[3]):
            return 연설시퀀스종료01(self.ctx)


class 연설시퀀스종료01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연설시퀀스종료02(self.ctx)


class 연설시퀀스종료02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[5000])
        self.destroy_monster(spawnIds=[5001])
        self.destroy_monster(spawnIds=[5002])
        self.destroy_monster(spawnIds=[5003])
        self.destroy_monster(spawnIds=[5004])
        self.destroy_monster(spawnIds=[5005])
        self.destroy_monster(spawnIds=[5006])
        self.destroy_monster(spawnIds=[5007])
        self.destroy_monster(spawnIds=[5008])
        self.destroy_monster(spawnIds=[5009])
        self.destroy_monster(spawnIds=[5010])
        self.destroy_monster(spawnIds=[3000])
        self.destroy_monster(spawnIds=[3001])
        self.destroy_monster(spawnIds=[3002])
        self.destroy_monster(spawnIds=[3003])
        self.destroy_monster(spawnIds=[3004])
        self.destroy_monster(spawnIds=[3005])
        self.destroy_monster(spawnIds=[3006])
        self.move_user(mapId=52010068, portalId=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 연설시퀀스종료03(self.ctx)


class 연설시퀀스종료03(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=20, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = Wait
