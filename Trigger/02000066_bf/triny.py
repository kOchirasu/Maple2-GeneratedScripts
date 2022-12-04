""" trigger/02000066_bf/triny.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='randomTalk', value=1):
            self.create_monster(spawnIds=[5002], animationEffect=False)
            return 전투대기(self.ctx)


class 전투대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[5002]):
            return 말풍선랜덤(self.ctx)


class 말풍선랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=25):
            return NPC대사01(self.ctx)
        if self.random_condition(rate=25):
            return NPC대사02(self.ctx)
        if self.random_condition(rate=25):
            return NPC대사03(self.ctx)
        if self.random_condition(rate=25):
            return NPC대사04(self.ctx)


class NPC대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=5002, script='$02000066_BF__TRINY__0$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class NPC대사02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=5002, script='$02000066_BF__TRINY__1$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class NPC대사03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=5002, script='$02000066_BF__TRINY__2$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class NPC대사04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=5002, script='$02000066_BF__TRINY__3$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 전투대기(self.ctx)


initial_state = 시작
