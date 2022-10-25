""" trigger/02000109_in/main.xml """
import common


class start(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4001,4002,4003,4004], visible=True)
        self.set_mesh(triggerIds=[4011], visible=False)
        self.destroy_monster(spawnIds=[101,102])

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001608], questStates=[3]):
            return 종료(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001608], questStates=[2]):
            return 일기장스폰_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001608], questStates=[1]):
            return 일기장스폰_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[3]):
            return 일기장스폰_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[2]):
            return 일기장스폰_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[1]):
            return 벽삭제(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[3]):
            return npc스폰_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[2]):
            return npc스폰_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[1]):
            return 종료(self.ctx)


class 퀘스트진행체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001608], questStates=[3]):
            return 종료(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001608], questStates=[2]):
            return None # Missing State: 일기장스폰
        if self.quest_user_detected(boxIds=[9000], questIds=[50001608], questStates=[1]):
            return None # Missing State: 일기장스폰
        if self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[3]):
            return None # Missing State: 일기장스폰
        if self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[2]):
            return 일기장스폰_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[1]):
            return 벽삭제(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[3]):
            return npc스폰(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[2]):
            return npc스폰(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[1]):
            return 종료(self.ctx)


class npc스폰_대기(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[1]):
            return 벽삭제(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[1]):
            return 퀘스트진행체크(self.ctx)


class npc스폰(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[1]):
            return 벽삭제(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[1]):
            return 퀘스트진행체크(self.ctx)


class 벽삭제(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4001,4002,4003,4004], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[2]):
            return 일기장스폰_대기(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[2]):
            return 퀘스트진행체크(self.ctx)


class 일기장스폰_대기(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.set_mesh(triggerIds=[4011], visible=True)
        self.set_mesh(triggerIds=[4001,4002,4003,4004], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[3]):
            return 종료(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[3]):
            return 일기장스폰01(self.ctx)


class 일기장스폰01(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4011], visible=True)
        self.set_mesh(triggerIds=[4001,4002,4003,4004], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[3]):
            return 종료(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[2]):
            return 일기장스폰02(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[3]):
            return 일기장없어짐(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[3]):
            return 일기장스폰02(self.ctx)


class 일기장스폰02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[4011], visible=True)
        self.set_mesh(triggerIds=[4001,4002,4003,4004], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[3]):
            return 종료(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[2]):
            return 일기장스폰01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[3]):
            return 일기장없어짐(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[3]):
            return 일기장스폰01(self.ctx)


class 일기장없어짐(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102])
        self.set_mesh(triggerIds=[4011], visible=False)
        self.set_mesh(triggerIds=[4001,4002,4003,4004], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[2]):
            return 일기장스폰_대기(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[2]):
            return 퀘스트진행체크(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = start
