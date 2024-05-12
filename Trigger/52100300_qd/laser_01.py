""" trigger/52100300_qd/laser_01.xml """
import trigger_api


class 레이저_01_생성(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Laser', value=1):
            self.spawn_monster(spawn_ids=[902], auto_target=True) # 몬스터 등장
            return 레이저_01_소멸(self.ctx)


class 레이저_01_소멸(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102,103]):
            self.destroy_monster(spawn_ids=[902])
            return 레이저_02_생성(self.ctx)


class 레이저_02_생성(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=711, min_users='1'):
            self.spawn_monster(spawn_ids=[711], auto_target=True) # 몬스터 등장
            return 레이저_02_소멸(self.ctx)


class 레이저_02_소멸(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=712, min_users='1'):
            self.destroy_monster(spawn_ids=[711])
            return 레이저_03_생성(self.ctx)


class 레이저_03_생성(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=712, min_users='1'):
            self.spawn_monster(spawn_ids=[712], auto_target=True) # 몬스터 등장
            return 레이저_03_소멸(self.ctx)


class 레이저_03_소멸(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=713, min_users='1'):
            self.destroy_monster(spawn_ids=[712])
            self.spawn_monster(spawn_ids=[713], auto_target=True) # 몬스터 등장
            return 레이저_04(self.ctx)


class 레이저_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Laser', value=0):
            self.destroy_monster(spawn_ids=[713])


initial_state = 레이저_01_생성
