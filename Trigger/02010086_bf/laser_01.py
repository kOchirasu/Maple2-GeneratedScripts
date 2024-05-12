""" trigger/02010086_bf/laser_01.xml """
import trigger_api


class 레이저_01_소멸(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=712, minUsers='1'):
            return 레이저_02(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawnIds=[999])


class 레이저_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=707, minUsers='1'):
            return 레이저_02_생성(self.ctx)


class 레이저_02_생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[998], animationEffect=True) # 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=708, minUsers='1'):
            return 레이저_03_생성(self.ctx)


class 레이저_03_생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[995], animationEffect=True) # 몬스터 등장


initial_state = 레이저_01_소멸
