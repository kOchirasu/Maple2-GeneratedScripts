""" trigger/52020020_qd/main_b.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200135], questStates=[2]):
            return ready()
        if quest_user_detected(boxIds=[2001], questIds=[60200135,60200136,60200137,60200138,60200139,60200140], questStates=[3]):
            return EndReady()


class ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        move_user(mapId=52020020, portalId=6002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Monologue_01()


class Monologue_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=0, msg='곧 알현식이 열린다고?', duration=2500)
        set_pc_emotion_loop(sequenceName='Object_React_H', duration=16000)
        set_scene_skip(state=EndReady, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return Monologue_02()


class Monologue_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='그럼 여기가 $map:02000001$$pp:라는,이라는$거야?', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return Monologue_03()


class Monologue_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='분명 알현식은 취소되었을텐데?', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Walk()

    def on_exit(self):
        set_cinematic_ui(type=4)


class Walk(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Door()


class Door(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventTalk_01()


class EventTalk_01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003590, msg='앗! 일어나 계셨습니까?', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return EventTalk_02()


class EventTalk_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='설마....', duration=2500, align='Right')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return EventTalk_03()


class EventTalk_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='설마.... 그럴리가 없어....', duration=3000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EndReady()


class EndReady(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_sound(triggerId=7001, arg2=True)
        set_pc_emotion_loop(sequenceName='Idle_A', duration=100)
        create_monster(spawnIds=[201], arg2=True) # 조디

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return exit()


class exit(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')


