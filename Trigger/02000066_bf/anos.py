""" trigger/02000066_bf/anos.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[103]):
            return NPC생성(self.ctx)


class NPC생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[98], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대기시간(self.ctx)


class 대기시간(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 말풍선랜덤(self.ctx)


class 말풍선랜덤(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=25):
            return NPC대사01(self.ctx)
        if self.random_condition(rate=25):
            return NPC대사02(self.ctx)
        if self.random_condition(rate=25):
            return NPC대사03(self.ctx)
        if self.random_condition(rate=25):
            return NPC대사04(self.ctx)


class NPC대사01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=98, script='$02000066_BF__ANOS__0$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class NPC대사02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=98, script='$02000066_BF__ANOS__1$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class NPC대사03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=98, script='$02000066_BF__ANOS__2$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class NPC대사04(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=98, script='$02000066_BF__ANOS__3$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기시간(self.ctx)


initial_state = 시작
