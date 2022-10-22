""" trigger/63000014_cs/checkstone01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10001004], state=2) # Stone
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0) # Stone_Off
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        set_effect(triggerIds=[5002], visible=False) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5100], visible=False) # NPC 경로 안내
        set_effect(triggerIds=[5101], visible=False) # NPC 경로 안내
        set_effect(triggerIds=[5102], visible=False) # NPC 경로 안내
        set_effect(triggerIds=[5103], visible=False) # NPC 경로 안내
        set_effect(triggerIds=[5200], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5201], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5202], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5203], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5204], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5205], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5206], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5207], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5208], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5209], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5210], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5300], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5301], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5302], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5303], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5304], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5305], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5306], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5307], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5308], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5309], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5310], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5311], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5312], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5313], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5400], visible=False) # 결계석 화살표
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return LodingDelay01()


class LodingDelay01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000450], questStates=[1]):
            return QuestOnGoing30()
        if quest_user_detected(boxIds=[9900], questIds=[90000449], questStates=[3]):
            return QuestOnGoing22()
        if quest_user_detected(boxIds=[9900], questIds=[90000449], questStates=[2]):
            return QuestOnGoing21()
        if quest_user_detected(boxIds=[9900], questIds=[90000449], questStates=[1]):
            return QuestOnGoing20()
        if quest_user_detected(boxIds=[9900], questIds=[90000448], questStates=[3]):
            return QuestOnGoing10()
        if quest_user_detected(boxIds=[9900], questIds=[90000448], questStates=[2]):
            return FirstQuestEnd01()


#  첫 번째 퀘스트 완료 상태 
class QuestOnGoing10(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return SecondQuestStart01()


#   두 번째 퀘스트 수락한 상태 
class QuestOnGoing20(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return MoveToFindStone01()


#  두 번째 퀘스트 완료 가능 상태 
class QuestOnGoing21(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return SecondQuestEnd01()


#  두 번째 퀘스트 완료 상태 
class QuestOnGoing22(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return ThirdQuestStart01()


#  세 번째 퀘스트 수락한 상태 
class QuestOnGoing30(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return MoveToNextMap01()


#  최초 입장 
class FirstQuestEnd01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10030100, textId=10030100) # 가이드 : [[icon:questcomplete]] 틴차이와 대화하기
        set_effect(triggerIds=[5100], visible=True) # NPC 경로 안내
        set_effect(triggerIds=[5101], visible=True) # NPC 경로 안내
        set_effect(triggerIds=[5102], visible=True) # NPC 경로 안내
        set_effect(triggerIds=[5103], visible=True) # NPC 경로 안내

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9003]):
            return FirstQuestEnd02()


class FirstQuestEnd02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5100], visible=False) # NPC 경로 안내
        set_effect(triggerIds=[5101], visible=False) # NPC 경로 안내
        set_effect(triggerIds=[5102], visible=False) # NPC 경로 안내
        set_effect(triggerIds=[5103], visible=False) # NPC 경로 안내

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000448], questStates=[3]):
            return SecondQuestStart01()

    def on_exit(self):
        hide_guide_summary(entityId=10030100)


class SecondQuestStart01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10030160, textId=10030160) # 가이드 : [[icon:questaccept]] 틴차이와 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000449], questStates=[1]):
            return MoveToFindStone01()


class MoveToFindStone01(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001004], state=1) # Stone
        set_mesh(triggerIds=[3000], visible=False, arg3=50, arg4=0, arg5=0) # Stone_Off
        hide_guide_summary(entityId=10030160)
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10032010, textId=10032010) # 가이드 : 연꽃 쉼터의 결계석 찾기
        set_effect(triggerIds=[5400], visible=True) # 결계석 화살표
        set_effect(triggerIds=[5200], visible=True) # 결계석 경로 안내
        set_effect(triggerIds=[5201], visible=True) # 결계석 경로 안내
        set_effect(triggerIds=[5202], visible=True) # 결계석 경로 안내
        set_effect(triggerIds=[5203], visible=True) # 결계석 경로 안내
        set_effect(triggerIds=[5204], visible=True) # 결계석 경로 안내
        set_effect(triggerIds=[5205], visible=True) # 결계석 경로 안내
        set_effect(triggerIds=[5206], visible=True) # 결계석 경로 안내
        set_effect(triggerIds=[5207], visible=True) # 결계석 경로 안내
        set_effect(triggerIds=[5208], visible=True) # 결계석 경로 안내
        set_effect(triggerIds=[5209], visible=True) # 결계석 경로 안내
        set_effect(triggerIds=[5210], visible=True) # 결계석 경로 안내

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return MoveToFindStone02()


class MoveToFindStone02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5001], visible=True) # 화살표 안내 사운드 이펙트
        hide_guide_summary(entityId=10032010)
        show_guide_summary(entityId=10032020, textId=10032020) # 가이드 : 스페이스 키를 눌러 파손된 결계석 복원하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000449], questStates=[2]):
            return SecondQuestEnd01()

    def on_exit(self):
        hide_guide_summary(entityId=10032020)
        set_effect(triggerIds=[5400], visible=False) # 결계석 화살표
        set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트


class SecondQuestEnd01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10030100, textId=10030100) # 가이드 : [[icon:questcomplete]] 틴차이와 대화하기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9003]):
            return SecondQuestEnd02()


class SecondQuestEnd02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5200], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5201], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5202], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5203], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5204], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5205], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5206], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5207], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5208], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5209], visible=False) # 결계석 경로 안내
        set_effect(triggerIds=[5210], visible=False) # 결계석 경로 안내

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000449], questStates=[3]):
            return ThirdQuestStart01()

    def on_exit(self):
        hide_guide_summary(entityId=10030100)


class ThirdQuestStart01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10030160, textId=10030160) # 가이드 : [[icon:questaccept]] 틴차이와 대화하기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000450], questStates=[1]):
            return MoveToNextMap01()

    def on_exit(self):
        hide_guide_summary(entityId=10030160)


class MoveToNextMap01(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=False, minimapVisible=True)
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10032030, textId=10032030) # 가이드 : 연꽃 쉼터 북부로 연결되는 포털을 향해 이동하기
        set_effect(triggerIds=[5300], visible=True) # 다음 맵 경로 안내
        set_effect(triggerIds=[5301], visible=True) # 다음 맵 경로 안내
        set_effect(triggerIds=[5302], visible=True) # 다음 맵 경로 안내
        set_effect(triggerIds=[5303], visible=True) # 다음 맵 경로 안내
        set_effect(triggerIds=[5304], visible=True) # 다음 맵 경로 안내
        set_effect(triggerIds=[5305], visible=True) # 다음 맵 경로 안내
        set_effect(triggerIds=[5306], visible=True) # 다음 맵 경로 안내
        set_effect(triggerIds=[5307], visible=True) # 다음 맵 경로 안내
        set_effect(triggerIds=[5308], visible=True) # 다음 맵 경로 안내
        set_effect(triggerIds=[5309], visible=True) # 다음 맵 경로 안내
        set_effect(triggerIds=[5310], visible=True) # 다음 맵 경로 안내
        set_effect(triggerIds=[5311], visible=True) # 다음 맵 경로 안내
        set_effect(triggerIds=[5312], visible=True) # 다음 맵 경로 안내
        set_effect(triggerIds=[5313], visible=True) # 다음 맵 경로 안내

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return MoveToNextMap02()


class MoveToNextMap02(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10032030)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=1060, textId=1060) # 가이드 : 포털 위치에서 스페이스 키 누르기

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=1060)
        destroy_monster(spawnIds=[101])
        set_effect(triggerIds=[5300], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5301], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5302], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5303], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5304], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5305], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5306], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5307], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5308], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5309], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5310], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5311], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5312], visible=False) # 다음 맵 경로 안내
        set_effect(triggerIds=[5313], visible=False) # 다음 맵 경로 안내


