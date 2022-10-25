""" trigger/99999927/main.xml """
import common


# 플레이어 감지
class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return ready(self.ctx)


class ready(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[701], skillId=99910120, level=1, isPlayer=False, isSkillSet=False)
        self.set_gravity(gravity=-25)
        self.create_monster(spawnIds=[201], animationEffect=True)


initial_state = idle
