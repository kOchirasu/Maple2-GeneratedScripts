""" trigger/63000042_cs/wakeup02.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_sound(triggerId=7001, arg2=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[60100005,60100006,60100007,60100008,60100009,60100010], questStates=[2]):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[102])
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        move_user(mapId=63000042, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return talk_01()


class talk_01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$63000042_CS__WAKEUP02__0$', duration=3000)
        set_scene_skip(state=sitready, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return talk_02()


class talk_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$63000042_CS__WAKEUP02__1$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return talk_03()


class talk_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$63000042_CS__WAKEUP02__2$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return talk_04()


class talk_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003145, msg='$63000042_CS__WAKEUP02__3$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return talk_05()


class talk_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$63000042_CS__WAKEUP02__4$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return talk_06()


class talk_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$63000042_CS__WAKEUP02__5$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return talk_07()


class talk_07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$63000042_CS__WAKEUP02__6$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return talk_08()


class talk_08(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003145, msg='$63000042_CS__WAKEUP02__7$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return talk_09()


class talk_09(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='$63000042_CS__WAKEUP02__8$', duration=3000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return sitready()


class sitready(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=13000)
        set_sound(triggerId=7002, arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return fadein()


class fadein(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        create_monster(spawnIds=[103], arg2=False) # 프레이 스폰

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return praymove_01()


class praymove_01(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_103')
        add_cinematic_talk(npcId=11003165, illustId='Fray_normal', msg='$63000042_CS__WAKEUP02__9$', duration=3000, align='Left')
        set_scene_skip(state=end, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return praytalk_02()


class praytalk_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003165, msg='$63000042_CS__WAKEUP02__10$', duration=3000)
        select_camera_path(pathIds=[502], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return pray()


class pray(state.State):
    def on_enter(self):
        show_caption(scale=2.5, type='NameCaption', title='$63000042_CS__WAKEUP02__11$', desc='$63000042_CS__WAKEUP02__12$', align='centerRight', offsetRateX=0.5, duration=4000)
        select_camera_path(pathIds=[502,503], returnView=False)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return end()


class end(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=100)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[60100010], questStates=[1]):
            return warp()


class warp(state.State):
    def on_enter(self):
        move_user(mapId=52000033, portalId=1)


