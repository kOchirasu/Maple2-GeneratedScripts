""" trigger/02020141_bf/mobspawn12.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 보스등장때까지잠시대기(self.ctx)


class 보스등장때까지잠시대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 트리거영역체크시작(self.ctx)


class 트리거영역체크시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobSpawnStop', value=4):
            return 졸몬스터제거작업(self.ctx)
        if self.monster_dead(boxIds=[99]): # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
            return 졸몬스터제거작업(self.ctx)
        if self.user_detected(boxIds=[11200]):
            return 졸몬스터등장대기중(self.ctx)


class 졸몬스터등장대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 트리거영역안플레이어최종체크(self.ctx)


class 트리거영역안플레이어최종체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobSpawnStop', value=4):
            return 졸몬스터제거작업(self.ctx)
        if self.monster_dead(boxIds=[99]): # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
            return 졸몬스터제거작업(self.ctx)
        if self.user_detected(boxIds=[11200]): # waitTick 후에도 플레이어가 트리거 박스 안에서 벗어났으면, 다시 처음단계로 돌아가기
            return 졸몬스터등장하기(self.ctx)
        if self.wait_tick(waitTick=500):
            return 트리거영역체크시작(self.ctx)


class 졸몬스터등장하기(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[11201,11202,11203,11204], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 트리거영역에계속있는지체크(self.ctx)


class 트리거영역에계속있는지체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobSpawnStop', value=4):
            return 졸몬스터제거작업(self.ctx)
        if self.monster_dead(boxIds=[99]): # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
            return 졸몬스터제거작업(self.ctx)
        if self.user_detected(boxIds=[11200]):
            return 졸몬스터리젠단계시작(self.ctx)
        if not self.user_detected(boxIds=[11200]):
            return 졸몬스터제거작동대기(self.ctx)


class 졸몬스터리젠단계시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[11200]):
            return 졸몬스터리젠대기중(self.ctx)
        if not self.user_detected(boxIds=[11200]):
            return 졸몬스터제거작동대기(self.ctx)


class 졸몬스터리젠대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobSpawnStop', value=4):
            return 졸몬스터제거작업(self.ctx)
        if self.monster_dead(boxIds=[99]): # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
            return 졸몬스터제거작업(self.ctx)
        if not self.user_detected(boxIds=[11200]):
            return 졸몬스터제거작동대기(self.ctx)
        if self.wait_tick(waitTick=15000):
            return 졸몬스터리젠YesNo(self.ctx)


class 졸몬스터리젠YesNo(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobSpawnStop', value=4):
            return 졸몬스터제거작업(self.ctx)
        if self.monster_dead(boxIds=[99]): # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
            return 졸몬스터제거작업(self.ctx)
        if self.user_detected(boxIds=[11200]):
            return 졸몬스터등장하기(self.ctx)
        if not self.user_detected(boxIds=[11200]):
            return 졸몬스터제거작동대기(self.ctx)


class 졸몬스터제거작동대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[11200]):
            return 트리거영역에계속있는지체크(self.ctx)
        if self.wait_tick(waitTick=7000):
            return 졸몬스터제거작업(self.ctx)


class 졸몬스터제거작업(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[11201,11202,11203,11204])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MobSpawnStop', value=4):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[99]): # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
            return 종료(self.ctx)
        if self.wait_tick(waitTick=2000):
            return 트리거영역체크시작(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
