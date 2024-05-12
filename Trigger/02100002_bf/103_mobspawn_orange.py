""" trigger/02100002_bf/103_mobspawn_orange.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 탱크 리필 트리거에서 받는 신호
        self.set_user_value(key='Gauge', value=0) # 탱크 리필 트리거에서 받는 신호
        # 홀더 트리거에서 받는 신호 0이면 스폰 진행 / 1이면 스폰 중지
        self.set_user_value(key='StopSpawn', value=0)
        self.set_user_value(key='SpawnHold', value=0)
        self.destroy_monster(spawnIds=[30100,30075,30050,30025,30001,31001,31002,31003])
        # Normal Slime Rebirth Sound
        self.set_effect(triggerIds=[5103], visible=False)
        # Abnormal Slime Rebirth Sound
        self.set_effect(triggerIds=[5203], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Gauge', value=100):
            return Gauge100_Normal(self.ctx)


class Gauge100_Normal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Normal Slime Rebirth Sound
        self.set_effect(triggerIds=[5103], visible=True)
        self.create_monster(spawnIds=[30100], animationEffect=False) # 100%

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return Gauge_SpawnRamdom(self.ctx)
        if self.user_value(key='SpawnHold', value=1):
            return SpawnHold(self.ctx)
        if self.user_value(key='Gauge', value=75):
            return Gauge75_Normal(self.ctx)
        if self.user_value(key='StopSpawn', value=1):
            return Quit(self.ctx)


class Gauge75_Normal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Normal Slime Rebirth Sound
        self.set_effect(triggerIds=[5103], visible=True)
        self.create_monster(spawnIds=[30075], animationEffect=False) # 75%

    def on_tick(self) -> trigger_api.Trigger:
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


class Gauge50_Normal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Normal Slime Rebirth Sound
        self.set_effect(triggerIds=[5103], visible=True)
        self.create_monster(spawnIds=[30050], animationEffect=False) # 50%

    def on_tick(self) -> trigger_api.Trigger:
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


class Gauge25_Normal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Normal Slime Rebirth Sound
        self.set_effect(triggerIds=[5103], visible=True)
        self.create_monster(spawnIds=[30025], animationEffect=False) # 25%

    def on_tick(self) -> trigger_api.Trigger:
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


class Gauge1_Normal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Normal Slime Rebirth Sound
        self.set_effect(triggerIds=[5103], visible=True)
        self.create_monster(spawnIds=[30001], animationEffect=False) # 1%

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return Gauge_SpawnRamdom(self.ctx)
        if self.user_value(key='SpawnHold', value=1):
            return SpawnHold(self.ctx)
        if self.user_value(key='Gauge', value=25):
            return Gauge25_Normal(self.ctx)
        if self.user_value(key='StopSpawn', value=1):
            return Quit(self.ctx)


# 스폰 홀드
class SpawnHold(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 홀더 트리거에서 받는 신호 0이면 스폰 진행 / 1이면 스폰 중지
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnHold', value=0):
            return BackToGaugeState(self.ctx)
        if self.user_value(key='StopSpawn', value=1):
            return Quit(self.ctx)


# 돌연변이 슬라임 랜덤 낮은 확률
class Gauge_SpawnRamdom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=100, desc='Normal'):
            return Spawn_Normal(self.ctx)
        if self.random_condition(rate=5, desc='Eater'):
            return Spawn_Eater(self.ctx)
        """
        if self.random_condition(rate=1, desc='BigMom'):
            return None # Missing State: Spawn_BigMom
        """
        if self.random_condition(rate=10, desc='Runner'):
            return Spawn_Runner(self.ctx)


# 랜덤 스폰 공용
class Spawn_Normal(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return BackToGaugeState(self.ctx)


class Spawn_Eater(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Abnormal Slime Rebirth Sound
        self.set_effect(triggerIds=[5203], visible=True)
        self.create_monster(spawnIds=[31001], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return BackToGaugeState(self.ctx)


class Spawn_Runner(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Abnormal Slime Rebirth Sound
        self.set_effect(triggerIds=[5203], visible=True)
        self.create_monster(spawnIds=[31002], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return BackToGaugeState(self.ctx)


"""
class Spawn_BigMom(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[31003], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return BackToGaugeState(self.ctx)

"""


# 게이지 상태 체크로 돌아가기 공용
class BackToGaugeState(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
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


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[30100,30075,30050,30025,30001,31001,31002,31003])


initial_state = Wait
