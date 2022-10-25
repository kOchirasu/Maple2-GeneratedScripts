""" trigger/02100002_bf/102_mobspawn_skyblue.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='Gauge', value=0) # 탱크 리필 트리거에서 받는 신호
        self.set_user_value(key='StopSpawn', value=0) # 홀더 트리거에서 받는 신호 0이면 스폰 진행 / 1이면 스폰 중지
        self.set_user_value(key='SpawnHold', value=0)
        self.destroy_monster(spawnIds=[20100,20075,20050,20025,20001,21001,21002,21003])
        self.set_effect(triggerIds=[5102], visible=False) # Normal Slime Rebirth Sound
        self.set_effect(triggerIds=[5202], visible=False) # Abnormal Slime Rebirth Sound

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Gauge', value=100):
            return Gauge100_Normal(self.ctx)


class Gauge100_Normal(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # Normal Slime Rebirth Sound
        self.create_monster(spawnIds=[20100], animationEffect=False) # 100%

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return Gauge_SpawnRamdom(self.ctx)
        if self.user_value(key='SpawnHold', value=1):
            return SpawnHold(self.ctx)
        if self.user_value(key='Gauge', value=75):
            return Gauge75_Normal(self.ctx)
        if self.user_value(key='StopSpawn', value=1):
            return Quit(self.ctx)


class Gauge75_Normal(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # Normal Slime Rebirth Sound
        self.create_monster(spawnIds=[20075], animationEffect=False) # 75%

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return Gauge_SpawnRamdom(self.ctx)
        if self.user_value(key='SpawnHold', value=1):
            return SpawnHold(self.ctx)
        if self.user_value(key='Gauge', value=100):
            return Gauge100_Normal(self.ctx)
        if self.user_value(key='Gauge', value=50):
            return Gauge50_Normal(self.ctx)
        if self.user_value(key='StopSpawn', value=1):
            return Quit(self.ctx)


class Gauge50_Normal(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # Normal Slime Rebirth Sound
        self.create_monster(spawnIds=[20050], animationEffect=False) # 50%

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return Gauge_SpawnRamdom(self.ctx)
        if self.user_value(key='SpawnHold', value=1):
            return SpawnHold(self.ctx)
        if self.user_value(key='Gauge', value=75):
            return Gauge75_Normal(self.ctx)
        if self.user_value(key='Gauge', value=25):
            return Gauge25_Normal(self.ctx)
        if self.user_value(key='StopSpawn', value=1):
            return Quit(self.ctx)


class Gauge25_Normal(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # Normal Slime Rebirth Sound
        self.create_monster(spawnIds=[20025], animationEffect=False) # 25%

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return Gauge_SpawnRamdom(self.ctx)
        if self.user_value(key='SpawnHold', value=1):
            return SpawnHold(self.ctx)
        if self.user_value(key='Gauge', value=50):
            return Gauge50_Normal(self.ctx)
        if self.user_value(key='Gauge', value=1):
            return Gauge1_Normal(self.ctx)
        if self.user_value(key='StopSpawn', value=1):
            return Quit(self.ctx)


class Gauge1_Normal(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # Normal Slime Rebirth Sound
        self.create_monster(spawnIds=[20001], animationEffect=False) # 1%

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return Gauge_SpawnRamdom(self.ctx)
        if self.user_value(key='SpawnHold', value=1):
            return SpawnHold(self.ctx)
        if self.user_value(key='Gauge', value=25):
            return Gauge25_Normal(self.ctx)
        if self.user_value(key='StopSpawn', value=1):
            return Quit(self.ctx)


# 스폰 홀드
class SpawnHold(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SpawnHold', value=0):
            return BackToGaugeState(self.ctx)
        if self.user_value(key='StopSpawn', value=1):
            return Quit(self.ctx)


# 돌연변이 슬라임 랜덤 낮은 확률
class Gauge_SpawnRamdom(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=100, desc='Normal'):
            return Spawn_Normal(self.ctx)
        if self.random_condition(rate=5, desc='Eater'):
            return Spawn_Eater(self.ctx)
        if self.random_condition(rate=10, desc='Runner'):
            return Spawn_Runner(self.ctx)
        """
        <condition name="랜덤조건" arg1="1" desc="BigMom">
            <transition state="Spawn_BigMom" /> 
        </condition>
        """


# 랜덤 스폰 공용
class Spawn_Normal(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.true():
            return BackToGaugeState(self.ctx)


class Spawn_Eater(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5202], visible=True) # Abnormal Slime Rebirth Sound
        self.create_monster(spawnIds=[21001], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return BackToGaugeState(self.ctx)


class Spawn_Runner(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5202], visible=True) # Abnormal Slime Rebirth Sound
        self.create_monster(spawnIds=[21002], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return BackToGaugeState(self.ctx)


# 게이지 상태 체크로 돌아가기 공용
class BackToGaugeState(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Gauge', value=100):
            return Gauge100_Normal(self.ctx)
        if self.user_value(key='Gauge', value=75):
            return Gauge75_Normal(self.ctx)
        if self.user_value(key='Gauge', value=50):
            return Gauge50_Normal(self.ctx)
        if self.user_value(key='Gauge', value=25):
            return Gauge25_Normal(self.ctx)
        if self.user_value(key='Gauge', value=1):
            return Gauge1_Normal(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[20100,20075,20050,20025,20001,21001,21002,21003])


initial_state = Wait
