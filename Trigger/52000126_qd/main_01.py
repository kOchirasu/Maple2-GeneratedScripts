""" trigger/52000126_qd/main_01.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60100210], questStates=[2]):
            return ready()
        if quest_user_detected(boxIds=[2001], questIds=[60100210], questStates=[3]):
            return ready()
        if quest_user_detected(boxIds=[2001], questIds=[60100215], questStates=[1]):
            return ready()
        if quest_user_detected(boxIds=[2001], questIds=[60100215], questStates=[2]):
            return ready()


#  준비 
class ready(state.State):
    def on_enter(self):
        move_user(mapId=52000126, portalId=6001)
        set_sound(triggerId=7002, arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[201], arg2=True)
        set_scene_skip(state=endwaiting, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return move()


class move(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_3001')
        add_balloon_talk(spawnId=201, msg='$52000126_QD__MAIN_01__0$', duration=7000, delayTick=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return talk()


class talk(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Clap_A')
        add_balloon_talk(spawnId=201, msg='$52000126_QD__MAIN_01__1$', duration=3000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return endtalk()


class endtalk(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=201, msg='$52000126_QD__MAIN_01__2$', duration=3000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return endwaiting()


class endwaiting(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        destroy_monster(spawnIds=[201])
        create_monster(spawnIds=[202], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return end()


class end(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


