""" trigger/52020032_qd/main_a.xml """
import common


class Idle(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=8001, visible=False, initialSequence='Damg_Idle_B')
        self.set_interact_object(triggerIds=[10001281], state=0)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200100], questStates=[3]):
            return Del_Npc(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200095], questStates=[1]):
            return Ready(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200095], questStates=[2]):
            return Exit(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200095], questStates=[3]):
            return Exit(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200100], questStates=[1]):
            return Exit(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200100], questStates=[2]):
            return Exit(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=8001, visible=True, initialSequence='Damg_Idle_B')
        self.create_monster(spawnIds=[102], animationEffect=True) # 미카엘
        self.create_monster(spawnIds=[201], animationEffect=True)
        self.create_monster(spawnIds=[202], animationEffect=True)
        self.create_monster(spawnIds=[203], animationEffect=True)
        self.create_monster(spawnIds=[204], animationEffect=True)
        self.create_monster(spawnIds=[205], animationEffect=True)
        self.create_monster(spawnIds=[206], animationEffect=True)
        self.create_monster(spawnIds=[207], animationEffect=True)
        self.create_monster(spawnIds=[301], animationEffect=True) # 폭주 마리오네트

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[60200095], questStates=[1]):
            return Battle_A(self.ctx)


class Battle_A(common.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=201, addSpawnId=601)
        self.change_monster(removeSpawnId=202, addSpawnId=602)
        self.change_monster(removeSpawnId=203, addSpawnId=603)
        self.change_monster(removeSpawnId=204, addSpawnId=604)
        self.change_monster(removeSpawnId=205, addSpawnId=605)
        self.change_monster(removeSpawnId=206, addSpawnId=606)
        self.change_monster(removeSpawnId=207, addSpawnId=607)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[601,602,603,604,605,606,607]):
            return Event_01(self.ctx)


class Event_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.set_scene_skip(state=Battle_B, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Event_02(self.ctx)


class Event_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4002,4003], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_03(self.ctx)


class Event_03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_3001')
        self.select_camera_path(pathIds=[4004], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Event_04(self.ctx)


class Event_04(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=301, sequenceName='Attack_01_B')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Battle_B(self.ctx)


class Battle_B(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0.5)
        self.change_monster(removeSpawnId=301, addSpawnId=701)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[701]):
            return Event_End(self.ctx)


class Event_End(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102])
        self.set_interact_object(triggerIds=[10001281], state=1)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200095], questStates=[2]):
            return Exit(self.ctx)


class Exit(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True) # 미카엘
        self.set_actor(triggerId=8001, visible=False, initialSequence='Damg_Idle_B')


class Del_Npc(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.set_actor(triggerId=8001, visible=False, initialSequence='Damg_Idle_B')


initial_state = Idle
