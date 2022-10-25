""" trigger/02020300_bf/monsterspawn.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990001, key='SpawnRoomEnd', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Spawn', value=1):
            return 스폰1(self.ctx)


class 스폰1(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[111,121,131,141], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=20000):
            return 스폰2(self.ctx)


class 스폰2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[112,122,132,142], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=20000):
            return 스폰5(self.ctx)


# 스폰3, 4는 스킵, 바로 5로 넘어감(1,2,5), 전체적인 전투 시간을 고려하여 밸런스 조정. 추후 수정 가능
class 스폰3(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[113,123,133,143], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return 스폰4(self.ctx)


class 스폰4(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[114,124,134,144], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=13000):
            return 스폰5(self.ctx)


# 필요에 따라 웨이브 하나씩 열어줄 수 있도록 코드 남겨둠.
class 스폰5(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[115,125,135,145], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[111,112,113,114,115,121,122,123,124,125,131,132,133,134,135,141,142,143,144,145]):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990001, key='SpawnRoomEnd', value=1)


initial_state = 대기
