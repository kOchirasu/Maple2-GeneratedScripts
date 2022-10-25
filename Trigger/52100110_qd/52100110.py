""" trigger/52100110_qd/52100110.xml """
import common


class Ready(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[10000], visible=False)
        self.set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1000]):
            return 퀘스트체크(self.ctx)


class 퀘스트체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[1000], questIds=[50101040], questStates=[1]):
            return 화이트박스제거(self.ctx)
        if self.quest_user_detected(boxIds=[1000], questIds=[50101030], questStates=[3]):
            return 로텔레포트52100105(self.ctx)
        if self.quest_user_detected(boxIds=[1000], questIds=[50101030], questStates=[2]):
            return 퀘스트용몬스터스폰(self.ctx)
        if self.quest_user_detected(boxIds=[1000], questIds=[50101030], questStates=[1]):
            return 퀘스트용몬스터스폰(self.ctx)
        if self.quest_user_detected(boxIds=[1000], questIds=[50101020], questStates=[3]):
            return 퀘스트용몬스터스폰(self.ctx)


class 퀘스트체크2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[1000], questIds=[50101040], questStates=[1]):
            return 화이트박스제거(self.ctx)
        if self.quest_user_detected(boxIds=[1000], questIds=[50101030], questStates=[3]):
            return None # Missing State: 


class 로텔레포트52100105(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[10000], visible=True)
        self.move_user(mapId=52100105, portalId=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return None # Missing State: 


class 퀘스트용몬스터스폰(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,102,103], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 화이트박스생성2(self.ctx)


class 화이트박스생성2(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[10000], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 퀘스트체크2(self.ctx)


class 화이트박스제거(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[10000], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return None # Missing State: 


initial_state = Ready
