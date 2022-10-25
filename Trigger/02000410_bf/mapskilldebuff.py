""" trigger/02000410_bf/mapskilldebuff.xml """
import common


class Ready(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[444], enable=False) # 맵 스킬 초기화 셋팅
        self.set_skill(triggerIds=[666], enable=False) # 맵 스킬 초기화 셋팅

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=750, boxId=1):
            return 전투시작(self.ctx)


class 전투시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.dungeon_check_play_time(playSeconds=600): # 언제든지  파티원이 전멸하거나 파티장이 던전 포기를 해서 몬스터가 전부 제거 될 수 있어서, 맵셋팅 스킬은 트리거 영역 안의 몬스터가 없으면 꺼지도록 매 턴마다 체크할 수 있도록 함
            return 단계_70000103_1(self.ctx)
        if not self.npc_detected(boxId=700, spawnIds=[0]):
            return 스킬끄기(self.ctx)


class 단계_70000103_1(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[444], enable=True) # 70000103  스킬 사용함

    def on_tick(self) -> common.Trigger:
        if self.dungeon_check_play_time(playSeconds=780): # 언제든지  파티원이 전멸하거나 파티장이 던전 포기를 해서 몬스터가 전부 제거 될 수 있어서, 맵셋팅 스킬은 트리거 영역 안의 몬스터가 없으면 꺼지도록 매 턴마다 체크할 수 있도록 함
            return 단계_70000104_2(self.ctx)
        if not self.npc_detected(boxId=700, spawnIds=[0]):
            return 스킬끄기(self.ctx)


class 단계_70000104_2(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[666], enable=True) # 70000104 스킬 사용함

    def on_tick(self) -> common.Trigger:
        if self.dungeon_check_play_time(playSeconds=900): # 언제든지  파티원이 전멸하거나 파티장이 던전 포기를 해서 몬스터가 전부 제거 될 수 있어서, 맵셋팅 스킬은 트리거 영역 안의 몬스터가 없으면 꺼지도록 매 턴마다 체크할 수 있도록 함
            return 스킬끄기(self.ctx)
        if not self.npc_detected(boxId=700, spawnIds=[0]):
            return 스킬끄기(self.ctx)


class 스킬끄기(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[444], enable=False) # 맵 스킬 끄기
        self.set_skill(triggerIds=[666], enable=False) # 던전실패 하거나 던전성공 하거나 어쨌든 끝나면 혹시 몸에 걸려있는 지옥의 불 시리즈 디버프를 제거해 주기 위해 아래 애디셔널을 걸어줌
        self.add_buff(boxIds=[750], skillId=50004524, level=1, isPlayer=False) # 지옥의 불 디버프 제거해주는 애디샤날던 던전 끝나면 걸어주기, MS2TriggerBox   TriggerObjectID = 750,   750은 스타팅 지점 전투판 다  포함되는 범위

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = Ready
