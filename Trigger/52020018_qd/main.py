""" trigger/52020018_qd/main.xml """
import trigger_api


# 트로이 여관 216호실 : 52020020
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/Eff_Fog_room.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200150], questStates=[1]):
            return ready(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60200150], questStates=[2]):
            return Battle_End(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.create_monster(spawnIds=[101], animationEffect=True) # 넬프
        self.create_monster(spawnIds=[102], animationEffect=True)
        self.create_monster(spawnIds=[103], animationEffect=True)
        self.create_monster(spawnIds=[104], animationEffect=True)
        self.create_monster(spawnIds=[105], animationEffect=True)
        self.create_monster(spawnIds=[106], animationEffect=True) # 조디
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.move_user(mapId=52020018, portalId=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return EventScene_01(self.ctx)


class EventScene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='일부러 그런게 아니야.......')
        self.set_scene_skip(state=EventScene_end, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_02(self.ctx)


class EventScene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11003723, msg='오호……. 핑계라도 대고 싶으신 겁니까?', duration=3000, illustId='Nelf_normal', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_03(self.ctx)


class EventScene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003724, msg='실망입니다. $MyPCName$님.', duration=3000, illustId='Jordy_normal', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_04(self.ctx)


class EventScene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003724, msg='그렇게 믿고 의지했는데…….', duration=3000, illustId='Jordy_normal', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_05(self.ctx)


class EventScene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003724, msg='절 버리고 가셨으니 평생 $MyPCName$님을 저주 할 겁니다.', duration=3000, illustId='Jordy_normal', align='Center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_06(self.ctx)


class EventScene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=0, msg='아니야... 아니라고...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_07(self.ctx)

    def on_exit(self) -> None:
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')


class EventScene_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawnId=102, msg='저주다! 저주!', duration=2000, delayTick=0)
        self.add_balloon_talk(spawnId=103, msg='평생 저주 할거다!', duration=2000, delayTick=500)
        self.add_balloon_talk(spawnId=104, msg='죽어.', duration=2000, delayTick=1000)
        self.add_balloon_talk(spawnId=105, msg='우리하고 평생 여기 있자.', duration=2000, delayTick=1500)
        self.add_balloon_talk(spawnId=0, msg='이건 사실이 아니야!!!', duration=2000, delayTick=3000)
        self.set_pc_emotion_loop(sequenceName='Emotion_Failure_Idle_A', duration=3000)
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return EventScene_end(self.ctx)


class EventScene_end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/Eff_Fog_room.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Battle_Ready(self.ctx)


class Battle_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[102])
        self.destroy_monster(spawnIds=[103])
        self.destroy_monster(spawnIds=[104])
        self.destroy_monster(spawnIds=[105])
        self.destroy_monster(spawnIds=[106])
        self.create_monster(spawnIds=[201], animationEffect=True) # 넬프
        self.create_monster(spawnIds=[202], animationEffect=True)
        self.create_monster(spawnIds=[203], animationEffect=True)
        self.create_monster(spawnIds=[204], animationEffect=True)
        self.create_monster(spawnIds=[205], animationEffect=True)
        self.create_monster(spawnIds=[206], animationEffect=True) # 조디

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Battle(self.ctx)


class Battle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='마리오네트들을 처치하고 이곳을 빠져나가자.', arg3='2000', arg4='0')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_white.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201,202,203,204,205,206]):
            return Battle_End(self.ctx)


class Battle_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(type='trigger', achieve='NightmareTroy')
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)


initial_state = idle
