""" trigger/52000115_qd/52000115.xml """
from common import *
import state


class START(state.State):
    def on_tick(self) -> state.State:
        if true():
            return 대기01()


class 대기01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[9001], visible=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], visible=True, arg3=0, arg4=0, arg5=0) # 큐브하나씩부셔지는연출
        set_breakable(triggerIds=[3000], enabled=False)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대기02()


class 대기02(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_1, arg2='exit')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        create_monster(spawnIds=[200], arg2=False) # 검은마법사등장
        select_camera_path(pathIds=[2000,2001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=14000):
            return camera01()


class camera01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2002,2003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return camera02()


class camera02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2004,2005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return camera03()


class camera03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2006,2007], returnView=False)
        move_npc(spawnId=200, patrolName='MS2PatrolData_BlackMage') # 마드리아 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return camera05()


class camera05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2008,2009], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return camera06()


class camera06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2010,2011], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return camera08()


class camera07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2012,2013], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return camera08()


class camera08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2014,2015], returnView=False)
        destroy_monster(spawnIds=[200])
        create_monster(spawnIds=[203], arg2=False) # 검은마법사등장

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return camera08b()


class camera08b(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2016,2017], returnView=False)

    def on_tick(self) -> state.State:
        if true():
            return camera09_b()


class camera09_b(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=203, sequenceName='Bore_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return camera09()


class camera09(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2018], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return camera10()


class camera10(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2020,2019], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return camera10_b()


class camera10_b(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=203, sequenceName='Attack_01_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1400):
            return camera11()


class camera11(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_blackfast.xml')
        set_effect(triggerIds=[9001], visible=True)
        select_camera_path(pathIds=[2022,2023], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return camera12()


#  오오오오오오오 쉐도우게이트강림 오오오오오오오
class camera12(state.State):
    def on_enter(self):
        change_background(dds='SW_BG_Iceage_C.dds')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return camera13()


class camera13(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        select_camera_path(pathIds=[2024,2025], returnView=False)
        set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025], visible=False, arg3=0, arg4=500, arg5=1000) # 큐브하나씩부셔지는연출
        set_mesh(triggerIds=[4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], visible=False, arg3=0, arg4=800, arg5=1000) # 큐브하나씩부셔지는연출
        set_breakable(triggerIds=[3000], enabled=True)
        create_monster(spawnIds=[204], arg2=False) # 검은마법사등장

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return camera14b()


class camera14b(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025], visible=True, arg3=0, arg4=500, arg5=1000) # 큐브하나씩부셔지는연출
        set_mesh(triggerIds=[4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], visible=True, arg3=0, arg4=800, arg5=1000) # 큐브하나씩부셔지는연출

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return camera14c()


class camera14c(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025], visible=False, arg3=0, arg4=500, arg5=1000) # 큐브하나씩부셔지는연출
        set_mesh(triggerIds=[4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], visible=False, arg3=0, arg4=800, arg5=1000) # 큐브하나씩부셔지는연출
        select_camera_path(pathIds=[2026,2027], returnView=False)
        destroy_monster(spawnIds=[204])
        create_monster(spawnIds=[205], arg2=False) # 검은마법사등장

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return camera15()


class camera15(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025], visible=True, arg3=0, arg4=500, arg5=1000) # 큐브하나씩부셔지는연출
        set_mesh(triggerIds=[4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], visible=True, arg3=0, arg4=800, arg5=1000) # 큐브하나씩부셔지는연출
        select_camera_path(pathIds=[2028,2029,2030,2031], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return camera16()


class camera16(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025], visible=False, arg3=0, arg4=500, arg5=1000) # 큐브하나씩부셔지는연출
        set_mesh(triggerIds=[4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], visible=False, arg3=0, arg4=800, arg5=1000) # 큐브하나씩부셔지는연출
        select_camera_path(pathIds=[2032,2033], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return camera17()


class camera17(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return camera18()


class camera18(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001811, msg='$52000115_QD__52000115__0$', duration=6000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return camera19()


class camera19(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit01()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit01()


class Quit01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199], jobCode=10):
            return 기본종료()
        if user_detected(boxIds=[199], jobCode=20):
            return 버서커리스항구01()
        if user_detected(boxIds=[199], jobCode=30):
            return 트라이아도서관01()
        if user_detected(boxIds=[199], jobCode=40):
            move_user(mapId=52000139, portalId=1)
            return None
        if user_detected(boxIds=[199], jobCode=50):
            return 기본종료()
        if user_detected(boxIds=[199], jobCode=60):
            return 기본종료()
        if user_detected(boxIds=[199], jobCode=70):
            return 기본종료()
        if user_detected(boxIds=[199], jobCode=80):
            return 기본종료()
        if user_detected(boxIds=[199], jobCode=90):
            return 기본종료()


class 트라이아도서관01(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$52000115_QD__52000115__1$', desc='$52000115_QD__52000115__2$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=10000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 트라이아도서관02()


class 트라이아도서관02(state.State):
    def on_enter(self):
        move_user(mapId=2000031, portalId=1)


class 버서커리스항구01(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$52000115_QD__52000115__3$', desc='$52000115_QD__52000115__4$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=10000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 버서커리스항구02()


class 버서커리스항구02(state.State):
    def on_enter(self):
        move_user(mapId=2000062, portalId=13)


class 기본종료(state.State):
    def on_enter(self):
        move_user(mapId=2000062, portalId=1)


