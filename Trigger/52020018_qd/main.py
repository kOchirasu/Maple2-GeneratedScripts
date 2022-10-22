""" trigger/52020018_qd/main.xml """
from common import *
import state


#  트로이 여관 216호실 : 52020020  
class idle(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/Eff_Fog_room.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60200150], questStates=[1]):
            return ready()
        if quest_user_detected(boxIds=[2001], questIds=[60200150], questStates=[2]):
            return Battle_End()


class ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        create_monster(spawnIds=[101], arg2=True) # 넬프
        create_monster(spawnIds=[102], arg2=True)
        create_monster(spawnIds=[103], arg2=True)
        create_monster(spawnIds=[104], arg2=True)
        create_monster(spawnIds=[105], arg2=True)
        create_monster(spawnIds=[106], arg2=True) # 조디
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        move_user(mapId=52020018, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return EventScene_01()


class EventScene_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='일부러 그런게 아니야.......')
        set_scene_skip(state=EventScene_end, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_02()


class EventScene_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003723, msg='오호……. 핑계라도 대고 싶으신 겁니까?', duration=3000, illustId='Nelf_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_03()


class EventScene_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003724, msg='실망입니다. $MyPCName$님.', duration=3000, illustId='Jordy_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_04()


class EventScene_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003724, msg='그렇게 믿고 의지했는데…….', duration=3000, illustId='Jordy_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_05()


class EventScene_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003724, msg='절 버리고 가셨으니 평생 $MyPCName$님을 저주 할 겁니다.', duration=3000, illustId='Jordy_normal', align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_06()


class EventScene_06(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='아니야... 아니라고...', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_07()

    def on_exit(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')


class EventScene_07(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=102, msg='저주다! 저주!', duration=2000, delayTick=0)
        add_balloon_talk(spawnId=103, msg='평생 저주 할거다!', duration=2000, delayTick=500)
        add_balloon_talk(spawnId=104, msg='죽어.', duration=2000, delayTick=1000)
        add_balloon_talk(spawnId=105, msg='우리하고 평생 여기 있자.', duration=2000, delayTick=1500)
        add_balloon_talk(spawnId=0, msg='이건 사실이 아니야!!!', duration=2000, delayTick=3000)
        set_pc_emotion_loop(sequenceName='Emotion_Failure_Idle_A', duration=3000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EventScene_end()


class EventScene_end(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')
        set_onetime_effect(id=3, enable=True, path='BG/Common/Eff_Fog_room.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Battle_Ready()


class Battle_Ready(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[102])
        destroy_monster(spawnIds=[103])
        destroy_monster(spawnIds=[104])
        destroy_monster(spawnIds=[105])
        destroy_monster(spawnIds=[106])
        create_monster(spawnIds=[201], arg2=True) # 넬프
        create_monster(spawnIds=[202], arg2=True)
        create_monster(spawnIds=[203], arg2=True)
        create_monster(spawnIds=[204], arg2=True)
        create_monster(spawnIds=[205], arg2=True)
        create_monster(spawnIds=[206], arg2=True) # 조디

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Battle()


class Battle(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='마리오네트들을 처치하고 이곳을 빠져나가자.', arg3='2000', arg4='0')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,203,204,205,206]):
            return Battle_End()


class Battle_End(state.State):
    def on_enter(self):
        set_achievement(type='trigger', achieve='NightmareTroy')
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)


