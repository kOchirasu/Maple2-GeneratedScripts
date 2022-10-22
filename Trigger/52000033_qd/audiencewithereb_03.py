""" trigger/52000033_qd/audiencewithereb_03.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[60100245], questStates=[2]):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_scene_skip(state=end, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return pcmove()


class pcmove(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1007')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return ErebTalk_01()


class ErebTalk_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[700], returnView=False) # 에레브 얼굴로 클로즈업
        add_cinematic_talk(npcId=11001663, illustId='Ereb_normal', msg='$52000033_QD__AUDIENCEWITHEREB_03__0$', duration=3000, delayTick=0, align='left') # 에레브

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ErebTalk_02()


class ErebTalk_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[901], returnView=False) # 에레브 얼굴로 클로즈업
        add_cinematic_talk(npcId=11001663, msg='$52000033_QD__AUDIENCEWITHEREB_03__1$', duration=3000, delayTick=0, align='left') # 에레브

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ErebTalk_03()


class ErebTalk_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[601], returnView=False) # 뒷 뷰

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return fadeout()


class fadeout(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[601], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return story_01()


class story_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000033_QD__AUDIENCEWITHEREB_03__2$', arg3=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return story_02()


class story_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000033_QD__AUDIENCEWITHEREB_03__3$', arg3=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return story_03()


class story_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='$52000033_QD__AUDIENCEWITHEREB_03__4$', arg3=False)
        move_npc(spawnId=601, patrolName='MS2PatrolData_1005')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return fadein()


class fadein(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ErebTalk_04()


class ErebTalk_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001663, illustId='Ereb_surprise', msg='$52000033_QD__AUDIENCEWITHEREB_03__5$', duration=3000, delayTick=0, align='left') # 에레브

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ErebTalk_05()


class ErebTalk_05(state.State):
    def on_enter(self):
        set_sound(triggerId=7001, arg2=True)
        add_cinematic_talk(npcId=11001663, illustId='Ereb_closeEye', msg='$52000033_QD__AUDIENCEWITHEREB_03__6$', duration=3000, delayTick=0, align='left') # 에레브
        add_balloon_talk(spawnId=401, msg='$52000033_QD__AUDIENCEWITHEREB_03__7$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ErebTalk_06()


class ErebTalk_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001663, illustId='Ereb_serious', msg='$52000033_QD__AUDIENCEWITHEREB_03__8$', duration=3000, delayTick=0, align='left') # 에레브
        move_npc(spawnId=601, patrolName='MS2PatrolData_1006')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ErebTalk_07()


class ErebTalk_07(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001663, illustId='Ereb_closeEye', msg='$52000033_QD__AUDIENCEWITHEREB_03__9$', duration=3000, delayTick=0, align='left') # 에레브
        destroy_monster(spawnIds=[601])
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return end()


class end(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[601])
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


