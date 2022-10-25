""" trigger/02000331_bf/defence17.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[99993]):
            return 전투시작(self.ctx)


class 전투시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9030, spawnIds=[999]):
            return 전투중(self.ctx)


class 전투중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[999]):
            return 생존체크01(self.ctx)


class 생존체크01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=99997, spawnIds=[601]):
            return 생존체크02(self.ctx)
        if self.monster_dead(boxIds=[601]):
            return 종료(self.ctx)


class 생존체크02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=99997, spawnIds=[602]):
            return 생존체크03(self.ctx)
        if self.monster_dead(boxIds=[602]):
            return 종료(self.ctx)


class 생존체크03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=99997, spawnIds=[603]):
            return 생존체크04(self.ctx)
        if self.monster_dead(boxIds=[603]):
            return 종료(self.ctx)


class 생존체크04(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=99997, spawnIds=[604]):
            return 생존체크05(self.ctx)
        if self.monster_dead(boxIds=[604]):
            return 종료(self.ctx)


class 생존체크05(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=99997, spawnIds=[605]):
            return 업적발생(self.ctx)
        if self.monster_dead(boxIds=[605]):
            return 종료(self.ctx)


class 업적발생(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=99996, type='trigger', achieve='defence_child') # defence_child


class 종료(common.Trigger):
    pass


initial_state = 대기
