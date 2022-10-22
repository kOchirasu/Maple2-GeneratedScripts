""" trigger/52000127_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=False)
        set_sound(triggerId=7001, arg2=False)
        set_sound(triggerId=7002, arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60100215,60100216,60100217,60100218,60100219,60100220], questStates=[2]):
            return ready()
        if quest_user_detected(boxIds=[2001], questIds=[60100220,60100221,60100222,60100223,60100224,60100225,60100226,60100227,60100228,60100229,60100230], questStates=[2]):
            return open()


class ready(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        create_monster(spawnIds=[101], arg2=True) # 조디

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return setting()


class setting(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        visible_my_pc(isVisible=True)
        select_camera_path(pathIds=[4002], returnView=False)
        move_user(mapId=52000127, portalId=6001)
        set_sound(triggerId=7001, arg2=True)
        set_scene_skip(state=end, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return dreamscene_01()


#  PC 꿈 
class dreamscene_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000127_QD__MAIN__0$', arg3=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return dreamscene_02()


class dreamscene_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000127_QD__MAIN__1$', arg3=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return dreamscene_03()


class dreamscene_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000127_QD__MAIN__2$', arg3=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return dreamscene_04()


class dreamscene_04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000127_QD__MAIN__3$', arg3=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return dreamscene_05()


class dreamscene_05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000127_QD__MAIN__4$', arg3=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return dreamscene_06()


class dreamscene_06(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000127_QD__MAIN__5$', arg3=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return dreamscene_07()


class dreamscene_07(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000127_QD__MAIN__6$', arg3=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_01()


#  연출 
class scene_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_sound(triggerId=7001, arg2=False)
        set_sound(triggerId=7002, arg2=True)
        set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=21000)
        face_emotion(spawnId=0, emotionName='Stun')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        face_emotion(spawnId=0, emotionName='Stun')
        show_caption(type='VerticalCaption', title='$52000127_QD__MAIN__12$', desc='$52000127_QD__MAIN__13$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        face_emotion(spawnId=0, emotionName='Stun')
        add_cinematic_talk(npcId=11003218, msg='$52000127_QD__MAIN__7$', duration=3000, illustId='Jordy_normal', align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False)
        face_emotion(spawnId=0, emotionName='Stun')
        add_cinematic_talk(npcId=11003218, msg='$52000127_QD__MAIN__8$', duration=3000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_05()


class scene_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False)
        add_cinematic_talk(npcId=11003218, msg='$52000127_QD__MAIN__9$', duration=3000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_06()


class scene_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        face_emotion(spawnId=0, emotionName='calm')
        add_cinematic_talk(npcId=0, msg='$52000127_QD__MAIN__10$', duration=3000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_07()


class scene_07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        face_emotion(spawnId=0, emotionName='Ride_Sp_Run_005')
        add_cinematic_talk(npcId=11003218, msg='$52000127_QD__MAIN__11$', duration=3000, align='Right')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return end()


class end(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)


class open(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        visible_my_pc(isVisible=True)
        create_monster(spawnIds=[101], arg2=True) # 조디

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return open2()


class open2(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


