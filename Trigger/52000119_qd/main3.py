""" trigger/52000119_qd/main3.xml """
from common import *
import state


#  골든타워 8층 : 60100030  
#  랄프:11003187 / 조디:11003169 / 코쿤:11003171 
#  오프닝 연출 
class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60100070], questStates=[2]):
            return monsterdel()
        if quest_user_detected(boxIds=[2002], questIds=[60100075], questStates=[1]):
            return fadeout()


class fadeout(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4020], returnView=False)
        destroy_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920])
        destroy_monster(spawnIds=[921,922,923,924,925,926,927,928,929])
        create_monster(spawnIds=[106], arg2=True)
        create_monster(spawnIds=[201,202], arg2=True)
        create_monster(spawnIds=[301,302,303,304,305,306], arg2=True)
        move_user(mapId=52000119, portalId=6001)
        set_scene_skip(state=fadeout_01, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return fadein()


class fadein(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=6000)
        face_emotion(spawnId=0, emotionName='Object_React_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_01()


#  랄프:11003187 / 조디:11003169 / 코쿤:11003171 
class scene_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4021], returnView=False)
        set_npc_emotion_sequence(spawnId=105, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003169, illustId='Jordy_normal', msg='$52000119_QD__MAIN3__0$', duration=3000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        set_npc_emotion_sequence(spawnId=104, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003187, msg='$52000119_QD__MAIN3__1$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4013,4014,4015], returnView=False)
        set_npc_emotion_sequence(spawnId=104, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003187, msg='$52000119_QD__MAIN3__2$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=104, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003187, msg='$52000119_QD__MAIN3__3$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return cheer_01()


#  응원 씬 
class cheer_01(state.State):
    def on_enter(self):
        set_sound(triggerId=7001, arg2=True)
        select_camera_path(pathIds=[4023,4024], returnView=False)
        add_cinematic_talk(npcId=11003354, msg='$52000119_QD__MAIN3__4$', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return cheer_02()


class cheer_02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=306, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003354, msg='$52000119_QD__MAIN3__5$', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return cheer_03()


class cheer_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4024,4025], returnView=False)
        add_cinematic_talk(npcId=11003354, msg='$52000119_QD__MAIN3__6$', duration=2000)
        add_cinematic_talk(npcId=11003354, msg='$52000119_QD__MAIN3__7$', duration=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return cheer_04()


class cheer_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003354, msg='$52000119_QD__MAIN3__8$', duration=2000)
        add_balloon_talk(spawnId=303, msg='$52000119_QD__MAIN3__9$', duration=2000, delayTick=1)
        add_cinematic_talk(npcId=11003354, msg='$52000119_QD__MAIN3__10$', duration=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_05()


#  응원 씬 종료 
class scene_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        set_npc_emotion_sequence(spawnId=106, sequenceName='Stun_A')
        add_cinematic_talk(npcId=11003171, msg='$52000119_QD__MAIN3__11$', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_06()


class scene_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4019], returnView=False)
        set_effect(triggerIds=[5002], visible=True)
        set_effect(triggerIds=[5003], visible=True)
        set_effect(triggerIds=[5004], visible=True)
        set_effect(triggerIds=[5005], visible=True)
        set_npc_emotion_sequence(spawnId=106, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003171, msg='$52000119_QD__MAIN3__12$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_07()


class scene_07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4019,4022], returnView=False)
        move_npc(spawnId=106, patrolName='MS2PatrolData_3001')
        set_conversation(type=2, spawnId=11003171, script='$52000119_QD__MAIN3__13$', arg4=3, arg5=0) # 코쿤
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return fadeout_01()


class fadeout_01(state.State):
    def on_enter(self):
        set_sound(triggerId=7001, arg2=False)
        set_sound(triggerId=7002, arg2=True)
        destroy_monster(spawnIds=[106]) # 106: 코쿤
        create_monster(spawnIds=[999], arg2=True) # 998: 강해진 코쿤
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=100)

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
        set_event_ui(type=1, arg2='$52000119_QD__MAIN3__14$', arg3='3000', arg4='0')
        add_balloon_talk(spawnId=999, msg='$52000119_QD__MAIN3__15$', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[999]):
            return fadeout_02()


class fadeout_02(state.State):
    def on_enter(self):
        set_sound(triggerId=7002, arg2=False)
        add_balloon_talk(spawnId=999, msg='$52000119_QD__MAIN3__19$', duration=2000, delayTick=0)
        add_balloon_talk(spawnId=306, msg='$52000119_QD__MAIN3__20$', duration=2000, delayTick=1)
        destroy_monster(spawnIds=[201,202])
        destroy_monster(spawnIds=[401,402,403,404,405,406,407])
        set_achievement(type='trigger', achieve='jordysave3')
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


#  진입 시 
class monsterdel(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920])
        destroy_monster(spawnIds=[921,922,923,924,925,926,927,928,929])
        create_monster(spawnIds=[401,402,403,404,405,406,407], arg2=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2002], questIds=[60100075], questStates=[1]):
            return ready()


