""" trigger/63000019_cs/drinkjuice01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5300], visible=False) # 목표지점 바닥 웨이홍 앞
        self.set_effect(triggerIds=[5400], visible=False) # 목표지점 바닥 바텐더 앞
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=False) # 화살표 사운드 이펙트
        self.set_effect(triggerIds=[5002], visible=False) # 목료 완료 사운드 이펙트
        self.set_effect(triggerIds=[5100], visible=False) # 제 1경로 안내
        self.set_effect(triggerIds=[5101], visible=False) # 제 1경로 안내
        self.set_effect(triggerIds=[5102], visible=False) # 제 1경로 안내
        self.set_effect(triggerIds=[5103], visible=False) # 제 1경로 안내
        self.set_effect(triggerIds=[5200], visible=False) # 제 2경로 안내
        self.set_effect(triggerIds=[5201], visible=False) # 제 2경로 안내
        self.set_effect(triggerIds=[5202], visible=False) # 제 2경로 안내
        self.set_effect(triggerIds=[8000], visible=False) # WeiHong 00001395
        self.set_effect(triggerIds=[8001], visible=False) # VasaraChen 00001348
        self.set_effect(triggerIds=[8002], visible=False) # WeiHong 00001396
        self.create_monster(spawnIds=[101,201,301,401,501], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return LodingDelay01(self.ctx)


class LodingDelay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return LodingDelay02(self.ctx)


class LodingDelay02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000438], questStates=[3]):
            return QuestComplete01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000442], questStates=[3]):
            return QuestComplete01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000442], questStates=[2]):
            return MoveToBartender01(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000437], questStates=[3]):
            return TalkToWeiHong02(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000437], questStates=[2]):
            return MoveToWeiHong01(self.ctx)


# 첫 번째 퀘스트 완료 가능 상태
class MoveToWeiHong01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=10024010, textId=10024010) # 가이드 : 웨이 홍을 향해 이동하기
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=True) # 화살표 사운드 이펙트
        self.set_effect(triggerIds=[5100], visible=True) # 제 1경로 안내
        self.set_effect(triggerIds=[5101], visible=True) # 제 1경로 안내
        self.set_effect(triggerIds=[5102], visible=True) # 제 1경로 안내
        self.set_effect(triggerIds=[5103], visible=True) # 제 1경로 안내
        self.set_effect(triggerIds=[5300], visible=True) # 목표지점 바닥 웨이홍 앞

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return TalkToWeiHong01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10024010)
        self.set_effect(triggerIds=[5100], visible=False) # 제 1경로 안내
        self.set_effect(triggerIds=[5101], visible=False) # 제 1경로 안내
        self.set_effect(triggerIds=[5102], visible=False) # 제 1경로 안내
        self.set_effect(triggerIds=[5103], visible=False) # 제 1경로 안내
        self.set_effect(triggerIds=[5300], visible=False) # 목표지점 바닥 웨이홍 앞


class TalkToWeiHong01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=10024020, textId=10024020) # 가이드 : 웨이 홍과 대화하기
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000437], questStates=[3]):
            return TalkToWeiHong02(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10024020)


class TalkToWeiHong02(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=10024030, textId=10024030) # 가이드 : 웨이 홍과 대화하기
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000438], questStates=[2]):
            return MoveToBartender01(self.ctx)


class MoveToBartender01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=10024040, textId=10024040) # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=True) # 화살표 사운드 이펙트
        self.set_effect(triggerIds=[5200], visible=True) # 제 2경로 안내
        self.set_effect(triggerIds=[5201], visible=True) # 제 2경로 안내
        self.set_effect(triggerIds=[5202], visible=True) # 제 2경로 안내
        self.set_effect(triggerIds=[5400], visible=True) # 목표지점 바닥 바텐더 앞

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9002]):
            return MoveToBartender02(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10024040)
        self.set_effect(triggerIds=[5400], visible=False) # 목표지점 바닥 바텐더 앞
        self.set_effect(triggerIds=[5001], visible=False) # 화살표 사운드 이펙트
        self.set_effect(triggerIds=[5200], visible=False) # 제 2경로 안내
        self.set_effect(triggerIds=[5201], visible=False) # 제 2경로 안내
        self.set_effect(triggerIds=[5202], visible=False) # 제 2경로 안내


class MoveToBartender02(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=10024050, textId=10024050) # 가이드 : 바텐더와 대화하기
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return TalkToBartender01(self.ctx)


class TalkToBartender01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000438], questStates=[3]):
            return QuestComplete01(self.ctx)


class QuestComplete01(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=10024050)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000442], questStates=[3]):
            return TalkingDelay01(self.ctx)


# 두번째 퀘스트 및 가이드 완료 상태
class TalkingDelay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return WeiHongTalk01(self.ctx)


class WeiHongTalk01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11000251, script='$63000019_CS__DRINKJUICE01__0$', arg4=5) # Voice 00001395
        self.set_effect(triggerIds=[8000], visible=True) # WeiHong 00001395
        self.set_skip(state=WeiHongTalk02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return WeiHongTalk02(self.ctx)


class WeiHongTalk02(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_effect(triggerIds=[8000], visible=False) # WeiHong 00001395

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return WeiHongTalk03(self.ctx)


class WeiHongTalk03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001547, script='$63000019_CS__DRINKJUICE01__1$', arg4=4) # Voice 00001348
        self.set_effect(triggerIds=[8001], visible=True) # VasaraChen 00001348
        self.set_skip(state=WeiHongTalk04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return WeiHongTalk04(self.ctx)


class WeiHongTalk04(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_effect(triggerIds=[8001], visible=False) # VasaraChen 00001348

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return WeiHongTalk05(self.ctx)


class WeiHongTalk05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000251, script='$63000019_CS__DRINKJUICE01__2$', arg4=8) # Voice 00001396
        self.set_effect(triggerIds=[8002], visible=True) # WeiHong 00001396
        self.set_skip(state=MovingDelay01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return MovingDelay01(self.ctx)


class MovingDelay01(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_effect(triggerIds=[8002], visible=False) # WeiHong 00001396

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(mapId=63000020, portalId=1, boxId=9900)


initial_state = Wait
