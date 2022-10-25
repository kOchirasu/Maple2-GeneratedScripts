""" trigger/84000006_wd/84000006_wd_fireworks.xml """
import common


# 불꽃놀이 발사 준비
class Staging(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Fireworks', value=1):
            return Volley(self.ctx)


# UV받아 불꽃놀이 연출
class Volley(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[3000], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return None


initial_state = Staging
