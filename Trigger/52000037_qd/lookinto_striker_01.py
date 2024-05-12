""" trigger/52000037_qd/lookinto_striker_01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=4000, visible=False, initialSequence='Dead_A') # NelfActor
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[10000175], state=0) # Bag

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[40002604], questStates=[3], jobCode=100):
            # 스트라이커 넬프의 죽음 퀘스트 완료
            return StrikerSetting04(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[40002604], questStates=[2], jobCode=100):
            # 스트라이커 넬프의 죽음 퀘스트 완료 가능
            return StrikerSetting03(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[40002604], questStates=[1], jobCode=100):
            # 스트라이커 넬프의 죽음 퀘스트 진행중
            return StrikerSetting05(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[60100065], questStates=[3], jobCode=100):
            # 스트라이커 랄프의 정보 퀘스트 완료
            return StrikerSetting02(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[60100065], questStates=[2], jobCode=100):
            # 스트라이커 랄프의 정보 퀘스트 완료 가능
            return StrikerSetting01(self.ctx)


# 스트라이커 연출 2차 입장
class StrikerSetting02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor
        self.create_monster(spawnIds=[202,302], animationEffect=False) # StrikerNPC
        self.create_monster(spawnIds=[101], animationEffect=False) # NelfDummyNPC

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9200]):
            # QuestZone
            return NextQuestStart01(self.ctx)


# 스트라이커 연출 2.5차 입장
class StrikerSetting05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000175], state=1) # Bag
        self.set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor
        self.create_monster(spawnIds=[202,302], animationEffect=False) # StrikerNPC
        self.create_monster(spawnIds=[101], animationEffect=False) # NelfDummyNPC

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9200]):
            # QuestZone
            return NextQuestStart01(self.ctx)


# 스트라이커 연출 3차 입장
class StrikerSetting03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor
        self.create_monster(spawnIds=[101], animationEffect=False) # NelfDummyNPC
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


# 스트라이커 연출 상황 종료
class StrikerSetting04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


# 스트라이커 연출 최초 입장
class StrikerSetting01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor
        self.create_monster(spawnIds=[201,301], animationEffect=False) # StrikerNPC

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9100]):
            # Mid
            return SayHi01(self.ctx)


class SayHi01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=201, script='$52000037_QD__LOOKINTO_STRIKER_01__0$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PCMove01(self.ctx)


class PCMove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(triggerId=600, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return PCMove02(self.ctx)


class PCMove02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52000037, portalId=10, boxId=9900)
        self.create_monster(spawnIds=[401], animationEffect=False) # StrikerNPC

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Patrol01(self.ctx)


class Patrol01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=601, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Patrol02(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_1000')
        self.set_conversation(type=1, spawnId=201, script='$52000037_QD__LOOKINTO_STRIKER_01__1$', arg4=3, arg5=0)
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_401')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_301')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Patrol04(self.ctx)


class Patrol04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=301, script='$52000037_QD__LOOKINTO_STRIKER_01__2$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return ComeAcrossSB01(self.ctx)


class ComeAcrossSB01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=700, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ComeAcrossSB02(self.ctx)


class ComeAcrossSB02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=301, script='$52000037_QD__LOOKINTO_STRIKER_01__3$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ComeAcrossSB03(self.ctx)


class ComeAcrossSB03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SBRunAway01(self.ctx)


class SBRunAway01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=401, script='$52000037_QD__LOOKINTO_STRIKER_01__14$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return SBRunAway02(self.ctx)


class SBRunAway02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_402')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SBRunAway03(self.ctx)


class SBRunAway03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=701, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Dialogue01(self.ctx)


class Dialogue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001546, script='$52000037_QD__LOOKINTO_STRIKER_01__4$', arg4=5) # 자베스
        self.set_skip(state=Dialogue02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Dialogue02(self.ctx)


class Dialogue02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Dialogue03(self.ctx)


class Dialogue03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[401])
        self.set_conversation(type=2, spawnId=11001545, script='$52000037_QD__LOOKINTO_STRIKER_01__5$', arg4=5) # 브라보
        self.set_skip(state=Dialogue04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Dialogue04(self.ctx)


class Dialogue04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=701, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return StepInside01(self.ctx)


class StepInside01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=301, script='$52000037_QD__LOOKINTO_STRIKER_01__6$', arg4=4, arg5=0)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_202')
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_302')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return StepInside02(self.ctx)


class StepInside02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=201, script='$52000037_QD__LOOKINTO_STRIKER_01__7$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return FirstQuestStart01(self.ctx)


class FirstQuestStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101], animationEffect=False) # NelfDummyNPC
        self.set_interact_object(triggerIds=[10000175], state=1) # Bag

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[60100065], questStates=[3], jobCode=100):
            # 스트라이커  랄프의 정보 퀘스트 완료 상태
            return TalkJabethNBravo01(self.ctx)


class TalkJabethNBravo01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001546, script='$52000037_QD__LOOKINTO_STRIKER_01__8$', arg4=5) # 자베스
        self.set_skip(state=TalkJabethNBravo02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return TalkJabethNBravo02(self.ctx)


class TalkJabethNBravo02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return TalkJabethNBravo03(self.ctx)


class TalkJabethNBravo03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001545, script='$52000037_QD__LOOKINTO_STRIKER_01__9$', arg4=5) # 브라보
        self.set_skip(state=TalkJabethNBravo04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return TalkJabethNBravo04(self.ctx)


class TalkJabethNBravo04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NPCChange01(self.ctx)


class NPCChange01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[201,301])
        self.create_monster(spawnIds=[202,302], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return NextQuestStart01(self.ctx)


class NextQuestStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=202, script='$52000037_QD__LOOKINTO_STRIKER_01__10$', arg4=4, arg5=0)
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_203')
        self.move_npc(spawnId=302, patrolName='MS2PatrolData_303')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return NextQuestStart02(self.ctx)


class NextQuestStart02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[40002604], questStates=[2], jobCode=100):
            # 스트라이커  넬프의 죽음 퀘스트 완료 상태
            return ReadyToLeave01(self.ctx)


class ReadyToLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001545, script='$52000037_QD__LOOKINTO_STRIKER_01__11$', arg4=6) # 브라보
        self.set_skip(state=ReadyToLeave02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return ReadyToLeave02(self.ctx)


class ReadyToLeave02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ReadyToLeave03(self.ctx)


class ReadyToLeave03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=302, patrolName='MS2PatrolData_304')
        self.set_conversation(type=1, spawnId=302, script='$52000037_QD__LOOKINTO_STRIKER_01__12$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ReadyToLeave04(self.ctx)


class ReadyToLeave04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_204')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ReadyToLeave05(self.ctx)


class ReadyToLeave05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=202, script='$52000037_QD__LOOKINTO_STRIKER_01__13$', arg4=3, arg5=0)
        self.move_npc(spawnId=302, patrolName='MS2PatrolData_305')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return NPCLeave01(self.ctx)


class NPCLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[302])
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_205')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return NPCLeave02(self.ctx)


class NPCLeave02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.destroy_monster(spawnIds=[202])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
