""" trigger/84000006_wd/84000006_wd_fireworks.xml """
import trigger_api


# 불꽃놀이 발사 준비
class Staging(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Fireworks', value=1):
            return Volley(self.ctx)


# UV받아 불꽃놀이 연출
class Volley(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[3000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            pass


initial_state = Staging
