""" trigger/52000119_qd/main2.xml """
from common import *
import state


#  골든타워 8층 : 60100030  
#  랄프:11003187 / 조디:11003169 / 코쿤:11003171 
#  오프닝 연출 
class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[60100060], questStates=[1]):
            return fadeout()


class fadeout(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[105,106])
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ready()


class ready(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4006], returnView=False)
        destroy_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920])
        destroy_monster(spawnIds=[921,922,923,924,925,926,927,928,929])
        create_monster(spawnIds=[105,106], arg2=True) # 105:조디 / 106: 브로커 랄프의 수하
        move_user(mapId=52000119, portalId=6002)
        set_scene_skip(state=fadeout_01, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return fadein()


class fadein(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4006,4007], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user_path(patrolName='MS2PatrolData_3002')
        face_emotion(spawnId=0, emotionName='Object_React_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_01()


#  랄프:11003187 / 조디:11003169 / 코쿤:11003171 
class scene_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4007,4008], returnView=False)
        set_npc_emotion_loop(spawnId=105, sequenceName='Sit_Down_A', duration=6000)
        set_npc_emotion_sequence(spawnId=104, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003187, msg='$52000119_QD__MAIN2__0$', duration=3000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008,4013,4014,4015], returnView=False)
        set_npc_emotion_sequence(spawnId=104, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003187, msg='$52000119_QD__MAIN2__1$', duration=3000, align='Left')
        set_conversation(type=1, spawnId=105, script='$52000119_QD__MAIN2__2$', arg4=3, arg5=0) # 조디

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=104, sequenceName='Talk_A')
        set_npc_emotion_sequence(spawnId=105, sequenceName='Attack_01_B')
        add_cinematic_talk(npcId=11003187, msg='$52000119_QD__MAIN2__3$', duration=3000, align='Left')
        set_conversation(type=1, spawnId=105, script='$52000119_QD__MAIN2__4$', arg4=3, arg5=0) # 조디

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        set_npc_emotion_sequence(spawnId=104, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003187, msg='$52000119_QD__MAIN2__5$', duration=4989, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_05()


class scene_05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=104, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003187, msg='$52000119_QD__MAIN2__6$', duration=8254, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_06()


class scene_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        set_npc_emotion_sequence(spawnId=106, sequenceName='Damg_B')
        add_cinematic_talk(npcId=11003171, msg='$52000119_QD__MAIN2__7$', duration=3000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_07()


class scene_07(state.State):
    def on_enter(self):
        set_sound(triggerId=7001, arg2=True)
        set_npc_emotion_sequence(spawnId=106, sequenceName='Attack_02_A')
        add_cinematic_talk(npcId=11003171, msg='$52000119_QD__MAIN2__8$', duration=3000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_08()


class scene_08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4016], returnView=False)
        set_effect(triggerIds=[5002], visible=True)
        set_npc_emotion_loop(spawnId=106, sequenceName='Attack_Idle_A', duration=8000)
        add_cinematic_talk(npcId=11003171, msg='$52000119_QD__MAIN2__9$', duration=3000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_09()


class scene_09(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4016,4017,4018], returnView=False)
        face_emotion(spawnId=0, emotionName='Object_React_A')
        add_cinematic_talk(npcId=11003171, msg='$52000119_QD__MAIN2__10$', duration=3000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_10()


class scene_10(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4018], returnView=False)
        set_npc_emotion_sequence(spawnId=106, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003171, msg='$52000119_QD__MAIN2__11$', duration=3000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_11()


class scene_11(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4019], returnView=False)
        set_npc_emotion_sequence(spawnId=106, sequenceName='Attack_02_C')
        add_cinematic_talk(npcId=11003171, msg='$52000119_QD__MAIN2__12$', duration=3000, align='Left')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return fadeout_01()


class fadeout_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_sound(triggerId=7001, arg2=False)
        set_sound(triggerId=7002, arg2=True)
        set_effect(triggerIds=[5002], visible=False)
        destroy_monster(spawnIds=[106]) # 106: 코쿤
        create_monster(spawnIds=[998], arg2=True) # 998: 강해진 코쿤
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return fadein_01()


class fadein_01(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0.5)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return msg()


class msg(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52000119_QD__MAIN2__13$', arg3='3000', arg4='0')
        add_balloon_talk(spawnId=997, msg='$52000119_QD__MAIN2__14$', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[998]):
            return fadeout_02()


class fadeout_02(state.State):
    def on_enter(self):
        set_sound(triggerId=7002, arg2=False)
        destroy_monster(spawnIds=[998]) # 106: 코쿤
        set_achievement(type='trigger', achieve='jordysave2')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return end()


class end(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0.5)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


