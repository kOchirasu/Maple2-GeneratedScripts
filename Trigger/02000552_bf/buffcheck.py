""" trigger/02000552_bf/buffcheck.xml """
import common


# TriggerModelID =  553
class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='MonsterMany', value=0) # MonsterMany변수 0으로 초기 셋팅, 소환몹이 한마리 나올때마다 1 더하고 한마리씩 죽으몬 1 빼기 함, 몬스터 등장 이전에 이 변수 0 초기화 하기

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 트리거작동시작(self.ctx)


class 트리거작동시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='MonsterMany', value=1, operator='GreaterEqual'):
            return 블랙빈에게버프부여(self.ctx)


class 블랙빈에게버프부여(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[101], skillId=50003307, level=2, isPlayer=True) # 공격반사 버프 부여하기 ,   arg1="101" 보스 스폰 ID ,  arg3="1" 은 애디셔널 레벨
        self.add_buff(boxIds=[102], skillId=50003307, level=2, isPlayer=True) # 공격반사 버프 부여하기 ,   arg1="102" 보스 스폰 ID ,  arg3="1" 은 애디셔널 레벨

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 블랙빈에게버프삭제체크(self.ctx)


class 블랙빈에게버프삭제체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='MonsterMany', value=0):
            return 블랙빈에게버프삭제대기(self.ctx)


class 블랙빈에게버프삭제대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=900):
            return 블랙빈에게버프삭제실시(self.ctx)


class 블랙빈에게버프삭제실시(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[101], skillId=50003309, level=1, isPlayer=True) # 공격반사 버프 버프 제거 ,   arg1="101" 보스 스폰 ID ,  arg3="1" 은 애디셔널 레벨
        self.add_buff(boxIds=[102], skillId=50003309, level=1, isPlayer=True) # 공격반사 버프 버프 제거 ,   arg1="102" 보스 스폰 ID ,  arg3="1" 은 애디셔널 레벨

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 트리거작동시작(self.ctx)


initial_state = 시작대기중
