""" trigger/63000022_cs/business01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5002], visible=False) # 미션 완료 사운드 이펙트
        self.set_effect(triggerIds=[5200], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5201], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5202], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5203], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5204], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5205], visible=False) # 경로 안내
        self.set_effect(triggerIds=[8000], visible=False) # Voice 00001397
        self.set_effect(triggerIds=[8001], visible=False) # Voice 00001398
        self.set_effect(triggerIds=[8002], visible=False) # Voice 00001399
        self.create_monster(spawnIds=[101,201,301,401], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return LodingDelay01(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(triggerId=500, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000439], questStates=[3]):
            return QuestOngoing01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000440], questStates=[1]):
            return QuestOngoing11(self.ctx)
        if self.wait_tick(waitTick=2000):
            return TalkWeiHong01(self.ctx)


# 이전  퀘스트 이미 완료한 상태
class QuestOngoing01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.select_camera(triggerId=500, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return QuestOngoing02(self.ctx)


class QuestOngoing02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NextQuestStart01(self.ctx)


# 새로운  퀘스트 이미 수락한 상태
class QuestOngoing11(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.select_camera(triggerId=500, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return QuestOngoing12(self.ctx)


class QuestOngoing12(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return MoveToNextMap01(self.ctx)


# 최초 입장
class TalkWeiHong01(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TalkWeiHong02(self.ctx)


class TalkWeiHong02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return TalkWeiHong03(self.ctx)


class TalkWeiHong03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=501, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TalkWeiHong04(self.ctx)


class TalkWeiHong04(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11000251, script='$63000022_CS__BUSINESS01__0$', arg4=6) # Voice 00001397
        self.set_effect(triggerIds=[8000], visible=True) # Voice 00001397
        self.set_skip(state=TalkWeiHong05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return TalkWeiHong05(self.ctx)


class TalkWeiHong05(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        self.move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return TalkWeiHong06(self.ctx)


class TalkWeiHong06(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.set_conversation(type=2, spawnId=11000251, script='$63000022_CS__BUSINESS01__1$', arg4=6) # Voice 00001398
        self.set_effect(triggerIds=[8001], visible=True) # Voice 00001398
        self.set_skip(state=TalkWeiHong07)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return TalkWeiHong07(self.ctx)


class TalkWeiHong07(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return TalkWeiHong08(self.ctx)


class TalkWeiHong08(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001547, script='$63000022_CS__BUSINESS01__3$', arg4=3)
        self.set_skip(state=TalkWeiHong09)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return TalkWeiHong09(self.ctx)


class TalkWeiHong09(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return TalkWeiHong10(self.ctx)


class TalkWeiHong10(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000251, script='$63000022_CS__BUSINESS01__2$', arg4=6) # Voice 00001399
        self.set_effect(triggerIds=[8002], visible=True) # Voice 00001399
        self.set_skip(state=TalkWeiHong11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return TalkWeiHong11(self.ctx)


class TalkWeiHong11(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=501, enable=False)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return QuestComplete01(self.ctx)


class QuestComplete01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=10024020, textId=10024020) # 가이드 : 웨이 홍과 대화하기
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000439], questStates=[3]):
            return NextQuestStart01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10024020)


class NextQuestStart01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=10024030, textId=10024030) # 가이드 : 웨이 홍과 대화하기
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000440], questStates=[1]):
            return MoveToNextMap01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10024030)


class MoveToNextMap01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=10027010, textId=10027010) # 가이드 : 포털을 타고 흑성회 고물 처리장으로 이동하기
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=True) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5200], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5201], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5202], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5203], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5204], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5205], visible=True) # 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return MoveToNextMap02(self.ctx)


class MoveToNextMap02(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=10027010)
        self.set_effect(triggerIds=[5002], visible=False) # 미션 완료 사운드 이펙트
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5200], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5201], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5202], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5203], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5204], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5205], visible=False) # 경로 안내


initial_state = Wait
