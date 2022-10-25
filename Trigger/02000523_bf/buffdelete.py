""" trigger/02000523_bf/buffdelete.xml """
import common


# TriggerModelID =  7 , 이 트리거는   AI_SandstoneGiantBlueShine.xml    AI_SandstoneDwarf2CloseAttack.xml   AI_SandstoneDwarf2LongAttack.xml 로 부터 신호를 받음
class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='MonsterMany', value=0) # MonsterMany변수 0으로 초기 셋팅, 소환몹이 한마리 나올때마다 1 더하고 한마리씩 죽으몬 1 빼기 함, 몬스터 등장 이전에 이 변수 0 초기화 하기
        self.set_user_value(key='BuffDeleteOk', value=0) # BuffDeleteOk 0으로 초기 셋팅, 보스가 소환몹 호출하면 AI_SandstoneGiantBlueShine.xml로 부터 1 셋팅 신호를 받게 됨

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 트리거작동01(self.ctx)


class 트리거작동01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BuffDeleteOk', value=1):
            return 트리거작동02대기중(self.ctx)


class 트리거작동02대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1200):
            return 트리거작동02(self.ctx)


class 트리거작동02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='MonsterMany', value=0):
            return 버프제거(self.ctx)


class 버프제거(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[900], skillId=50001098, level=1, isPlayer=True) # 물방업, 마방업, 공업 버프 제거 하는 기능이 있는 버프 부여하기 ,   arg1="900" 보스 스폰 ID ,  arg3="1" 은 애디셔널 레벨
        self.set_user_value(key='BuffDeleteOk', value=0) # 이 변수 0 초기화 시켜, 보스가 졸몹 소환때까지 다시 대기 상태가 되도록 함

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3700):
            return 트리거작동01(self.ctx)


initial_state = 시작대기중
