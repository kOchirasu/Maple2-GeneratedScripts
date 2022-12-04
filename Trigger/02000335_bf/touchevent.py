""" trigger/02000335_bf/touchevent.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=702, boxId=1):
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[118,119], animationEffect=False) # 기본 배치 될 몬스터 등장


initial_state = 시작
