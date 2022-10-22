""" trigger/63000022_cs/business01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5002], visible=False) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5200], visible=False) # 경로 안내
        set_effect(triggerIds=[5201], visible=False) # 경로 안내
        set_effect(triggerIds=[5202], visible=False) # 경로 안내
        set_effect(triggerIds=[5203], visible=False) # 경로 안내
        set_effect(triggerIds=[5204], visible=False) # 경로 안내
        set_effect(triggerIds=[5205], visible=False) # 경로 안내
        set_effect(triggerIds=[8000], visible=False) # Voice 00001397
        set_effect(triggerIds=[8001], visible=False) # Voice 00001398
        set_effect(triggerIds=[8002], visible=False) # Voice 00001399
        create_monster(spawnIds=[101,201,301,401], arg2=False)

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
        if quest_user_detected(boxIds=[9900], questIds=[90000439], questStates=[3]):
            return QuestOngoing01()
        if quest_user_detected(boxIds=[9900], questIds=[90000440], questStates=[1]):
            return QuestOngoing11()
        if wait_tick(waitTick=2000):
            return TalkWeiHong01()


#  이전  퀘스트 이미 완료한 상태 
class QuestOngoing01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)
        select_camera(triggerId=500, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return QuestOngoing02()


class QuestOngoing02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if true():
            return NextQuestStart01()


#  새로운  퀘스트 이미 수락한 상태 
class QuestOngoing11(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)
        select_camera(triggerId=500, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return QuestOngoing12()


class QuestOngoing12(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if true():
            return MoveToNextMap01()


#  최초 입장 
class TalkWeiHong01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TalkWeiHong02()


class TalkWeiHong02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return TalkWeiHong03()


class TalkWeiHong03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=501, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TalkWeiHong04()


class TalkWeiHong04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11000251, script='$63000022_CS__BUSINESS01__0$', arg4=6) # Voice 00001397
        set_effect(triggerIds=[8000], visible=True) # Voice 00001397
        set_skip(state=TalkWeiHong05)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return TalkWeiHong05()


class TalkWeiHong05(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return TalkWeiHong06()


class TalkWeiHong06(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11000251, script='$63000022_CS__BUSINESS01__1$', arg4=6) # Voice 00001398
        set_effect(triggerIds=[8001], visible=True) # Voice 00001398
        set_skip(state=TalkWeiHong07)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return TalkWeiHong07()


class TalkWeiHong07(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')

    def on_tick(self) -> state.State:
        if true():
            return TalkWeiHong08()


class TalkWeiHong08(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001547, script='$63000022_CS__BUSINESS01__3$', arg4=3)
        set_skip(state=TalkWeiHong09)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return TalkWeiHong09()


class TalkWeiHong09(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return TalkWeiHong10()


class TalkWeiHong10(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000251, script='$63000022_CS__BUSINESS01__2$', arg4=6) # Voice 00001399
        set_effect(triggerIds=[8002], visible=True) # Voice 00001399
        set_skip(state=TalkWeiHong11)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return TalkWeiHong11()


class TalkWeiHong11(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=501, enable=False)
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return QuestComplete01()


class QuestComplete01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10024020, textId=10024020) # 가이드 : 웨이 홍과 대화하기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000439], questStates=[3]):
            return NextQuestStart01()

    def on_exit(self):
        hide_guide_summary(entityId=10024020)


class NextQuestStart01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10024030, textId=10024030) # 가이드 : 웨이 홍과 대화하기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000440], questStates=[1]):
            return MoveToNextMap01()

    def on_exit(self):
        hide_guide_summary(entityId=10024030)


class MoveToNextMap01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10027010, textId=10027010) # 가이드 : 포털을 타고 흑성회 고물 처리장으로 이동하기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=True) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5200], visible=True) # 경로 안내
        set_effect(triggerIds=[5201], visible=True) # 경로 안내
        set_effect(triggerIds=[5202], visible=True) # 경로 안내
        set_effect(triggerIds=[5203], visible=True) # 경로 안내
        set_effect(triggerIds=[5204], visible=True) # 경로 안내
        set_effect(triggerIds=[5205], visible=True) # 경로 안내

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return MoveToNextMap02()


class MoveToNextMap02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10027010)
        set_effect(triggerIds=[5002], visible=False) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5200], visible=False) # 경로 안내
        set_effect(triggerIds=[5201], visible=False) # 경로 안내
        set_effect(triggerIds=[5202], visible=False) # 경로 안내
        set_effect(triggerIds=[5203], visible=False) # 경로 안내
        set_effect(triggerIds=[5204], visible=False) # 경로 안내
        set_effect(triggerIds=[5205], visible=False) # 경로 안내


