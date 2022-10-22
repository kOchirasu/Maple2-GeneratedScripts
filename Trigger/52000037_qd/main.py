""" trigger/52000037_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_actor(triggerId=4000, visible=False, initialSequence='Dead_A') # NelfActor
        set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, arg4=0, arg5=0)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/Sound/Eff_System_Dark_Ending_Chord_01.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        set_onetime_effect(id=4, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        set_onetime_effect(id=5, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        set_onetime_effect(id=6, enable=False, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[60100125], questStates=[1]):
            return ready()
        if quest_user_detected(boxIds=[9000], questIds=[60100125,60100126,60100127,60100128,60100129,60100130,60100131,60100132,60100133,60100134,60100135], questStates=[2]):
            return npcspawn_02()
        if quest_user_detected(boxIds=[9000], questIds=[60100135], questStates=[3]):
            return npcspawn_03()


#  첫 진입 시 연출 
class ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_sound(triggerId=7001, arg2=True)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return waitng()


class waitng(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False)
        move_user(mapId=52000037, portalId=1)
        create_monster(spawnIds=[604], arg2=True) # 604:연출용 고호: 11003204
        create_monster(spawnIds=[602], arg2=True) # 602:연출용 조디: 11003202

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return startscene()


class startscene(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[4001,4002,4003,4004,4005,4006,4007], returnView=False)
        move_user_path(patrolName='MS2PatrolData_2101')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_01()


#  조디 연출 시작 
class scene_01(state.State):
    def on_enter(self):
        move_npc(spawnId=602, patrolName='MS2PatrolData_3002')
        add_cinematic_talk(npcId=11003202, illustId='Jordy_normal', msg='$52000037_QD__MAIN__0$', duration=3000, align='Right')
        set_scene_skip(state=fadeout, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        move_npc(spawnId=604, patrolName='MS2PatrolData_3004')
        add_cinematic_talk(npcId=11003204, msg='$52000037_QD__MAIN__1$', duration=2000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003202, illustId='Jordy_normal', msg='$52000037_QD__MAIN__2$', duration=4000, align='Right')
        set_npc_emotion_sequence(spawnId=602, sequenceName='Bore_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003204, msg='$52000037_QD__MAIN__3$', duration=2000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_05()


class scene_05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=602, sequenceName='Attack_01_B')
        add_cinematic_talk(npcId=11003202, illustId='Jordy_normal', msg='$52000037_QD__MAIN__4$', duration=3000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_06()


class scene_06(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=604, sequenceName='Bore_C')
        add_cinematic_talk(npcId=11003204, msg='$52000037_QD__MAIN__5$', duration=3000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_07()


class scene_07(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=602, sequenceName='Dead_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3735):
            return scene_08()


class scene_08(state.State):
    def on_enter(self):
        move_npc(spawnId=602, patrolName='MS2PatrolData_3003')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_09()


class scene_09(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_10()


class scene_10(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        set_onetime_effect(id=3, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_11()


class scene_11(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        set_onetime_effect(id=4, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_12()


class scene_12(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        set_onetime_effect(id=5, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return scene_13()


class scene_13(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        set_onetime_effect(id=6, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return scene_14()


class scene_14(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4010], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_15()


class scene_15(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=602, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003202, illustId='Jordy_normal', msg='$52000037_QD__MAIN__6$', duration=3000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_16()


class scene_16(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=604, sequenceName='Bore_C')
        add_cinematic_talk(npcId=11003204, msg='$52000037_QD__MAIN__7$', duration=3000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return fadeout()


class fadeout(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return endready()


class endready(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[602,604])
        create_monster(spawnIds=[601], arg2=True) # 601:퀘스트 고호: 11003204
        create_monster(spawnIds=[603], arg2=True) # 603:퀘스트 조디: 11003203
        reset_camera(interpolationTime=0)
        set_sound(triggerId=7001, arg2=False)
        set_achievement(triggerId=9900, type='trigger', achieve='nelfmissing')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return end()


class end(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


#  퀘스트 진행 및 완료 상태 
class npcspawn_02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[601,602,603,604])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return npcspawn_02_A()


class npcspawn_02_A(state.State):
    def on_enter(self):
        create_monster(spawnIds=[603], arg2=True) # 603:퀘스트 조디
        create_monster(spawnIds=[601], arg2=True) # 601:고호


class npcspawn_03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[601,602,603,604])


