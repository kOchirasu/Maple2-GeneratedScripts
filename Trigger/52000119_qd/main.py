""" trigger/52000119_qd/main.xml """
from common import *
import state


#  골든타워 8층 : 60100030  
#  랄프:11003187 / 조디:11003169 / 코쿤:11003171 
#  오프닝 연출 
class intro(state.State):
    def on_enter(self):
        create_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920], arg2=True) # 기본 배치 몬스터
        create_monster(spawnIds=[921,922,923,924,925,926,927,928,929], arg2=True) # 기본 배치 몬스터
        create_monster(spawnIds=[104,105], arg2=True) # 104:랄프
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)
        set_effect(triggerIds=[5005], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60100030], questStates=[1]):
            return fadeout_01()


class fadeout_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        destroy_monster(spawnIds=[104,105]) # 104: 랄프
        create_monster(spawnIds=[101,102,103], arg2=True) # 101:랄프 / 102:조디 / 103: 브로커 랄프의 수하
        select_camera_path(pathIds=[4010,4001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return fadein_01()


class fadein_01(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=102, sequenceName='Sit_Down_A', duration=900000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return eventscene_01()


class eventscene_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003169, illustId='Jordy_normal', msg='$52000119_QD__MAIN__0$', duration=3000, align='Left')
        set_scene_skip(state=fadeout_02, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return eventscene_02()


class eventscene_02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        set_conversation(type=2, spawnId=11000173, script='$52000119_QD__MAIN__1$', arg4=3, arg5=0) # 브로커 랄프
        set_conversation(type=2, spawnId=11000173, script='$52000119_QD__MAIN__2$', arg4=3, arg5=3) # 브로커 랄프

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return eventscene_03()


class eventscene_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001,4003], returnView=False)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk')
        set_conversation(type=2, spawnId=11000173, script='$52000119_QD__MAIN__3$', arg4=3, arg5=0) # 브로커 랄프

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return eventscene_04()


class eventscene_04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=103, sequenceName='Damg_B')
        set_conversation(type=2, spawnId=11003171, script='$52000119_QD__MAIN__4$', arg4=3, arg5=0) # 코쿤

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return eventscene_05()


class eventscene_05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        set_conversation(type=2, spawnId=11000173, script='$52000119_QD__MAIN__5$', arg4=3, arg5=0) # 브로커 랄프
        set_conversation(type=2, spawnId=11000173, script='$52000119_QD__MAIN__6$', arg4=3, arg5=3) # 브로커 랄프

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return eventscene_06()


class eventscene_06(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=103, sequenceName='Bore_A')
        set_conversation(type=2, spawnId=11003171, script='$52000119_QD__MAIN__7$', arg4=3, arg5=0) # 코쿤
        set_conversation(type=2, spawnId=11003171, script='$52000119_QD__MAIN__8$', arg4=3, arg5=3) # 코쿤
        set_conversation(type=1, spawnId=102, script='$52000119_QD__MAIN__9$', arg4=2, arg5=4) # 코쿤
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return fadeout_02()


class fadeout_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return reset()


class reset(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return eventscene_end()


class eventscene_end(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=3)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52000119_QD__MAIN__10$', arg3='1000', arg4='0')
        set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return hintmsg()


class hintmsg(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        select_camera_path(pathIds=[4005], returnView=False)
        set_conversation(type=2, spawnId=0, script='$52000119_QD__MAIN__11$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return play()


class play(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2002]):
            return fadeout_03()


class fadeout_03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920])
        destroy_monster(spawnIds=[921,922,923,924,925,926,927,928,929])
        destroy_monster(spawnIds=[101,102,103]) # 101:랄프 / 102:조디 / 103: 브로커 랄프의 수하
        create_monster(spawnIds=[104,105,106], arg2=True) # 104:랄프 / 105:조디 / 106: 브로커 랄프의 수하
        move_user(mapId=52000119, portalId=6002)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return fadein_03()


class fadein_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user_path(patrolName='MS2PatrolData_3003')
        add_balloon_talk(spawnId=0, msg='$52000119_QD__MAIN__12$', duration=2000, delayTick=0)
        set_scene_skip(state=fadeout_04, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return bossscene_01()


#  랄프:11003187 / 조디:11003169 / 코쿤:11003171 
class bossscene_01(state.State):
    def on_enter(self):
        set_sound(triggerId=7001, arg2=True)
        set_npc_emotion_loop(spawnId=105, sequenceName='Sit_Down_A', duration=150000)
        set_conversation(type=2, spawnId=11003187, script='$52000119_QD__MAIN__13$', arg4=3, arg5=0) # 랄프

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return bossscene_02()


class bossscene_02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=104, sequenceName='Bore_A')
        set_conversation(type=2, spawnId=11003187, script='$52000119_QD__MAIN__14$', arg4=3, arg5=0) # 랄프

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return bossscene_03()


class bossscene_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4011], returnView=False)
        set_npc_emotion_sequence(spawnId=104, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11003187, script='$52000119_QD__MAIN__15$', arg4=3, arg5=0) # 랄프
        set_conversation(type=1, spawnId=105, script='$52000119_QD__MAIN__16$', arg4=3, arg5=1) # 랄프

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return bossscene_04()


class bossscene_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4013,4014,4015], returnView=False)
        set_npc_emotion_sequence(spawnId=104, sequenceName='Bore_A')
        set_conversation(type=2, spawnId=11003187, script='$52000119_QD__MAIN__17$', arg4=3, arg5=0) # 랄프

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return bossscene_05()


class bossscene_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4010], returnView=False)
        set_npc_emotion_sequence(spawnId=104, sequenceName='Talk_A')
        face_emotion(spawnId=0, emotionName='Object_React_A')
        set_conversation(type=2, spawnId=11003187, script='$52000119_QD__MAIN__18$', arg4=3, arg5=0) # 랄프

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return bossscene_06()


class bossscene_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4010], returnView=False)
        move_user_path(patrolName='MS2PatrolData_3004')
        set_npc_emotion_sequence(spawnId=106, sequenceName='Attack_01_C')
        move_npc(spawnId=106, patrolName='MS2PatrolData_3001')
        face_emotion(spawnId=0, emotionName='Object_React_A')
        set_conversation(type=2, spawnId=11003171, script='$52000119_QD__MAIN__19$', arg4=3, arg5=0) # 코쿤

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return bossscene_07()


class bossscene_07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        set_npc_emotion_sequence(spawnId=106, sequenceName='Bore_A')
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=4000)
        face_emotion(spawnId=0, emotionName='Object_React_A')
        set_conversation(type=2, spawnId=11003171, script='$52000119_QD__MAIN__20$', arg4=3, arg5=0) # 코쿤
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return fadeout_04()


class fadeout_04(state.State):
    def on_enter(self):
        set_sound(triggerId=7001, arg2=False)
        set_sound(triggerId=7002, arg2=True)
        destroy_monster(spawnIds=[106]) # 106: 코쿤
        create_monster(spawnIds=[997], arg2=True) # 999: 코쿤
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return fadein_04()


class fadein_04(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0.5)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        add_balloon_talk(spawnId=997, msg='$52000119_QD__MAIN__21$', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return bossmsg()


class bossmsg(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52000119_QD__MAIN__22$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[997]):
            return wait()


class wait(state.State):
    def on_enter(self):
        set_sound(triggerId=7002, arg2=False)
        add_balloon_talk(spawnId=104, msg='$52000119_QD__MAIN__23$', duration=2000, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return fadeout_05()


class fadeout_05(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[997]) # 106: 코쿤
        set_achievement(type='trigger', achieve='jordysave')
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


