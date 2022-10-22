""" trigger/52020011_qd/main_b.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        set_actor(triggerId=8001, visible=False, initialSequence='Attack_Idle_A')
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200130], questStates=[2]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Set()


class Set(state.State):
    def on_enter(self):
        move_user(mapId=52020011, portalId=6001)
        select_camera_path(pathIds=[4009], returnView=False)
        set_actor(triggerId=8001, visible=True, initialSequence='Attack_Idle_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Go()


class Go(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003599, msg='나 $npcName:11003599$의 이름으로 명한다.', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Scene_01()


class Scene_01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003599, msg='이 땅의 모든 저주받은 존재여! 깊고 어두운 곳으로 떨어져라!', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Scene_02()


class Scene_02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True)
        set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Scene_03()


class Scene_03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5003], visible=True)
        set_effect(triggerIds=[5004], visible=True)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        add_balloon_talk(spawnId=0, msg='!', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=700):
            return Scene_Exit()


class Scene_Exit(state.State):
    def on_enter(self):
        move_user(mapId=52020020, portalId=6001)


