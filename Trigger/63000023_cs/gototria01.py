""" trigger/63000023_cs/gototria01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001001], state=0) # car
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5002], visible=False) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5200], visible=False) # 목표 바닥 지점 자동차 옆
        set_effect(triggerIds=[5300], visible=False) # 자동차 화살표
        set_effect(triggerIds=[5100], visible=False) # 경로 안내
        set_effect(triggerIds=[5101], visible=False) # 경로 안내
        set_effect(triggerIds=[5102], visible=False) # 경로 안내
        set_effect(triggerIds=[5103], visible=False) # 경로 안내
        set_effect(triggerIds=[5104], visible=False) # 경로 안내
        create_monster(spawnIds=[201,301,401,501,601], arg2=False)
        set_breakable(triggerIds=[4000], enabled=False)
        set_effect(triggerIds=[6000], visible=False) # CarIdle
        set_effect(triggerIds=[6001], visible=False) # CarMovingAway
        set_effect(triggerIds=[7000], visible=False) # Voice Bravo 00001460
        set_effect(triggerIds=[7001], visible=False) # Voice Bravo 00001461
        set_effect(triggerIds=[7002], visible=False) # Voice Bravo 00001462
        set_effect(triggerIds=[7003], visible=False) # Voice Bravo 00001463
        set_effect(triggerIds=[7100], visible=False) # Voice Jabeth 00001548
        set_effect(triggerIds=[7101], visible=False) # Voice Jabeth 00001549
        set_effect(triggerIds=[7102], visible=False) # Voice Jabeth 00001550
        set_effect(triggerIds=[7103], visible=False) # Voice Jabeth 00001551
        set_effect(triggerIds=[7200], visible=False) # Voice BravoNJabeth 00001598

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return LodingDelay01()


class LodingDelay01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        select_camera(triggerId=500, enable=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000440], questStates=[3]):
            return QuestOngoing01()
        if quest_user_detected(boxIds=[9900], questIds=[90000441], questStates=[1]):
            return QuestOngoing11()
        if wait_tick(waitTick=2000):
            return WalkWithJacey01()


#  첫번째  퀘스트 이미 완료한 상태 
class QuestOngoing01(state.State):
    def on_enter(self):
        select_camera(triggerId=500, enable=False)
        destroy_monster(spawnIds=[201,301])
        create_monster(spawnIds=[202,302], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return QuestOngoing02()


class QuestOngoing02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NextQuestStart01()


#  새로운  퀘스트 이미 수락한 상태 
class QuestOngoing11(state.State):
    def on_enter(self):
        select_camera(triggerId=500, enable=False)
        destroy_monster(spawnIds=[201,301])
        create_monster(spawnIds=[202,302], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return QuestOngoing12()


class QuestOngoing12(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return GetCloseToTheCar01()


#  최초 입장 
class WalkWithJacey01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return WalkWithJacey02()


class WalkWithJacey02(state.State):
    def on_enter(self):
        select_camera(triggerId=501, enable=True)
        move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return WalkWithJacey03()


class WalkWithJacey03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Dialogue01()


class Dialogue01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        set_effect(triggerIds=[7000], visible=True) # Voice Bravo 00001460
        set_conversation(type=2, spawnId=11001545, script='$63000023_CS__GOTOTRIA01__0$', arg4=6) # 브라보
        set_skip(state=Dialogue02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Dialogue02()


class Dialogue02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7000], visible=False) # Voice Bravo 00001460
        set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue03()


class Dialogue03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=301, sequenceName='Talk_A')
        set_effect(triggerIds=[7100], visible=True) # Voice Jabeth 00001548
        set_conversation(type=2, spawnId=11001546, script='$63000023_CS__GOTOTRIA01__1$', arg4=6) # 자베스
        set_skip(state=Dialogue04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Dialogue04()


class Dialogue04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7100], visible=False) # Voice Jabeth 00001548
        set_npc_emotion_sequence(spawnId=301, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue05()


class Dialogue05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        set_effect(triggerIds=[7001], visible=True) # Voice Bravo 00001461
        set_conversation(type=2, spawnId=11001545, script='$63000023_CS__GOTOTRIA01__2$', arg4=6) # 브라보
        set_skip(state=Dialogue06)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Dialogue06()


class Dialogue06(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7001], visible=False) # Voice Bravo 00001461
        set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue07()


class Dialogue07(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001545, script='$63000023_CS__GOTOTRIA01__3$', arg4=4) # 브라보
        set_skip(state=Dialogue08)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Dialogue08()


class Dialogue08(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue09()


class Dialogue09(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=301, sequenceName='Talk_A')
        set_effect(triggerIds=[7101], visible=True) # Voice Jabeth 00001549
        set_conversation(type=2, spawnId=11001546, script='$63000023_CS__GOTOTRIA01__4$', arg4=5) # 자베스
        set_skip(state=Dialogue10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Dialogue10()


class Dialogue10(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7101], visible=False) # Voice Jabeth 00001549
        set_npc_emotion_sequence(spawnId=301, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue11()


class Dialogue11(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        set_effect(triggerIds=[7002], visible=True) # Voice Bravo 00001462
        set_conversation(type=2, spawnId=11001545, script='$63000023_CS__GOTOTRIA01__5$', arg4=5) # 브라보
        set_skip(state=Dialogue12)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Dialogue12()


class Dialogue12(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7002], visible=False) # Voice Bravo 00001462
        set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue13()


class Dialogue13(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=301, sequenceName='Talk_A')
        set_effect(triggerIds=[7102], visible=True) # Voice Jabeth 00001550
        set_conversation(type=2, spawnId=11001546, script='$63000023_CS__GOTOTRIA01__6$', arg4=5) # 자베스
        set_skip(state=Dialogue14)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Dialogue14()


class Dialogue14(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7102], visible=False) # Voice Jabeth 00001550
        set_npc_emotion_sequence(spawnId=301, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue15()


class Dialogue15(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        set_effect(triggerIds=[7003], visible=True) # Voice Bravo 00001463
        set_conversation(type=2, spawnId=11001545, script='$63000023_CS__GOTOTRIA01__7$', arg4=5) # 브라보
        set_skip(state=Dialogue16)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Dialogue16()


class Dialogue16(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue17()


class Dialogue17(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001545, script='$63000023_CS__GOTOTRIA01__8$', arg4=4) # 브라보
        set_skip(state=Dialogue18)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Dialogue18()


class Dialogue18(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7003], visible=False) # Voice Bravo 00001463
        set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue19()


class Dialogue19(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=301, sequenceName='Talk_A')
        set_effect(triggerIds=[7103], visible=True) # Voice Jabeth 00001551
        set_conversation(type=2, spawnId=11001546, script='$63000023_CS__GOTOTRIA01__9$', arg4=5) # 자베스
        set_skip(state=Dialogue20)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Dialogue20()


class Dialogue20(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=301, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue21()


class Dialogue21(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=301, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001546, script='$63000023_CS__GOTOTRIA01__10$', arg4=4) # 자베스
        set_skip(state=Dialogue22)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Dialogue22()


class Dialogue22(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7103], visible=False) # Voice Jabeth 00001551
        set_npc_emotion_sequence(spawnId=301, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=601, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return AttackIdle01()


class AttackIdle01(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        move_npc(spawnId=301, patrolName='MS2PatrolData_301')
        set_effect(triggerIds=[7200], visible=True) # Voice BravoNJabeth 00001598
        set_conversation(type=1, spawnId=201, script='$63000023_CS__GOTOTRIA01__11$', arg4=3, arg5=0) # 둘이 함께  Voice 00001598
        set_conversation(type=1, spawnId=301, script='$63000023_CS__GOTOTRIA01__12$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return TalkJacey01()


class TalkJacey01(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')
        move_user_path(patrolName='MS2PatrolData_1001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TalkJacey02()


class TalkJacey02(state.State):
    def on_enter(self):
        select_camera(triggerId=700, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TalkJacey03()


class TalkJacey03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7200], visible=False) # Voice BravoNJabeth 00001598
        move_npc(spawnId=101, patrolName='MS2PatrolData_102')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return JaceyTalk04()


class JaceyTalk04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001620, script='$63000023_CS__GOTOTRIA01__13$', arg4=5) # 제이시
        set_skip(state=JaceyTalk05)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return JaceyTalk05()


class JaceyTalk05(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return JaceyLeave01()


class JaceyLeave01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return JaceyLeave02()


class JaceyLeave02(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_103')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return JaceyLeave03()


class JaceyLeave03(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1002')
        select_camera_path(pathIds=[701,702], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return JaceyLeave04()


class JaceyLeave04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$63000023_CS__GOTOTRIA01__14$', arg4=4, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return JaceyLeave05()


class JaceyLeave05(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201,301])
        create_monster(spawnIds=[202,302], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return JaceyLeave06()


class JaceyLeave06(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=702, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return QuestComplete01()


class QuestComplete01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        show_guide_summary(entityId=10028010, textId=10028010) # 가이드 : 브라보와 대화하기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000440], questStates=[3]):
            return NextQuestStart01()

    def on_exit(self):
        hide_guide_summary(entityId=10028010)


class NextQuestStart01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10028020, textId=10028020) # 가이드 : 브라보와 대화하기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000441], questStates=[1]):
            return GetCloseToTheCar01()

    def on_exit(self):
        hide_guide_summary(entityId=10028020)


class GetCloseToTheCar01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True) # CarIdle
        show_guide_summary(entityId=10028030, textId=10028030) # 가이드 : 트라이아행 차에 가까이 가기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=True) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5200], visible=True) # 목표 바닥 지점 자동차 옆
        set_effect(triggerIds=[5100], visible=True) # 경로 안내
        set_effect(triggerIds=[5101], visible=True) # 경로 안내
        set_effect(triggerIds=[5102], visible=True) # 경로 안내
        set_effect(triggerIds=[5103], visible=True) # 경로 안내
        set_effect(triggerIds=[5104], visible=True) # 경로 안내

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return GetCloseToTheCar02()

    def on_exit(self):
        hide_guide_summary(entityId=10028030)


class GetCloseToTheCar02(state.State):
    def on_enter(self):
        move_npc(spawnId=202, patrolName='MS2PatrolData_202')
        move_npc(spawnId=302, patrolName='MS2PatrolData_302')
        show_guide_summary(entityId=10028040, textId=10028040) # 가이드 : 차에 탑승해 트라이아로 이동하기
        set_interact_object(triggerIds=[10001001], state=1) # car
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5300], visible=True) # 자동차 화살표

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001001], arg2=0):
            return GetInTheCar01()


class GetInTheCar01(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4000], enabled=True)
        hide_guide_summary(entityId=10028040)
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5002], visible=False) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5200], visible=False) # 목표 바닥 지점 자동차 옆
        set_effect(triggerIds=[5100], visible=False) # 경로 안내
        set_effect(triggerIds=[5101], visible=False) # 경로 안내
        set_effect(triggerIds=[5102], visible=False) # 경로 안내
        set_effect(triggerIds=[5103], visible=False) # 경로 안내
        set_effect(triggerIds=[5104], visible=False) # 경로 안내
        set_effect(triggerIds=[5300], visible=False) # 자동차 화살표
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return GetInTheCar02()


class GetInTheCar02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=False) # CarIdle
        set_effect(triggerIds=[6001], visible=True) # CarMovingAway
        move_user(mapId=63000023, portalId=2, boxId=9900)
        select_camera(triggerId=800, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return GetInTheCar03()


class GetInTheCar03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CarMoving01()


class CarMoving01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return CarMoving02()


class CarMoving02(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4000], enabled=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        select_camera(triggerId=800, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CarMoving03()


class CarMoving03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001], visible=False) # CarMovingAway
        move_user(mapId=2000062, portalId=13, boxId=9900)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


