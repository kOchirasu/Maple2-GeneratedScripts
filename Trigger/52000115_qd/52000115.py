""" trigger/52000115_qd/52000115.xml """
import common


class START(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기01(self.ctx)


class 대기01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[9001], visible=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], visible=True, arg3=0, delay=0, scale=0) # 큐브하나씩부셔지는연출
        self.set_breakable(triggerIds=[3000], enable=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대기02(self.ctx)


class 대기02(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=Skip_1, action='exit')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.create_monster(spawnIds=[200], animationEffect=False) # 검은마법사등장
        self.select_camera_path(pathIds=[2000,2001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=14000):
            return camera01(self.ctx)


class camera01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2002,2003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return camera02(self.ctx)


class camera02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2004,2005], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return camera03(self.ctx)


class camera03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2006,2007], returnView=False)
        self.move_npc(spawnId=200, patrolName='MS2PatrolData_BlackMage') # 마드리아 이동

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return camera05(self.ctx)


class camera05(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2008,2009], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return camera06(self.ctx)


class camera06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2010,2011], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return camera08(self.ctx)


class camera07(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2012,2013], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return camera08(self.ctx)


class camera08(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2014,2015], returnView=False)
        self.destroy_monster(spawnIds=[200])
        self.create_monster(spawnIds=[203], animationEffect=False) # 검은마법사등장

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return camera08b(self.ctx)


class camera08b(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2016,2017], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return camera09_b(self.ctx)


class camera09_b(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Bore_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=400):
            return camera09(self.ctx)


class camera09(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2018], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return camera10(self.ctx)


class camera10(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2020,2019], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            return camera10_b(self.ctx)


class camera10_b(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=203, sequenceName='Attack_01_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1400):
            return camera11(self.ctx)


class camera11(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_blackfast.xml')
        self.set_effect(triggerIds=[9001], visible=True)
        self.select_camera_path(pathIds=[2022,2023], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=700):
            return camera12(self.ctx)


# 오오오오오오오 쉐도우게이트강림 오오오오오오오
class camera12(common.Trigger):
    def on_enter(self):
        self.change_background(dds='SW_BG_Iceage_C.dds')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return camera13(self.ctx)


class camera13(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        self.select_camera_path(pathIds=[2024,2025], returnView=False)
        self.set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025], visible=False, arg3=0, delay=500, scale=1000) # 큐브하나씩부셔지는연출
        self.set_mesh(triggerIds=[4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], visible=False, arg3=0, delay=800, scale=1000) # 큐브하나씩부셔지는연출
        self.set_breakable(triggerIds=[3000], enable=True)
        self.create_monster(spawnIds=[204], animationEffect=False) # 검은마법사등장

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return camera14b(self.ctx)


class camera14b(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025], visible=True, arg3=0, delay=500, scale=1000) # 큐브하나씩부셔지는연출
        self.set_mesh(triggerIds=[4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], visible=True, arg3=0, delay=800, scale=1000) # 큐브하나씩부셔지는연출

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return camera14c(self.ctx)


class camera14c(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025], visible=False, arg3=0, delay=500, scale=1000) # 큐브하나씩부셔지는연출
        self.set_mesh(triggerIds=[4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], visible=False, arg3=0, delay=800, scale=1000) # 큐브하나씩부셔지는연출
        self.select_camera_path(pathIds=[2026,2027], returnView=False)
        self.destroy_monster(spawnIds=[204])
        self.create_monster(spawnIds=[205], animationEffect=False) # 검은마법사등장

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return camera15(self.ctx)


class camera15(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025], visible=True, arg3=0, delay=500, scale=1000) # 큐브하나씩부셔지는연출
        self.set_mesh(triggerIds=[4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], visible=True, arg3=0, delay=800, scale=1000) # 큐브하나씩부셔지는연출
        self.select_camera_path(pathIds=[2028,2029,2030,2031], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return camera16(self.ctx)


class camera16(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025], visible=False, arg3=0, delay=500, scale=1000) # 큐브하나씩부셔지는연출
        self.set_mesh(triggerIds=[4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040,4041,4042,4043,4044,4045,4046,4047,4048,4049,4050,4051,4052], visible=False, arg3=0, delay=800, scale=1000) # 큐브하나씩부셔지는연출
        self.select_camera_path(pathIds=[2032,2033], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return camera17(self.ctx)


class camera17(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return camera18(self.ctx)


class camera18(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11001811, msg='$52000115_QD__52000115__0$', duration=6000, align='center')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return camera19(self.ctx)


class camera19(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit01(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit01(self.ctx)


class Quit01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199], jobCode=10):
            return 기본종료(self.ctx)
        if self.user_detected(boxIds=[199], jobCode=20):
            return 버서커리스항구01(self.ctx)
        if self.user_detected(boxIds=[199], jobCode=30):
            return 트라이아도서관01(self.ctx)
        if self.user_detected(boxIds=[199], jobCode=40):
            self.move_user(mapId=52000139, portalId=1)
            return None
        if self.user_detected(boxIds=[199], jobCode=50):
            return 기본종료(self.ctx)
        if self.user_detected(boxIds=[199], jobCode=60):
            return 기본종료(self.ctx)
        if self.user_detected(boxIds=[199], jobCode=70):
            return 기본종료(self.ctx)
        if self.user_detected(boxIds=[199], jobCode=80):
            return 기본종료(self.ctx)
        if self.user_detected(boxIds=[199], jobCode=90):
            return 기본종료(self.ctx)


class 트라이아도서관01(common.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$52000115_QD__52000115__1$', desc='$52000115_QD__52000115__2$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=10000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트라이아도서관02(self.ctx)


class 트라이아도서관02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000031, portalId=1)


class 버서커리스항구01(common.Trigger):
    def on_enter(self):
        self.show_caption(type='VerticalCaption', title='$52000115_QD__52000115__3$', desc='$52000115_QD__52000115__4$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=10000, scale=2.5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 버서커리스항구02(self.ctx)


class 버서커리스항구02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000062, portalId=13)


class 기본종료(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000062, portalId=1)


initial_state = START
