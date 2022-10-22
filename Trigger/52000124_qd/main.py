""" trigger/52000124_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60100105,60100106,60100107,60100108,60100109,60100110], questStates=[2]):
            return ready()
        if quest_user_detected(boxIds=[2001], questIds=[60100110], questStates=[3]):
            return delnpc()


#  준비 
class ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        destroy_monster(spawnIds=[201])
        create_monster(spawnIds=[202], arg2=True) # 연출용 카트반 (11003195)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return camera()


class camera(state.State):
    def on_enter(self):
        select_camera(triggerId=4001, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start()


class start(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_01()


#  이벤트 씬 시작 
class scene_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001,4002], returnView=False)
        set_npc_emotion_sequence(spawnId=202, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003195, msg='$52000124_QD__MAIN__0$', duration=2000, align='right')
        set_scene_skip(state=scene_07, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=202, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003195, msg='$52000124_QD__MAIN__1$', duration=2000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        add_cinematic_talk(npcId=11000069, msg='$52000124_QD__MAIN__2$', duration=2000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        move_npc(spawnId=202, patrolName='MS2PatrolData_3001')
        add_cinematic_talk(npcId=11003195, msg='$52000124_QD__MAIN__3$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_05()


class scene_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005], returnView=False)
        set_npc_emotion_loop(spawnId=101, sequenceName='Sit_down_A', duration=1E+12)
        add_cinematic_talk(npcId=11000069, msg='$52000124_QD__MAIN__4$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_06()


class scene_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        add_cinematic_talk(npcId=11003195, msg='$52000124_QD__MAIN__5$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_07()


class scene_07(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return end()


class end(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True) # 카트반(11003196)
        destroy_monster(spawnIds=[202]) # 연출용 카트반(11003195)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60100110], questStates=[2]):
            return warptalk()


class warptalk(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=201, msg='$52000124_QD__MAIN__6$', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return warp()


class warp(state.State):
    def on_enter(self):
        move_user(mapId=52000073, portalId=4)


#  delnpc 
class delnpc(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201,202])


