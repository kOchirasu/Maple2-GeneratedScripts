""" trigger/52000055_qd/jordy.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[60100120,60100121,60100122,60100123,60100124,60100125,60100126,60100127,60100128,60100129,60100130], questStates=[1]):
            return jordy(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[60100235,60100236,60100237,60100238,60100239,60100240], questStates=[2]):
            return jordy(self.ctx)


# 조디 스폰
class jordy(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103], animationEffect=False) # 조디


initial_state = Ready
