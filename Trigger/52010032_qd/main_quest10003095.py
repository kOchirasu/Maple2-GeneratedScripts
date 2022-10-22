""" trigger/52010032_qd/main_quest10003095.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False) # 나메드 치유 시전 이펙트
        set_effect(triggerIds=[5002], visible=False) # 붉은 늑대의 심장 치유 이펙트

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003095], questStates=[1]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_scene_skip(state=Skip_1, arg2='nextState')
        select_camera_path(pathIds=[4001], returnView=False)
        move_user(mapId=52010032, portalId=7001)
        create_monster(spawnIds=[101], arg2=True) # 붉은늑대의심장:
        set_npc_emotion_loop(spawnId=101, sequenceName='Dead_Idle_A', duration=100000000)
        face_emotion(spawnId=101, emotionName='Trigger_Dead')
        destroy_monster(spawnIds=[202])
        create_monster(spawnIds=[201], arg2=True) # 나메드:

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 치유의식_01()


class 치유의식_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003095__0$', duration=4000)
        add_balloon_talk(spawnId=0, msg='$52010032_QD__MAIN_QUEST10003095__1$', duration=2000, delayTick=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 치유의식_02()


class 치유의식_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002,4003], returnView=False)
        move_user_path(patrolName='MS2PatrolData_3002')
        set_npc_emotion_sequence(spawnId=401, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003095__2$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 치유의식_03()


class 치유의식_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_B')
        set_effect(triggerIds=[5001], visible=True)
        set_pc_emotion_loop(sequenceName='Emotion_Dance_Event01', duration=7000)
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003095__3$', duration=5000)
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003095__4$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 치유의식_04()


class 치유의식_04(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 치유의식_04_1()


class 치유의식_04_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_loop(spawnId=101, sequenceName='Down_Idle_A', duration=100000000)
        add_cinematic_talk(npcId=11003406, msg='$52010032_QD__MAIN_QUEST10003095__5$', duration=4000)
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003095__6$', duration=3000)
        add_cinematic_talk(npcId=11003406, msg='$52010032_QD__MAIN_QUEST10003095__7$', duration=3000)
        add_balloon_talk(spawnId=0, msg='$52010032_QD__MAIN_QUEST10003095__8$', duration=2000, delayTick=6000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return 치유의식_05()


class 치유의식_05(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 치유의식_05_1()


class 치유의식_05_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[4003,4001], returnView=False)
        set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_B')
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_npc_emotion_loop(spawnId=101, sequenceName='Dead_Idle_A', duration=100000000)
        face_emotion(spawnId=101, emotionName='Trigger_Dead')
        set_pc_emotion_sequence(sequenceNames=['Talk_A'])
        add_cinematic_talk(npcId=0, msg='$52010032_QD__MAIN_QUEST10003095__9$', duration=3000)
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003095__10$', duration=4000)
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003095__11$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 의식종료_01()


class 의식종료_01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_A')
        move_user_path(patrolName='MS2PatrolData_3007')
        add_cinematic_talk(npcId=0, msg='$52010032_QD__MAIN_QUEST10003095__12$', duration=3000)
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003095__13$', duration=3000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 의식종료_02()


class 의식종료_02(state.State):
    def on_enter(self):
        set_achievement(triggerId=2001, type='trigger', achieve='Namid2')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_achievement(triggerId=2001, type='trigger', achieve='Namid2')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        create_monster(spawnIds=[202], arg2=True) # 나메드:
        destroy_monster(spawnIds=[201])
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[101])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return None # Missing State: 


