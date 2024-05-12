""" trigger/52000037_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=4000, visible=False, initialSequence='Dead_A') # NelfActor
        self.set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, delay=0, scale=0)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/Sound/Eff_System_Dark_Ending_Chord_01.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.set_onetime_effect(id=6, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[60100125], questStates=[1]):
            return ready(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[60100125,60100126,60100127,60100128,60100129,60100130,60100131,60100132,60100133,60100134,60100135], questStates=[2]):
            return npcspawn_02(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[60100135], questStates=[3]):
            return npcspawn_03(self.ctx)


# 첫 진입 시 연출
class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_sound(triggerId=7001, enable=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return waitng(self.ctx)


class waitng(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.move_user(mapId=52000037, portalId=1)
        self.create_monster(spawnIds=[604], animationEffect=True) # 604:연출용 고호: 11003204
        self.create_monster(spawnIds=[602], animationEffect=True) # 602:연출용 조디: 11003202

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return startscene(self.ctx)


class startscene(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[4001,4002,4003,4004,4005,4006,4007], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_2101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_01(self.ctx)


# 조디 연출 시작
class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=602, patrolName='MS2PatrolData_3002')
        self.add_cinematic_talk(npcId=11003202, illustId='Jordy_normal', msg='$52000037_QD__MAIN__0$', duration=3000, align='Right')
        self.set_scene_skip(state=fadeout, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=604, patrolName='MS2PatrolData_3004')
        self.add_cinematic_talk(npcId=11003204, msg='$52000037_QD__MAIN__1$', duration=2000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003202, illustId='Jordy_normal', msg='$52000037_QD__MAIN__2$', duration=4000, align='Right')
        self.set_npc_emotion_sequence(spawnId=602, sequenceName='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003204, msg='$52000037_QD__MAIN__3$', duration=2000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=602, sequenceName='Attack_01_B')
        self.add_cinematic_talk(npcId=11003202, illustId='Jordy_normal', msg='$52000037_QD__MAIN__4$', duration=3000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=604, sequenceName='Bore_C')
        self.add_cinematic_talk(npcId=11003204, msg='$52000037_QD__MAIN__5$', duration=3000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=602, sequenceName='Dead_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3735):
            return scene_08(self.ctx)


class scene_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=602, patrolName='MS2PatrolData_3003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_09(self.ctx)


class scene_09(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_10(self.ctx)


class scene_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_11(self.ctx)


class scene_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4009], returnView=False)
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_12(self.ctx)


class scene_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return scene_13(self.ctx)


class scene_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4009], returnView=False)
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return scene_14(self.ctx)


class scene_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4010], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_15(self.ctx)


class scene_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=602, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003202, illustId='Jordy_normal', msg='$52000037_QD__MAIN__6$', duration=3000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_16(self.ctx)


class scene_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=604, sequenceName='Bore_C')
        self.add_cinematic_talk(npcId=11003204, msg='$52000037_QD__MAIN__7$', duration=3000, align='Right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return fadeout(self.ctx)


class fadeout(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return endready(self.ctx)


class endready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[602,604])
        self.create_monster(spawnIds=[601], animationEffect=True) # 601:퀘스트 고호: 11003204
        self.create_monster(spawnIds=[603], animationEffect=True) # 603:퀘스트 조디: 11003203
        self.reset_camera(interpolationTime=0)
        self.set_sound(triggerId=7001, enable=False)
        self.set_achievement(triggerId=9900, type='trigger', achieve='nelfmissing')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


# 퀘스트 진행 및 완료 상태
class npcspawn_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[601,602,603,604])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return npcspawn_02_A(self.ctx)


class npcspawn_02_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[603], animationEffect=True) # 603:퀘스트 조디
        self.create_monster(spawnIds=[601], animationEffect=True) # 601:고호


class npcspawn_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[601,602,603,604])


initial_state = idle
