""" trigger/52000186_qd/52000186.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return 영상재생()


class 영상재생(state.State):
    def on_enter(self):
        create_widget(type='SceneMovie')
        play_scene_movie(fileName='common\jp\Lapenta_Frontier.usm', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 묘지전경씬01()
        if wait_tick(waitTick=110000):
            return 묘지전경씬01()


class 묘지전경씬01(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[8000,8001,8002,8003], returnView=False)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 묘지전경씬02()


class 묘지전경씬02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004,8005], returnView=False)
        show_caption(type='VerticalCaption', title='$52000186_QD__52000186__0$', desc='$52000186_QD__52000186__1$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=7000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 묘지전경씬03()


class 묘지전경씬03(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit01()


class Quit01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit02()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit02()


class Quit02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        add_balloon_talk(spawnId=0, msg='$52000186_QD__52000186__2$', duration=6000, delayTick=1000)
        show_guide_summary(entityId=25201861, textId=25201861, duration=10000)
        create_monster(spawnIds=[4000], arg2=False)
        create_monster(spawnIds=[4001], arg2=False)
        create_monster(spawnIds=[4002], arg2=False)
        create_monster(spawnIds=[4003], arg2=False)
        create_monster(spawnIds=[4004], arg2=False)
        create_monster(spawnIds=[4005], arg2=False)
        create_monster(spawnIds=[4006], arg2=False)
        create_monster(spawnIds=[4007], arg2=False)
        create_monster(spawnIds=[4008], arg2=False)
        create_monster(spawnIds=[4009], arg2=False)
        create_monster(spawnIds=[4010], arg2=False)
        create_monster(spawnIds=[2000], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[40002777], questStates=[3]):
            return 출범연설시작01()
        if quest_user_detected(boxIds=[9001], questIds=[40002778], questStates=[3]):
            return 출범연설시작01()
        if quest_user_detected(boxIds=[9001], questIds=[40002779], questStates=[3]):
            return 출범연설시작01()
        if quest_user_detected(boxIds=[9001], questIds=[40002780], questStates=[3]):
            return 출범연설시작01()
        if quest_user_detected(boxIds=[9001], questIds=[40002781], questStates=[3]):
            return 출범연설시작01()
        if quest_user_detected(boxIds=[9001], questIds=[40002782], questStates=[3]):
            return 출범연설시작01()
        if quest_user_detected(boxIds=[9001], questIds=[40002783], questStates=[3]):
            return 출범연설시작01()
        if quest_user_detected(boxIds=[9001], questIds=[40002784], questStates=[3]):
            return 출범연설시작01()
        if quest_user_detected(boxIds=[9001], questIds=[40002785], questStates=[3]):
            return 출범연설시작01()
        if quest_user_detected(boxIds=[9001], questIds=[40002786], questStates=[3]):
            return 출범연설시작01()
        if quest_user_detected(boxIds=[9001], questIds=[40002787], questStates=[3]):
            return 출범연설시작01()


#  ########################씬2 케이틀린 등장########################
class 출범연설시작01(state.State):
    def on_enter(self):
        set_onetime_effect(id=10, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 출범연설시작02()


class 출범연설시작02(state.State):
    def on_enter(self):
        move_user(mapId=52000186, portalId=20)
        destroy_monster(spawnIds=[4000])
        destroy_monster(spawnIds=[4001])
        destroy_monster(spawnIds=[4002])
        destroy_monster(spawnIds=[4003])
        destroy_monster(spawnIds=[4004])
        destroy_monster(spawnIds=[4005])
        destroy_monster(spawnIds=[4006])
        destroy_monster(spawnIds=[4007])
        destroy_monster(spawnIds=[4008])
        destroy_monster(spawnIds=[4009])
        destroy_monster(spawnIds=[4010])
        create_monster(spawnIds=[5000], arg2=False)
        create_monster(spawnIds=[5001], arg2=False)
        create_monster(spawnIds=[5002], arg2=False)
        create_monster(spawnIds=[5003], arg2=False)
        create_monster(spawnIds=[5004], arg2=False)
        create_monster(spawnIds=[5005], arg2=False)
        create_monster(spawnIds=[5006], arg2=False)
        create_monster(spawnIds=[5007], arg2=False)
        create_monster(spawnIds=[5008], arg2=False)
        create_monster(spawnIds=[5009], arg2=False)
        create_monster(spawnIds=[5010], arg2=False)
        create_monster(spawnIds=[3000], arg2=False)
        create_monster(spawnIds=[3001], arg2=False)
        create_monster(spawnIds=[3002], arg2=False)
        create_monster(spawnIds=[3003], arg2=False)
        create_monster(spawnIds=[3004], arg2=False)
        create_monster(spawnIds=[3005], arg2=False)
        create_monster(spawnIds=[3006], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 출범연설시작03()


class 출범연설시작03(state.State):
    def on_enter(self):
        set_onetime_effect(id=10, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002388], questStates=[3]):
            return 베아트리체움직임01()


class 베아트리체움직임01(state.State):
    def on_enter(self):
        move_npc(spawnId=3000, patrolName='MS2PatrolData_bche_Run')
        move_npc(spawnId=3001, patrolName='MS2PatrolData_alf_Run')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[20002389], questStates=[3]):
            return 연설시퀀스종료01()


class 연설시퀀스종료01(state.State):
    def on_enter(self):
        set_onetime_effect(id=20, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연설시퀀스종료02()


class 연설시퀀스종료02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[5000])
        destroy_monster(spawnIds=[5001])
        destroy_monster(spawnIds=[5002])
        destroy_monster(spawnIds=[5003])
        destroy_monster(spawnIds=[5004])
        destroy_monster(spawnIds=[5005])
        destroy_monster(spawnIds=[5006])
        destroy_monster(spawnIds=[5007])
        destroy_monster(spawnIds=[5008])
        destroy_monster(spawnIds=[5009])
        destroy_monster(spawnIds=[5010])
        destroy_monster(spawnIds=[3000])
        destroy_monster(spawnIds=[3001])
        destroy_monster(spawnIds=[3002])
        destroy_monster(spawnIds=[3003])
        destroy_monster(spawnIds=[3004])
        destroy_monster(spawnIds=[3005])
        destroy_monster(spawnIds=[3006])
        move_user(mapId=52010068, portalId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연설시퀀스종료03()


class 연설시퀀스종료03(state.State):
    def on_enter(self):
        set_onetime_effect(id=20, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


