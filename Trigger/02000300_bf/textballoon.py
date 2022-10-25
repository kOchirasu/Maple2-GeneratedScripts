""" trigger/02000300_bf/textballoon.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_in_combat(boxIds=[1099]):
            return 랜덤대화(self.ctx)
        if self.monster_dead(boxIds=[1099]):
            return 종료대화(self.ctx)


class 랜덤대화(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=25):
            return 초20(self.ctx)
        if self.random_condition(rate=25):
            return 초25(self.ctx)
        if self.random_condition(rate=25):
            return 초30(self.ctx)
        if self.random_condition(rate=25):
            return 초35(self.ctx)
        if self.monster_dead(boxIds=[1099]):
            return 종료대화(self.ctx)


class 초20(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='20', seconds=20)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='20'):
            return 대화(self.ctx)
        if self.monster_dead(boxIds=[1099]):
            return 종료대화(self.ctx)


class 초25(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='25', seconds=25)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='25'):
            return 대화(self.ctx)
        if self.monster_dead(boxIds=[1099]):
            return 종료대화(self.ctx)


class 초30(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='30', seconds=30)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='30'):
            return 대화(self.ctx)
        if self.monster_dead(boxIds=[1099]):
            return 종료대화(self.ctx)


class 초35(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='35', seconds=35)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='35'):
            return 대화(self.ctx)
        if self.monster_dead(boxIds=[1099]):
            return 종료대화(self.ctx)


class 대화(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=25):
            return 대사1(self.ctx)
        if self.random_condition(rate=25):
            return 대사2(self.ctx)
        if self.random_condition(rate=25):
            return 대사3(self.ctx)
        if self.random_condition(rate=25):
            return 대사4(self.ctx)


class 대사1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=1002, script='$02000300_BF__TEXTBALLOON__0$', arg4=2, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 대기(self.ctx)


class 대사2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=1003, script='$02000300_BF__TEXTBALLOON__1$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 대기(self.ctx)


class 대사3(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=1003, script='$02000300_BF__TEXTBALLOON__2$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 대기(self.ctx)


class 대사4(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_conversation(type=1, spawnId=1004, script='$02000300_BF__TEXTBALLOON__3$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 대기(self.ctx)


class 종료대화(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=10)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='10'):
            self.set_conversation(type=1, spawnId=1001, script='$02000300_BF__TEXTBALLOON__4$', arg4=3, arg5=0)
            self.set_conversation(type=1, spawnId=1003, script='$02000300_BF__TEXTBALLOON__5$', arg4=2, arg5=2)
            self.set_conversation(type=1, spawnId=1002, script='$02000300_BF__TEXTBALLOON__6$', arg4=2, arg5=4)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
