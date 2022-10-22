""" trigger/63000019_cs/drinkjuice01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5300], visible=False) # 목표지점 바닥 웨이홍 앞
        set_effect(triggerIds=[5400], visible=False) # 목표지점 바닥 바텐더 앞
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=False) # 화살표 사운드 이펙트
        set_effect(triggerIds=[5002], visible=False) # 목료 완료 사운드 이펙트
        set_effect(triggerIds=[5100], visible=False) # 제 1경로 안내
        set_effect(triggerIds=[5101], visible=False) # 제 1경로 안내
        set_effect(triggerIds=[5102], visible=False) # 제 1경로 안내
        set_effect(triggerIds=[5103], visible=False) # 제 1경로 안내
        set_effect(triggerIds=[5200], visible=False) # 제 2경로 안내
        set_effect(triggerIds=[5201], visible=False) # 제 2경로 안내
        set_effect(triggerIds=[5202], visible=False) # 제 2경로 안내
        set_effect(triggerIds=[8000], visible=False) # WeiHong 00001395
        set_effect(triggerIds=[8001], visible=False) # VasaraChen 00001348
        set_effect(triggerIds=[8002], visible=False) # WeiHong 00001396
        create_monster(spawnIds=[101,201,301,401,501], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return LodingDelay01()


class LodingDelay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LodingDelay02()


class LodingDelay02(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000438], questStates=[3]):
            return QuestComplete01()
        if quest_user_detected(boxIds=[9900], questIds=[90000442], questStates=[3]):
            return QuestComplete01()
        if quest_user_detected(boxIds=[9900], questIds=[90000442], questStates=[2]):
            return MoveToBartender01()
        if quest_user_detected(boxIds=[9900], questIds=[90000437], questStates=[3]):
            return TalkToWeiHong02()
        if quest_user_detected(boxIds=[9900], questIds=[90000437], questStates=[2]):
            return MoveToWeiHong01()


#   첫 번째 퀘스트 완료 가능 상태
class MoveToWeiHong01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10024010, textId=10024010) # 가이드 : 웨이 홍을 향해 이동하기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=True) # 화살표 사운드 이펙트
        set_effect(triggerIds=[5100], visible=True) # 제 1경로 안내
        set_effect(triggerIds=[5101], visible=True) # 제 1경로 안내
        set_effect(triggerIds=[5102], visible=True) # 제 1경로 안내
        set_effect(triggerIds=[5103], visible=True) # 제 1경로 안내
        set_effect(triggerIds=[5300], visible=True) # 목표지점 바닥 웨이홍 앞

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return TalkToWeiHong01()

    def on_exit(self):
        hide_guide_summary(entityId=10024010)
        set_effect(triggerIds=[5100], visible=False) # 제 1경로 안내
        set_effect(triggerIds=[5101], visible=False) # 제 1경로 안내
        set_effect(triggerIds=[5102], visible=False) # 제 1경로 안내
        set_effect(triggerIds=[5103], visible=False) # 제 1경로 안내
        set_effect(triggerIds=[5300], visible=False) # 목표지점 바닥 웨이홍 앞


class TalkToWeiHong01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10024020, textId=10024020) # 가이드 : 웨이 홍과 대화하기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000437], questStates=[3]):
            return TalkToWeiHong02()

    def on_exit(self):
        hide_guide_summary(entityId=10024020)


class TalkToWeiHong02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10024030, textId=10024030) # 가이드 : 웨이 홍과 대화하기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000438], questStates=[2]):
            return MoveToBartender01()


class MoveToBartender01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10024040, textId=10024040) # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5001], visible=True) # 화살표 사운드 이펙트
        set_effect(triggerIds=[5200], visible=True) # 제 2경로 안내
        set_effect(triggerIds=[5201], visible=True) # 제 2경로 안내
        set_effect(triggerIds=[5202], visible=True) # 제 2경로 안내
        set_effect(triggerIds=[5400], visible=True) # 목표지점 바닥 바텐더 앞

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return MoveToBartender02()

    def on_exit(self):
        hide_guide_summary(entityId=10024040)
        set_effect(triggerIds=[5400], visible=False) # 목표지점 바닥 바텐더 앞
        set_effect(triggerIds=[5001], visible=False) # 화살표 사운드 이펙트
        set_effect(triggerIds=[5200], visible=False) # 제 2경로 안내
        set_effect(triggerIds=[5201], visible=False) # 제 2경로 안내
        set_effect(triggerIds=[5202], visible=False) # 제 2경로 안내


class MoveToBartender02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10024050, textId=10024050) # 가이드 : 바텐더와 대화하기
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if true():
            return TalkToBartender01()


class TalkToBartender01(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000438], questStates=[3]):
            return QuestComplete01()


class QuestComplete01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=10024050)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000442], questStates=[3]):
            return TalkingDelay01()


#  두번째 퀘스트 및 가이드 완료 상태  
class TalkingDelay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return WeiHongTalk01()


class WeiHongTalk01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11000251, script='$63000019_CS__DRINKJUICE01__0$', arg4=5) # Voice 00001395
        set_effect(triggerIds=[8000], visible=True) # WeiHong 00001395
        set_skip(state=WeiHongTalk02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return WeiHongTalk02()


class WeiHongTalk02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[8000], visible=False) # WeiHong 00001395

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return WeiHongTalk03()


class WeiHongTalk03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001547, script='$63000019_CS__DRINKJUICE01__1$', arg4=4) # Voice 00001348
        set_effect(triggerIds=[8001], visible=True) # VasaraChen 00001348
        set_skip(state=WeiHongTalk04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return WeiHongTalk04()


class WeiHongTalk04(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[8001], visible=False) # VasaraChen 00001348

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return WeiHongTalk05()


class WeiHongTalk05(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000251, script='$63000019_CS__DRINKJUICE01__2$', arg4=8) # Voice 00001396
        set_effect(triggerIds=[8002], visible=True) # WeiHong 00001396
        set_skip(state=MovingDelay01)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return MovingDelay01()


class MovingDelay01(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_effect(triggerIds=[8002], visible=False) # WeiHong 00001396

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=63000020, portalId=1, boxId=9900)


