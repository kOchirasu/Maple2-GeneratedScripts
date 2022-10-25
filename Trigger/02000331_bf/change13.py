""" trigger/02000331_bf/change13.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9024, spawnIds=[604]):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9030, spawnIds=[990]):
            return 분기점(self.ctx)


# 자코 몬스터 웨이브 중 꼬마가 사망했는지 체크
class 분기점(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9030, spawnIds=[999]):
            return 보스전투(self.ctx)
        if self.monster_dead(boxIds=[604]):
            return 교체딜레이(self.ctx)


# 보스 몬스터 웨이브 중 꼬마가 사망했는지 체크
class 보스전투(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[999]):
            return 전투종료(self.ctx)
        if self.monster_dead(boxIds=[604]):
            return 교체딜레이(self.ctx)


# 보스 몬스터가 죽을 때 까지 꼬마 NPC가 살아 있는지 체크
class 전투종료(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9024, spawnIds=[604]):
            return 디펜스성공(self.ctx)


# 모든 전투가 끝날 때 까지 꼬마 NPC가 살아 있으면 교체 없이 종료
class 디펜스성공(common.Trigger):
    pass


# 자코 또는 보스 몬스터와 전투 중 꼬마가 쓰러졌을 때 교체 진행
class 교체딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 교체쓰러짐(self.ctx)


class 교체쓰러짐(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[614])

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9020, spawnIds=[600]):
            return 교체일어남(self.ctx)


class 교체일어남(common.Trigger):
    def on_enter(self):
        self.change_monster(removeSpawnId=614, addSpawnId=410)


initial_state = 대기
