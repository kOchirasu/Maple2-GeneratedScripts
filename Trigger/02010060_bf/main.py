""" trigger/02010060_bf/main.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6001], visible=False) # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기, 남쪽 넓게 설정
        self.set_mesh(triggerIds=[6002], visible=False) # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기, 10시쪽 끊어진 다리 지점
        self.set_mesh(triggerIds=[6003], visible=False) # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기, 2시쪽 끊어진 다리 지점

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=700, boxId=1):
            return Ready_Idle(self.ctx)


class Ready_Idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1, interval=0)


initial_state = Ready
