""" trigger/52000033_qd/audiencewithereb_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,201,301,401,501,502,503,504,505,506,507,508,509,510], arg2=False)
        set_effect(triggerIds=[5000], visible=False) # SpotLight_01
        set_effect(triggerIds=[5001], visible=False) # SpotLight_02
        set_effect(triggerIds=[5002], visible=False) # GuardBow

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return LodingDelay01()


class LodingDelay01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001301], questStates=[3]):
            return QuestOngoing02()
        if quest_user_detected(boxIds=[9000], questIds=[50001300], questStates=[3]):
            return QuestOngoing01()
        if quest_user_detected(boxIds=[9000], questIds=[50001300], questStates=[2]):
            return PCWalkIn01()
        if wait_tick(waitTick=3000):
            return PCtoLeave01()


#   첫 번째 퀘스트 완료 상태 
class QuestOngoing01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return SecondQuestCheck02()


#   두 번째 퀘스트 완료 상태 
class QuestOngoing02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCGoCenter01()


#   첫 번째 퀘스트 완료 가능 상태 
class PCWalkIn01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return PCWalkIn02()


class PCWalkIn02(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCWalkIn03()


class PCWalkIn03(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PCWalkIn04()


class PCWalkIn04(state.State):
    def on_enter(self):
        select_camera(triggerId=602, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return BowAction01()


class BowAction01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=501, sequenceName='Bow_A')
        set_npc_emotion_sequence(spawnId=502, sequenceName='Bow_A')
        set_npc_emotion_sequence(spawnId=503, sequenceName='Bow_A')
        set_npc_emotion_sequence(spawnId=504, sequenceName='Bow_A')
        set_npc_emotion_sequence(spawnId=505, sequenceName='Bow_A')
        set_npc_emotion_sequence(spawnId=506, sequenceName='Bow_A')
        set_npc_emotion_sequence(spawnId=507, sequenceName='Bow_A')
        set_npc_emotion_sequence(spawnId=508, sequenceName='Bow_A')
        set_npc_emotion_sequence(spawnId=509, sequenceName='Bow_A')
        set_npc_emotion_sequence(spawnId=510, sequenceName='Bow_A')
        set_effect(triggerIds=[5002], visible=True) # GuardBow

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BowAction02()


class BowAction02(state.State):
    def on_enter(self):
        select_camera(triggerId=701, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ErebTalk01()


class ErebTalk01(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1001')
        select_camera(triggerId=700, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ErebTalk02()


class ErebTalk02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52000033_QD__AUDIENCEWITHEREB_01__0$', arg4=4, arg5=0)
        set_skip(state=ErebTalk03)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ErebTalk03()


class ErebTalk03(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ErebTalk04()


class ErebTalk04(state.State):
    def on_enter(self):
        select_camera(triggerId=700, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SecondQuestCheck01()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class SecondQuestCheck01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[50001300], questStates=[3]):
            return SecondQuestCheck02()


class SecondQuestCheck02(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[50001301], questStates=[3]):
            return PCGoCenter01()


class PCGoCenter01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCGoCenter02()


class PCGoCenter02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCGoCenter03()


class PCGoCenter03(state.State):
    def on_enter(self):
        move_user(mapId=52000033, portalId=10, boxId=9900)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCGoCenter04()


class PCGoCenter04(state.State):
    def on_enter(self):
        select_camera(triggerId=800, enable=True)
        move_user_path(patrolName='MS2PatrolData_1002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCGoCenter05()


class PCGoCenter05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCSpotLighting01()


class PCSpotLighting01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # SpotLight_01
        set_effect(triggerIds=[5001], visible=True) # SpotLight_02

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCSpotLighting02()


class PCSpotLighting02(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Emotion_Happy_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PCSpotLighting03()


class PCSpotLighting03(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1003')
        select_camera(triggerId=801, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ErebTalk11()


class ErebTalk11(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000075, script='$52000033_QD__AUDIENCEWITHEREB_01__1$', arg4=5, arg5=0)
        set_skip(state=ErebTalk12)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ErebTalk12()


class ErebTalk12(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ErebTalk13()


class ErebTalk13(state.State):
    def on_enter(self):
        select_camera(triggerId=801, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCtoLeave01()

    def on_exit(self):
        set_effect(triggerIds=[5000], visible=False) # SpotLight_01
        set_effect(triggerIds=[5001], visible=False) # SpotLight_02


class PCtoLeave01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


