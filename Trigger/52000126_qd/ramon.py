""" trigger/52000126_qd/ramon.xml """
from common import *
import state


#  장사꾼의 목격담(60100205) 완료 가능 상태 연출  
class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60100205], questStates=[2]):
            return fadein()


#  준비 
class fadein(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_scene_skip(state=end, arg2='exit')
        select_camera_path(pathIds=[4101], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return fadeout()


class fadeout(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return camera_01()


class camera_01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        select_camera_path(pathIds=[4101,4102], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return camera_02()


class camera_02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        select_camera_path(pathIds=[4102,4103], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return camera_03()


class camera_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003209, msg='$52000126_QD__RAMON__0$', duration=2000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return end()


class end(state.State):
    def on_enter(self):
        set_scene_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)


