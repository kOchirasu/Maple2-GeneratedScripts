""" trigger/52020020_qd/main_a.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200130], questStates=[2]):
            return ready()
        if quest_user_detected(boxIds=[2001], questIds=[60200130], questStates=[3]):
            return end()


class ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        move_user(mapId=52020020, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Monologue_01()


class Monologue_01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='으으.......', duration=2500, align='Right')
        set_scene_skip(state=end, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return Monologue_02()


class Monologue_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='도대체 무슨 일이 일어난 거지?', duration=2500, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return Monologue_03()


class Monologue_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='.......', duration=3000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Monologue_04()


class Monologue_04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=3000)
        add_cinematic_talk(npcId=0, msg='잠깐! 여기는?!', duration=3000, align='Right')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return end()


class end(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')


