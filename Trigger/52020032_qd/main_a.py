""" trigger/52020032_qd/main_a.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_actor(triggerId=8001, visible=False, initialSequence='Damg_Idle_B')
        set_interact_object(triggerIds=[10001281], state=0)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200100], questStates=[3]):
            return Del_Npc()
        if quest_user_detected(boxIds=[2001], questIds=[60200095], questStates=[1]):
            return Ready()
        if quest_user_detected(boxIds=[2001], questIds=[60200095], questStates=[2]):
            return Exit()
        if quest_user_detected(boxIds=[2001], questIds=[60200095], questStates=[3]):
            return Exit()
        if quest_user_detected(boxIds=[2001], questIds=[60200100], questStates=[1]):
            return Exit()
        if quest_user_detected(boxIds=[2001], questIds=[60200100], questStates=[2]):
            return Exit()


class Ready(state.State):
    def on_enter(self):
        set_actor(triggerId=8001, visible=True, initialSequence='Damg_Idle_B')
        create_monster(spawnIds=[102], arg2=True) # 미카엘
        create_monster(spawnIds=[201], arg2=True)
        create_monster(spawnIds=[202], arg2=True)
        create_monster(spawnIds=[203], arg2=True)
        create_monster(spawnIds=[204], arg2=True)
        create_monster(spawnIds=[205], arg2=True)
        create_monster(spawnIds=[206], arg2=True)
        create_monster(spawnIds=[207], arg2=True)
        create_monster(spawnIds=[301], arg2=True) # 폭주 마리오네트

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[60200095], questStates=[1]):
            return Battle_A()


class Battle_A(state.State):
    def on_enter(self):
        change_monster(removeSpawnId=201, addSpawnId=601)
        change_monster(removeSpawnId=202, addSpawnId=602)
        change_monster(removeSpawnId=203, addSpawnId=603)
        change_monster(removeSpawnId=204, addSpawnId=604)
        change_monster(removeSpawnId=205, addSpawnId=605)
        change_monster(removeSpawnId=206, addSpawnId=606)
        change_monster(removeSpawnId=207, addSpawnId=607)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[601,602,603,604,605,606,607]):
            return Event_01()


class Event_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4001], returnView=False)
        set_scene_skip(state=Battle_B, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Event_02()


class Event_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002,4003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_03()


class Event_03(state.State):
    def on_enter(self):
        move_npc(spawnId=301, patrolName='MS2PatrolData_3001')
        select_camera_path(pathIds=[4004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Event_04()


class Event_04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=301, sequenceName='Attack_01_B')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Battle_B()


class Battle_B(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0.5)
        change_monster(removeSpawnId=301, addSpawnId=701)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[701]):
            return Event_End()


class Event_End(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])
        set_interact_object(triggerIds=[10001281], state=1)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200095], questStates=[2]):
            return Exit()


class Exit(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True) # 미카엘
        set_actor(triggerId=8001, visible=False, initialSequence='Damg_Idle_B')


class Del_Npc(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        set_actor(triggerId=8001, visible=False, initialSequence='Damg_Idle_B')


