""" trigger/52000033_qd/audiencewithereb_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101,201,301,401,501,502,503,504,505,506,507,508,509,510], animationEffect=False)
        self.set_effect(triggerIds=[5000], visible=False) # SpotLight_01
        self.set_effect(triggerIds=[5001], visible=False) # SpotLight_02
        self.set_effect(triggerIds=[5002], visible=False) # GuardBow

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return LodingDelay01(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001301], questStates=[3]):
            # 두 번째 퀘스트 완료 상태
            return QuestOngoing02(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001300], questStates=[3]):
            # 첫 번째 퀘스트 완료 상태
            return QuestOngoing01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001300], questStates=[2]):
            # 첫 번째 퀘스트 완료 가능 상태
            return PCWalkIn01(self.ctx)
        if self.wait_tick(waitTick=3000):
            return PCtoLeave01(self.ctx)


# 첫 번째 퀘스트 완료 상태
class QuestOngoing01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return SecondQuestCheck02(self.ctx)


# 두 번째 퀘스트 완료 상태
class QuestOngoing02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PCGoCenter01(self.ctx)


# 첫 번째 퀘스트 완료 가능 상태
class PCWalkIn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=600, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return PCWalkIn02(self.ctx)


class PCWalkIn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=601, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PCWalkIn03(self.ctx)


class PCWalkIn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PCWalkIn04(self.ctx)


class PCWalkIn04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=602, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return BowAction01(self.ctx)


class BowAction01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=501, sequenceName='Bow_A')
        self.set_npc_emotion_sequence(spawnId=502, sequenceName='Bow_A')
        self.set_npc_emotion_sequence(spawnId=503, sequenceName='Bow_A')
        self.set_npc_emotion_sequence(spawnId=504, sequenceName='Bow_A')
        self.set_npc_emotion_sequence(spawnId=505, sequenceName='Bow_A')
        self.set_npc_emotion_sequence(spawnId=506, sequenceName='Bow_A')
        self.set_npc_emotion_sequence(spawnId=507, sequenceName='Bow_A')
        self.set_npc_emotion_sequence(spawnId=508, sequenceName='Bow_A')
        self.set_npc_emotion_sequence(spawnId=509, sequenceName='Bow_A')
        self.set_npc_emotion_sequence(spawnId=510, sequenceName='Bow_A')
        self.set_effect(triggerIds=[5002], visible=True) # GuardBow

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return BowAction02(self.ctx)


class BowAction02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=701, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ErebTalk01(self.ctx)


class ErebTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_1001')
        self.select_camera(triggerId=700, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return ErebTalk02(self.ctx)


class ErebTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000075, script='$52000033_QD__AUDIENCEWITHEREB_01__0$', arg4=4, arg5=0)
        self.set_skip(state=ErebTalk03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return ErebTalk03(self.ctx)


class ErebTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ErebTalk04(self.ctx)


class ErebTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=700, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SecondQuestCheck01(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class SecondQuestCheck01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[50001300], questStates=[3]):
            # 첫 번째 퀘스트 완료 상태
            return SecondQuestCheck02(self.ctx)


class SecondQuestCheck02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[50001301], questStates=[3]):
            # 두 번째 퀘스트 완료 상태
            return PCGoCenter01(self.ctx)


class PCGoCenter01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCGoCenter02(self.ctx)


class PCGoCenter02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PCGoCenter03(self.ctx)


class PCGoCenter03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52000033, portalId=10, boxId=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PCGoCenter04(self.ctx)


class PCGoCenter04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=800, enable=True)
        self.move_user_path(patrolName='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PCGoCenter05(self.ctx)


class PCGoCenter05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PCSpotLighting01(self.ctx)


class PCSpotLighting01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=True) # SpotLight_01
        self.set_effect(triggerIds=[5001], visible=True) # SpotLight_02

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PCSpotLighting02(self.ctx)


class PCSpotLighting02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Happy_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PCSpotLighting03(self.ctx)


class PCSpotLighting03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_1003')
        self.select_camera(triggerId=801, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ErebTalk11(self.ctx)


class ErebTalk11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000075, script='$52000033_QD__AUDIENCEWITHEREB_01__1$', arg4=5, arg5=0)
        self.set_skip(state=ErebTalk12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ErebTalk12(self.ctx)


class ErebTalk12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ErebTalk13(self.ctx)


class ErebTalk13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=801, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCtoLeave01(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(triggerIds=[5000], visible=False)
        # SpotLight_01
        self.set_effect(triggerIds=[5001], visible=False)
        # SpotLight_02


class PCtoLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 대기
