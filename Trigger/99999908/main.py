""" trigger/99999908/main.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.create_monster(spawnIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117], animationEffect=True)
        self.set_ambient_light(primary=[1,1,1])
        self.set_directional_light(diffuseColor=[1,1,1], specularColor=[0,0,0])
        self.set_timer(timerId='240', seconds=240, startDelay=1, interval=1)


class switch(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5500):
            return 시작(self.ctx)


initial_state = 시작
