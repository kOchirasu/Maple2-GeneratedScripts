""" trigger/99999876/17000_minipuzzle_chatchupnpc.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='ChangeNpc', value=0) # 17101 몬스터 AI에서 받는 신호
        destroy_monster(spawnIds=[17101,17102])

    def on_tick(self) -> state.State:
        if check_user():
            return SettingDelay()


class SettingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Setting()


class Setting(state.State):
    def on_enter(self):
        create_monster(spawnIds=[17101], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='ChangeNpc', value=1):
            return ChatchUpNpc()


class ChatchUpNpc(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=True, display=False, arg5=0) # UI 표시 안함 / NPC AI에서 스폰시킨 InteractObject 의 LifeTime
        change_monster(removeSpawnId=17101, addSpawnId=17102) # 동일 맵에 스포너가 있으면 대상 npc의 위치를 보정해서 교체되는 npc를 스폰 시켜줌

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return ChatchUpNpc_Quit()


class ChatchUpNpc_Quit(state.State):
    def on_enter(self):
        reset_timer(timerId='1')
        destroy_monster(spawnIds=[17101,17102])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Wait()


