""" trigger/63000021_cs/wakup01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0) # monitor off
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0) # monitor on
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5002], visible=False) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5200], visible=False) # 경로 안내
        set_effect(triggerIds=[5201], visible=False) # 경로 안내
        set_effect(triggerIds=[5202], visible=False) # 경로 안내
        set_effect(triggerIds=[5203], visible=False) # 경로 안내
        set_effect(triggerIds=[5204], visible=False) # 경로 안내
        set_effect(triggerIds=[5205], visible=False) # 경로 안내
        set_effect(triggerIds=[5206], visible=False) # 경로 안내
        set_effect(triggerIds=[5207], visible=False) # 경로 안내
        set_effect(triggerIds=[5208], visible=False) # 경로 안내
        set_effect(triggerIds=[5209], visible=False) # 경로 안내
        set_effect(triggerIds=[5210], visible=False) # 경로 안내
        set_effect(triggerIds=[5211], visible=False) # 경로 안내
        set_effect(triggerIds=[5212], visible=False) # 경로 안내
        set_effect(triggerIds=[5213], visible=False) # 경로 안내
        set_effect(triggerIds=[5214], visible=False) # 경로 안내
        set_effect(triggerIds=[5215], visible=False) # 경로 안내
        set_effect(triggerIds=[5216], visible=False) # 경로 안내
        set_effect(triggerIds=[5217], visible=False) # 경로 안내
        set_effect(triggerIds=[7000], visible=False) # Voice Jabeth 00001545
        set_effect(triggerIds=[7001], visible=False) # Voice Jabeth 00001546
        set_effect(triggerIds=[7002], visible=False) # Voice Jabeth 00001547
        set_effect(triggerIds=[7003], visible=False) # Voice Jabeth 00001596 monologue
        set_effect(triggerIds=[7004], visible=False) # Voice Jabeth 00001597 monologue
        set_effect(triggerIds=[7100], visible=False) # Voice Bravo 00001457
        set_effect(triggerIds=[7101], visible=False) # Voice Bravo 00001458
        set_effect(triggerIds=[7102], visible=False) # Voice Bravo 00001459
        set_effect(triggerIds=[7103], visible=False) # Voice Bravo 00001525 monologue
        set_effect(triggerIds=[7104], visible=False) # Voice Bravo 00001526 monologue
        set_effect(triggerIds=[6000], visible=False) # RadioInterference

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
        if wait_tick(waitTick=2000):
            return LodingDelay02()


class LodingDelay02(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Down_Idle_D', duration=6600)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000439], questStates=[1]):
            return QuestOngoing01()
        if wait_tick(waitTick=2000):
            return WakeUp01()


#  이미 퀘스트 수락한 상태 
class QuestOngoing01(state.State):
    def on_enter(self):
        select_camera(triggerId=500, enable=False)
        create_monster(spawnIds=[103], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return QuestOngoing02()


class QuestOngoing02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=63000021, portalId=10, boxId=9002)
        set_pc_emotion_loop(sequenceName='Idle_A', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CallNextRoom01()


#  최초 입장 
class WakeUp01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return WakeUp02()


class WakeUp02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return WakeUp03()


class WakeUp03(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=60000)
        create_monster(spawnIds=[101,201,301], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return WakeUp04()


class WakeUp04(state.State):
    def on_enter(self):
        select_camera(triggerId=599, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return WakeUp05()


class WakeUp05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Dialogue01()


class Dialogue01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=301, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001546, script='$63000021_CS__WAKUP01__0$', arg4=4) # 자베스
        set_effect(triggerIds=[7000], visible=True) # Voice Jabeth 00001545
        set_skip(state=Dialogue02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Dialogue02()


class Dialogue02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=301, sequenceName='Idle_A')
        set_effect(triggerIds=[7000], visible=False) # Voice Jabeth 00001545
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Dialogue03()


class Dialogue03(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_200')
        set_conversation(type=2, spawnId=11001545, script='$63000021_CS__WAKUP01__1$', arg4=4) # 브라보
        set_effect(triggerIds=[7100], visible=True) # Voice Bravo 00001457

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Dialogue04()


class Dialogue04(state.State):
    def on_enter(self):
        move_npc(spawnId=301, patrolName='MS2PatrolData_300')
        set_skip(state=Dialogue05)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Dialogue05()


class Dialogue05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7100], visible=False) # Voice Bravo 00001457
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Dialogue06()


class Dialogue06(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001546, script='$63000021_CS__WAKUP01__2$', arg4=4) # 자베스
        set_effect(triggerIds=[7001], visible=True) # Voice Jabeth 00001546
        set_skip(state=Dialogue07)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Dialogue07()


class Dialogue07(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7001], visible=False) # Voice Jabeth 00001546
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return JaceyWalkIn01()


class JaceyWalkIn01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=601, enable=True)
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return JaceyWalkIn02()


class JaceyWalkIn02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Trialogue01()


class Trialogue01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001620, script='$63000021_CS__WAKUP01__3$', arg4=4) # 제이시
        set_skip(state=Trialogue02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Trialogue02()


class Trialogue02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        select_camera(triggerId=602, enable=True)
        move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        move_npc(spawnId=301, patrolName='MS2PatrolData_301')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Trialogue03()


class Trialogue03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001545, script='$63000021_CS__WAKUP01__4$', arg4=4) # 브라보
        set_effect(triggerIds=[7101], visible=True) # Voice Bravo 00001458
        set_skip(state=Trialogue04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Trialogue04()


class Trialogue04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7101], visible=False) # Voice Bravo 00001458
        set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Trialogue05()


class Trialogue05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=301, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001546, script='$63000021_CS__WAKUP01__5$', arg4=4) # 자베스
        set_effect(triggerIds=[7002], visible=True) # Voice Jabeth 00001547
        set_skip(state=Trialogue06)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Trialogue06()


class Trialogue06(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7002], visible=False) # Voice Jabeth 00001547
        set_npc_emotion_sequence(spawnId=301, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Trialogue07()


class Trialogue07(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001545, script='$63000021_CS__WAKUP01__6$', arg4=4) # 브라보
        set_effect(triggerIds=[7102], visible=True) # Voice Bravo 00001459
        set_skip(state=Trialogue08)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Trialogue08()


class Trialogue08(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7102], visible=False) # Voice Bravo 00001459
        set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return Trialogue09()


class Trialogue09(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001620, script='$63000021_CS__WAKUP01__7$', arg4=4) # 제이시
        set_skip(state=Trialogue10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Trialogue10()


class Trialogue10(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return TwoMenWalkOut01()


class TwoMenWalkOut01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=700, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return TwoMenWalkOut02()


class TwoMenWalkOut02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=201, script='$63000021_CS__WAKUP01__8$', arg4=3, arg5=0) # Voice 00001525
        set_effect(triggerIds=[7103], visible=True) # Voice Bravo 00001525 monologue

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TwoMenWalkOut03()


class TwoMenWalkOut03(state.State):
    def on_enter(self):
        move_npc(spawnId=201, patrolName='MS2PatrolData_202')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TwoMenWalkOut04()


class TwoMenWalkOut04(state.State):
    def on_enter(self):
        move_npc(spawnId=301, patrolName='MS2PatrolData_302')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TwoMenWalkOut05()


class TwoMenWalkOut05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7103], visible=False) # Voice Bravo 00001525 monologue
        set_effect(triggerIds=[7003], visible=True) # Voice Jabeth 00001596 monologue
        set_conversation(type=1, spawnId=301, script='$63000021_CS__WAKUP01__9$', arg4=3, arg5=0) # Voice 00001596

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TwoMenWalkOut06()


class TwoMenWalkOut06(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7003], visible=False) # Voice Jabeth 00001596 monologue
        select_camera_path(pathIds=[701,702], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_102')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return TwoMenWalkOut07()


class TwoMenWalkOut07(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7104], visible=True) # Voice Bravo 00001526 monologue
        set_conversation(type=1, spawnId=201, script='$63000021_CS__WAKUP01__10$', arg4=4, arg5=0) # Voice 00001526

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return TwoMenWalkOut08()


class TwoMenWalkOut08(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7104], visible=False) # Voice Bravo 00001526 monologue
        set_effect(triggerIds=[7004], visible=True) # Voice Jabeth 00001597 monologue
        set_conversation(type=1, spawnId=301, script='$63000021_CS__WAKUP01__11$', arg4=4, arg5=0) # Voice 00001597

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return StandUp01()


class StandUp01(state.State):
    def on_enter(self):
        move_user(mapId=63000021, portalId=10, boxId=9900)
        set_pc_emotion_loop(sequenceName='Idle_A', duration=2000)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=703, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return JaceyTalk01()


class JaceyTalk01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7004], visible=False) # Voice Jabeth 00001597 monologue

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return JaceyTalk02()


class JaceyTalk02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001620, script='$63000021_CS__WAKUP01__12$', arg4=3) # 제이시
        set_skip(state=JaceyTalk03)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return JaceyTalk03()


class JaceyTalk03(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return JaceyTalk04()


class JaceyTalk04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001620, script='$63000021_CS__WAKUP01__13$', arg4=5) # 제이시
        set_skip(state=JaceyTalk05)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return JaceyTalk05()


class JaceyTalk05(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201,301])
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=703, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return JaceyQuest01()


class JaceyQuest01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10021030, textId=10021030) # 가이드 : 제이시와 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000439], questStates=[1]):
            return JaceyQuest02()


class JaceyQuest02(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10021030)
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[103], arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CallNextRoom01()


class CallNextRoom01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=103, patrolName='MS2PatrolData_103')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CallNextRoom02()


class CallNextRoom02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000], visible=False, arg3=100, arg4=0, arg5=0) # MonitorOff
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0) # MonitorOn
        set_effect(triggerIds=[6000], visible=True) # RadioInterference

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CallNextRoom03()


class CallNextRoom03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True) # RadioInterference
        set_conversation(type=2, spawnId=11001620, script='$63000021_CS__WAKUP01__14$', arg4=4) # 제이시
        set_skip(state=CallNextRoom04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return CallNextRoom04()


class CallNextRoom04(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CallNextRoom05()


class CallNextRoom05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True) # RadioInterference
        set_conversation(type=2, spawnId=11001620, script='$63000021_CS__WAKUP01__15$', arg4=3) # 제이시
        set_skip(state=CallNextRoom06)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CallNextRoom06()


class CallNextRoom06(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return SayGoodBye01()


class SayGoodBye01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=103, patrolName='MS2PatrolData_104')
        set_effect(triggerIds=[6000], visible=False) # RadioInterference

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return SayGoodBye02()


class SayGoodBye02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001620, script='$63000021_CS__WAKUP01__16$', arg4=5) # 제이시
        set_skip(state=SayGoodBye03)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return SayGoodBye03()


class SayGoodBye03(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        destroy_monster(spawnIds=[103])
        create_monster(spawnIds=[104], arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if true():
            return GuideNextMap01()


class GuideNextMap01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10026010, textId=10026010) # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        set_effect(triggerIds=[5001], visible=True) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5200], visible=True) # 경로 안내
        set_effect(triggerIds=[5201], visible=True) # 경로 안내
        set_effect(triggerIds=[5202], visible=True) # 경로 안내
        set_effect(triggerIds=[5203], visible=True) # 경로 안내
        set_effect(triggerIds=[5204], visible=True) # 경로 안내
        set_effect(triggerIds=[5205], visible=True) # 경로 안내
        set_effect(triggerIds=[5206], visible=True) # 경로 안내
        set_effect(triggerIds=[5207], visible=True) # 경로 안내
        set_effect(triggerIds=[5208], visible=True) # 경로 안내
        set_effect(triggerIds=[5209], visible=True) # 경로 안내
        set_effect(triggerIds=[5210], visible=True) # 경로 안내
        set_effect(triggerIds=[5211], visible=True) # 경로 안내
        set_effect(triggerIds=[5212], visible=True) # 경로 안내
        set_effect(triggerIds=[5213], visible=True) # 경로 안내
        set_effect(triggerIds=[5214], visible=True) # 경로 안내
        set_effect(triggerIds=[5215], visible=True) # 경로 안내
        set_effect(triggerIds=[5216], visible=True) # 경로 안내
        set_effect(triggerIds=[5217], visible=True) # 경로 안내

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return GuideNextMap02()


class GuideNextMap02(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10026010)
        set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5002], visible=False) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5200], visible=False) # 경로 안내
        set_effect(triggerIds=[5201], visible=False) # 경로 안내
        set_effect(triggerIds=[5202], visible=False) # 경로 안내
        set_effect(triggerIds=[5203], visible=False) # 경로 안내
        set_effect(triggerIds=[5204], visible=False) # 경로 안내
        set_effect(triggerIds=[5205], visible=False) # 경로 안내
        set_effect(triggerIds=[5206], visible=False) # 경로 안내
        set_effect(triggerIds=[5207], visible=False) # 경로 안내
        set_effect(triggerIds=[5208], visible=False) # 경로 안내
        set_effect(triggerIds=[5209], visible=False) # 경로 안내
        set_effect(triggerIds=[5210], visible=False) # 경로 안내
        set_effect(triggerIds=[5211], visible=False) # 경로 안내
        set_effect(triggerIds=[5212], visible=False) # 경로 안내
        set_effect(triggerIds=[5213], visible=False) # 경로 안내
        set_effect(triggerIds=[5214], visible=False) # 경로 안내
        set_effect(triggerIds=[5215], visible=False) # 경로 안내
        set_effect(triggerIds=[5216], visible=False) # 경로 안내
        set_effect(triggerIds=[5217], visible=False) # 경로 안내


