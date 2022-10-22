""" trigger/52000037_qd/lookinto_striker_01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_actor(triggerId=4000, visible=False, initialSequence='Dead_A') # NelfActor
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10000175], state=0) # Bag

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[40002604], questStates=[3], jobCode=100):
            return StrikerSetting04()
        if quest_user_detected(boxIds=[9000], questIds=[40002604], questStates=[2], jobCode=100):
            return StrikerSetting03()
        if quest_user_detected(boxIds=[9000], questIds=[40002604], questStates=[1], jobCode=100):
            return StrikerSetting05()
        if quest_user_detected(boxIds=[9000], questIds=[60100065], questStates=[3], jobCode=100):
            return StrikerSetting02()
        if quest_user_detected(boxIds=[9000], questIds=[60100065], questStates=[2], jobCode=100):
            return StrikerSetting01()


#  스트라이커 연출 2차 입장
class StrikerSetting02(state.State):
    def on_enter(self):
        set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor
        create_monster(spawnIds=[202,302], arg2=False) # StrikerNPC
        create_monster(spawnIds=[101], arg2=False) # NelfDummyNPC

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9200]):
            return NextQuestStart01()


#  스트라이커 연출 2.5차 입장
class StrikerSetting05(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000175], state=1) # Bag
        set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor
        create_monster(spawnIds=[202,302], arg2=False) # StrikerNPC
        create_monster(spawnIds=[101], arg2=False) # NelfDummyNPC

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9200]):
            return NextQuestStart01()


#  스트라이커 연출 3차 입장
class StrikerSetting03(state.State):
    def on_enter(self):
        set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor
        create_monster(spawnIds=[101], arg2=False) # NelfDummyNPC
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


#  스트라이커 연출 상황 종료
class StrikerSetting04(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


#  스트라이커 연출 최초 입장
class StrikerSetting01(state.State):
    def on_enter(self):
        set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor
        create_monster(spawnIds=[201,301], arg2=False) # StrikerNPC

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9100]):
            return SayHi01()


class SayHi01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=201, script='$52000037_QD__LOOKINTO_STRIKER_01__0$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PCMove01()


class PCMove01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PCMove02()


class PCMove02(state.State):
    def on_enter(self):
        move_user(mapId=52000037, portalId=10, boxId=9900)
        create_monster(spawnIds=[401], arg2=False) # StrikerNPC

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Patrol01()


class Patrol01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=601, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Patrol02()


class Patrol02(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1000')
        set_conversation(type=1, spawnId=201, script='$52000037_QD__LOOKINTO_STRIKER_01__1$', arg4=3, arg5=0)
        move_npc(spawnId=401, patrolName='MS2PatrolData_401')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol03()


class Patrol03(state.State):
    def on_enter(self):
        move_npc(spawnId=301, patrolName='MS2PatrolData_301')
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Patrol04()


class Patrol04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=301, script='$52000037_QD__LOOKINTO_STRIKER_01__2$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ComeAcrossSB01()


class ComeAcrossSB01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=700, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ComeAcrossSB02()


class ComeAcrossSB02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=301, script='$52000037_QD__LOOKINTO_STRIKER_01__3$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ComeAcrossSB03()


class ComeAcrossSB03(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SBRunAway01()


class SBRunAway01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=401, script='$52000037_QD__LOOKINTO_STRIKER_01__14$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return SBRunAway02()


class SBRunAway02(state.State):
    def on_enter(self):
        move_npc(spawnId=401, patrolName='MS2PatrolData_402')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SBRunAway03()


class SBRunAway03(state.State):
    def on_enter(self):
        select_camera(triggerId=701, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Dialogue01()


class Dialogue01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001546, script='$52000037_QD__LOOKINTO_STRIKER_01__4$', arg4=5) # 자베스
        set_skip(state=Dialogue02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Dialogue02()


class Dialogue02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue03()


class Dialogue03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[401])
        set_conversation(type=2, spawnId=11001545, script='$52000037_QD__LOOKINTO_STRIKER_01__5$', arg4=5) # 브라보
        set_skip(state=Dialogue04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Dialogue04()


class Dialogue04(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=701, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return StepInside01()


class StepInside01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=301, script='$52000037_QD__LOOKINTO_STRIKER_01__6$', arg4=4, arg5=0)
        move_npc(spawnId=201, patrolName='MS2PatrolData_202')
        move_npc(spawnId=301, patrolName='MS2PatrolData_302')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return StepInside02()


class StepInside02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=201, script='$52000037_QD__LOOKINTO_STRIKER_01__7$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FirstQuestStart01()


class FirstQuestStart01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False) # NelfDummyNPC
        set_interact_object(triggerIds=[10000175], state=1) # Bag

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[60100065], questStates=[3], jobCode=100):
            return TalkJabethNBravo01()


class TalkJabethNBravo01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001546, script='$52000037_QD__LOOKINTO_STRIKER_01__8$', arg4=5) # 자베스
        set_skip(state=TalkJabethNBravo02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return TalkJabethNBravo02()


class TalkJabethNBravo02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return TalkJabethNBravo03()


class TalkJabethNBravo03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001545, script='$52000037_QD__LOOKINTO_STRIKER_01__9$', arg4=5) # 브라보
        set_skip(state=TalkJabethNBravo04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return TalkJabethNBravo04()


class TalkJabethNBravo04(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if true():
            return NPCChange01()


class NPCChange01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201,301])
        create_monster(spawnIds=[202,302], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return NextQuestStart01()


class NextQuestStart01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=202, script='$52000037_QD__LOOKINTO_STRIKER_01__10$', arg4=4, arg5=0)
        move_npc(spawnId=202, patrolName='MS2PatrolData_203')
        move_npc(spawnId=302, patrolName='MS2PatrolData_303')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return NextQuestStart02()


class NextQuestStart02(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[40002604], questStates=[2], jobCode=100):
            return ReadyToLeave01()


class ReadyToLeave01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001545, script='$52000037_QD__LOOKINTO_STRIKER_01__11$', arg4=6) # 브라보
        set_skip(state=ReadyToLeave02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return ReadyToLeave02()


class ReadyToLeave02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ReadyToLeave03()


class ReadyToLeave03(state.State):
    def on_enter(self):
        move_npc(spawnId=302, patrolName='MS2PatrolData_304')
        set_conversation(type=1, spawnId=302, script='$52000037_QD__LOOKINTO_STRIKER_01__12$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ReadyToLeave04()


class ReadyToLeave04(state.State):
    def on_enter(self):
        move_npc(spawnId=202, patrolName='MS2PatrolData_204')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ReadyToLeave05()


class ReadyToLeave05(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=202, script='$52000037_QD__LOOKINTO_STRIKER_01__13$', arg4=3, arg5=0)
        move_npc(spawnId=302, patrolName='MS2PatrolData_305')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return NPCLeave01()


class NPCLeave01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[302])
        move_npc(spawnId=202, patrolName='MS2PatrolData_205')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return NPCLeave02()


class NPCLeave02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        destroy_monster(spawnIds=[202])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    pass


