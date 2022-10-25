""" trigger/02000419_bf/main.xml """
import common


class Ready(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6001], visible=False) # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기
        self.set_mesh(triggerIds=[6002], visible=False) # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기
        self.set_mesh(triggerIds=[6003], visible=False) # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기
        self.set_mesh(triggerIds=[6004], visible=False) # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=700, boxId=1):
            return Ready_Idle(self.ctx)


class Ready_Idle(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1, interval=0)


initial_state = Ready
