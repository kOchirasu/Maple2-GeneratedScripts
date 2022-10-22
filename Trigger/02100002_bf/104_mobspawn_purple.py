""" trigger/02100002_bf/104_mobspawn_purple.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='Gauge', value=0) # 탱크 리필 트리거에서 받는 신호
        set_user_value(key='StopSpawn', value=0) # 홀더 트리거에서 받는 신호 0이면 스폰 진행 / 1이면 스폰 중지
        set_user_value(key='SpawnHold', value=0)
        destroy_monster(spawnIds=[40100,40075,40050,40025,40001,41001,41002,41003])
        set_effect(triggerIds=[5104], visible=False) # Normal Slime Rebirth Sound
        set_effect(triggerIds=[5204], visible=False) # Abnormal Slime Rebirth Sound

    def on_tick(self) -> state.State:
        if user_value(key='Gauge', value=100):
            return Gauge100_Normal()


class Gauge100_Normal(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=True) # Normal Slime Rebirth Sound
        create_monster(spawnIds=[40100], arg2=False) # 100%

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Gauge_SpawnRamdom()
        if user_value(key='SpawnHold', value=1):
            return SpawnHold()
        if user_value(key='Gauge', value=75):
            return Gauge75_Normal()
        if user_value(key='StopSpawn', value=1):
            return Quit()


class Gauge75_Normal(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=True) # Normal Slime Rebirth Sound
        create_monster(spawnIds=[40075], arg2=False) # 75%

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Gauge_SpawnRamdom()
        if user_value(key='SpawnHold', value=1):
            return SpawnHold()
        if user_value(key='Gauge', value=100):
            return Gauge100_Normal()
        if user_value(key='Gauge', value=50):
            return Gauge50_Normal()
        if user_value(key='StopSpawn', value=1):
            return Quit()


class Gauge50_Normal(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=True) # Normal Slime Rebirth Sound
        create_monster(spawnIds=[40050], arg2=False) # 50%

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Gauge_SpawnRamdom()
        if user_value(key='SpawnHold', value=1):
            return SpawnHold()
        if user_value(key='Gauge', value=75):
            return Gauge75_Normal()
        if user_value(key='Gauge', value=25):
            return Gauge25_Normal()
        if user_value(key='StopSpawn', value=1):
            return Quit()


class Gauge25_Normal(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=True) # Normal Slime Rebirth Sound
        create_monster(spawnIds=[40025], arg2=False) # 25%

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Gauge_SpawnRamdom()
        if user_value(key='SpawnHold', value=1):
            return SpawnHold()
        if user_value(key='Gauge', value=50):
            return Gauge50_Normal()
        if user_value(key='Gauge', value=1):
            return Gauge1_Normal()
        if user_value(key='StopSpawn', value=1):
            return Quit()


class Gauge1_Normal(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5104], visible=True) # Normal Slime Rebirth Sound
        create_monster(spawnIds=[40001], arg2=False) # 1%

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return Gauge_SpawnRamdom()
        if user_value(key='SpawnHold', value=1):
            return SpawnHold()
        if user_value(key='Gauge', value=25):
            return Gauge25_Normal()
        if user_value(key='StopSpawn', value=1):
            return Quit()


#  스폰 홀드 
class SpawnHold(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='SpawnHold', value=0):
            return BackToGaugeState()
        if user_value(key='StopSpawn', value=1):
            return Quit()


#  돌연변이 슬라임 랜덤 낮은 확률
class Gauge_SpawnRamdom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=100, desc='Normal'):
            return Spawn_Normal()
        if random_condition(rate=5, desc='Eater'):
            return Spawn_Eater()
        if random_condition(rate=10, desc='Runner'):
            return Spawn_Runner()
        """
        <condition name="랜덤조건" arg1="1" desc="BigMom">
            <transition state="Spawn_BigMom" /> 
        </condition>
        """


#  랜덤 스폰 공용 
class Spawn_Normal(state.State):
    def on_tick(self) -> state.State:
        if true():
            return BackToGaugeState()


class Spawn_Eater(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5204], visible=True) # Abnormal Slime Rebirth Sound
        create_monster(spawnIds=[41001], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return BackToGaugeState()


class Spawn_Runner(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5204], visible=True) # Abnormal Slime Rebirth Sound
        create_monster(spawnIds=[41002], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return BackToGaugeState()


#  게이지 상태 체크로 돌아가기 공용 
class BackToGaugeState(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Gauge', value=100):
            return Gauge100_Normal()
        if user_value(key='Gauge', value=75):
            return Gauge75_Normal()
        if user_value(key='Gauge', value=50):
            return Gauge50_Normal()
        if user_value(key='Gauge', value=25):
            return Gauge25_Normal()
        if user_value(key='Gauge', value=1):
            return Gauge1_Normal()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[40100,40075,40050,40025,40001,41001,41002,41003])


