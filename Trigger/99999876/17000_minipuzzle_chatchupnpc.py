""" trigger/99999876/17000_minipuzzle_chatchupnpc.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='ChangeNpc', value=0) # 17101 몬스터 AI에서 받는 신호
        self.destroy_monster(spawnIds=[17101,17102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return SettingDelay(self.ctx)


class SettingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Setting(self.ctx)


class Setting(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[17101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ChangeNpc', value=1):
            return ChatchUpNpc(self.ctx)


class ChatchUpNpc(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30, startDelay=1, interval=0, vOffset=0) # UI 표시 안함 / NPC AI에서 스폰시킨 InteractObject 의 LifeTime
        self.change_monster(removeSpawnId=17101, addSpawnId=17102) # 동일 맵에 스포너가 있으면 대상 npc의 위치를 보정해서 교체되는 npc를 스폰 시켜줌

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return ChatchUpNpc_Quit(self.ctx)


class ChatchUpNpc_Quit(trigger_api.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')
        self.destroy_monster(spawnIds=[17101,17102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Wait(self.ctx)


initial_state = Wait
