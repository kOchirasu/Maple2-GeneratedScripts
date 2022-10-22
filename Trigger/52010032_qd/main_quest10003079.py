""" trigger/52010032_qd/main_quest10003079.xml """
from common import *
import state


#  나메드가 페리온이야기하고 에바고르는 삐져서 나감 
class 무르파고스에들어오면(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003079], questStates=[1]):
            set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
            return Ready()


class Ready(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[202])
        destroy_monster(spawnIds=[301])
        destroy_monster(spawnIds=[302])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Ready01()


class Ready01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4004], returnView=False)
        face_emotion(spawnId=401, emotionName='Trigger_angry')
        create_monster(spawnIds=[401], arg2=True) # 나메드
        create_monster(spawnIds=[301], arg2=True) # 시끄러운 주먹
        create_monster(spawnIds=[302], arg2=True) # 에바고르
        move_npc(spawnId=301, patrolName='MS2PatrolData_3003')
        move_npc(spawnId=302, patrolName='MS2PatrolData_3004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 대화시작()


class 대화시작(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_1, arg2='nextState')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_npc_emotion_sequence(spawnId=401, sequenceName='Talk_A')
        move_user(mapId=52010032, portalId=6002)
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__0$', duration=3000)
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__1$', duration=4000)
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__2$', duration=4000)
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__3$', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return 대화시작01()


class 대화시작01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=401, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__4$', duration=4000)
        add_cinematic_talk(npcId=0, msg='$52010032_QD__MAIN_QUEST10003079__5$', duration=3500)
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__6$', duration=3500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return 대화시작02()


class 대화시작02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        set_pc_emotion_sequence(sequenceNames=['Emotion_Focus_A'])
        add_cinematic_talk(npcId=0, msg='$52010032_QD__MAIN_QUEST10003079__7$', duration=3500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 대화시작03()


class 대화시작03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        set_npc_emotion_sequence(spawnId=401, sequenceName='Bore_A')
        face_emotion(spawnId=203, emotionName='Trigger_Sad')
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__8$', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 에바고르삐짐()


class 에바고르삐짐(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005], returnView=False)
        add_cinematic_talk(npcId=11003391, msg='$52010032_QD__MAIN_QUEST10003079__9$', duration=4000)
        add_cinematic_talk(npcId=11003391, msg='$52010032_QD__MAIN_QUEST10003079__10$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 에바고르삐짐01()


class 에바고르삐짐01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        set_npc_emotion_sequence(spawnId=401, sequenceName='Bore_B')
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__11$', duration=3000)
        add_cinematic_talk(npcId=11003391, msg='$52010032_QD__MAIN_QUEST10003079__12$', duration=2000)
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__13$', duration=5000)
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__14$', duration=3500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=14000):
            return 에바고르삐짐02()


class 에바고르삐짐02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005], returnView=False)
        set_npc_emotion_sequence(spawnId=302, sequenceName='Attack_01_A')
        add_cinematic_talk(npcId=11003391, msg='$52010032_QD__MAIN_QUEST10003079__15$', duration=4000)
        add_cinematic_talk(npcId=11003391, msg='$52010032_QD__MAIN_QUEST10003079__16$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 에바고르퇴장()


class 에바고르퇴장(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4006], returnView=False)
        add_cinematic_talk(npcId=11003388, msg='$52010032_QD__MAIN_QUEST10003079__17$', duration=3000)
        move_npc(spawnId=302, patrolName='MS2PatrolData_3006')
        set_achievement(triggerId=2001, type='trigger', achieve='Namid')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 에바고르퇴장후()


class 에바고르퇴장후(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        set_npc_emotion_sequence(spawnId=401, sequenceName='Bore_B')
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__18$', duration=3500)
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN_QUEST10003079__19$', duration=3500)
        add_cinematic_talk(npcId=11003388, msg='$52010032_QD__MAIN_QUEST10003079__20$', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 에바고르퇴장후_1()


class 에바고르퇴장후_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 나메드에게퀘스트마무리()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        destroy_monster(spawnIds=[302])
        destroy_monster(spawnIds=[401])
        reset_camera(interpolationTime=0.5)
        set_achievement(triggerId=2001, type='trigger', achieve='Namid')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 나메드에게퀘스트마무리()


class 나메드에게퀘스트마무리(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        destroy_monster(spawnIds=[302])
        destroy_monster(spawnIds=[401])
        create_monster(spawnIds=[202], arg2=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return None # Missing State: 


