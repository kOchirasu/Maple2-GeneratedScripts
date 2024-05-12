""" trigger/52020026_qd/52020026_main.xml """
import trigger_api


class 감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=1, visible=False, enable=False)
        self.set_portal(portalId=2, visible=False, enable=False)
        self.set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018], visible=False)
        self.set_agent(triggerIds=[9001], visible=True)
        self.set_agent(triggerIds=[9002], visible=True)
        self.set_agent(triggerIds=[9003], visible=True)
        self.set_agent(triggerIds=[9004], visible=True)
        self.set_agent(triggerIds=[9005], visible=True)
        self.set_agent(triggerIds=[9006], visible=True)
        self.set_agent(triggerIds=[9007], visible=True)
        self.set_agent(triggerIds=[9008], visible=True)
        self.set_agent(triggerIds=[9009], visible=True)
        self.set_agent(triggerIds=[9010], visible=True)
        self.set_agent(triggerIds=[9011], visible=True)
        self.set_agent(triggerIds=[9012], visible=True)
        self.set_agent(triggerIds=[9013], visible=True)
        self.set_agent(triggerIds=[9014], visible=True)
        self.set_agent(triggerIds=[9015], visible=True)
        self.set_agent(triggerIds=[9016], visible=True)
        self.set_agent(triggerIds=[9017], visible=True)
        self.set_agent(triggerIds=[9018], visible=True)
        self.set_agent(triggerIds=[9019], visible=True)
        self.set_agent(triggerIds=[9020], visible=True)
        self.set_agent(triggerIds=[9021], visible=True)
        self.set_agent(triggerIds=[9022], visible=True)
        self.set_agent(triggerIds=[9023], visible=True)
        self.set_agent(triggerIds=[9024], visible=True)
        self.set_agent(triggerIds=[9025], visible=True)
        self.set_agent(triggerIds=[9026], visible=True)
        self.set_agent(triggerIds=[9027], visible=True)
        self.set_agent(triggerIds=[9028], visible=True)
        self.set_agent(triggerIds=[9029], visible=True)
        self.set_agent(triggerIds=[9030], visible=True)
        self.set_agent(triggerIds=[9031], visible=True)
        self.set_agent(triggerIds=[9032], visible=True)
        self.set_interact_object(triggerIds=[10001320], state=2)
        self.set_interact_object(triggerIds=[10001321], state=2)
        self.set_interact_object(triggerIds=[10001322], state=2)
        self.set_interact_object(triggerIds=[10001323], state=2)
        self.set_interact_object(triggerIds=[10001324], state=2)
        self.set_interact_object(triggerIds=[10001325], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[901]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 층1(self.ctx)


class 층1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 층레버활성1(self.ctx)


class 층레버활성1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='레버를 작동시켜 계단을 완성하세요.', arg3='5000')
        self.set_interact_object(triggerIds=[10001320], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001320], stateValue=0):
            return 층2(self.ctx)


class 층2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.set_mesh(triggerIds=[1001,1002,1003], visible=True, arg3=0, delay=500, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[102]):
            return 층레버활성2(self.ctx)


class 층레버활성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10001321], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001321], stateValue=0):
            return 층3(self.ctx)


class 층3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.set_mesh(triggerIds=[1004,1005,1006], visible=True, arg3=0, delay=500, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[103,104]):
            return 층레버활성3(self.ctx)


class 층레버활성3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10001322], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001322], stateValue=0):
            return 층4(self.ctx)


class 층4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.create_monster(spawnIds=[106], animationEffect=False)
        self.set_mesh(triggerIds=[1007,1008,1009], visible=True, arg3=0, delay=500, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[105,106]):
            return 층레버활성4(self.ctx)


class 층레버활성4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10001323], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001323], stateValue=0):
            return 층5(self.ctx)


class 층5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.set_mesh(triggerIds=[1010,1011,1012], visible=True, arg3=0, delay=500, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[906]):
            return 층_벽부수기5(self.ctx)


class 층_벽부수기5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(triggerIds=[9001], visible=False)
        self.set_agent(triggerIds=[9002], visible=False)
        self.set_agent(triggerIds=[9003], visible=False)
        self.set_agent(triggerIds=[9004], visible=False)
        self.set_agent(triggerIds=[9005], visible=False)
        self.set_agent(triggerIds=[9006], visible=False)
        self.set_agent(triggerIds=[9007], visible=False)
        self.set_agent(triggerIds=[9008], visible=False)
        self.set_agent(triggerIds=[9009], visible=False)
        self.set_agent(triggerIds=[9010], visible=False)
        self.set_agent(triggerIds=[9011], visible=False)
        self.set_agent(triggerIds=[9012], visible=False)
        self.set_agent(triggerIds=[9013], visible=False)
        self.set_agent(triggerIds=[9014], visible=False)
        self.set_agent(triggerIds=[9015], visible=False)
        self.set_agent(triggerIds=[9016], visible=False)
        self.create_monster(spawnIds=[108], animationEffect=True)
        self.set_skill(triggerIds=[1], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[107,108]):
            return 층레버활성5(self.ctx)


class 층레버활성5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10001324], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001324], stateValue=0):
            return 층6(self.ctx)


class 층6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[109], animationEffect=False)
        self.create_monster(spawnIds=[110], animationEffect=False)
        self.set_mesh(triggerIds=[1013,1014,1015], visible=True, arg3=0, delay=500, scale=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[907]):
            return 층_벽부수기6(self.ctx)


class 층_벽부수기6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(triggerIds=[9017], visible=False)
        self.set_agent(triggerIds=[9018], visible=False)
        self.set_agent(triggerIds=[9019], visible=False)
        self.set_agent(triggerIds=[9020], visible=False)
        self.set_agent(triggerIds=[9021], visible=False)
        self.set_agent(triggerIds=[9022], visible=False)
        self.set_agent(triggerIds=[9023], visible=False)
        self.set_agent(triggerIds=[9024], visible=False)
        self.set_agent(triggerIds=[9025], visible=False)
        self.set_agent(triggerIds=[9026], visible=False)
        self.set_agent(triggerIds=[9027], visible=False)
        self.set_agent(triggerIds=[9028], visible=False)
        self.set_agent(triggerIds=[9029], visible=False)
        self.set_agent(triggerIds=[9030], visible=False)
        self.set_agent(triggerIds=[9031], visible=False)
        self.set_agent(triggerIds=[9032], visible=False)
        self.create_monster(spawnIds=[111], animationEffect=True)
        self.set_skill(triggerIds=[2], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[109,110,111]):
            return 층레버활성6(self.ctx)


class 층레버활성6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10001325], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001325], stateValue=0):
            return 포탈활성화(self.ctx)


class 포탈활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[1016,1017,1018], visible=True, arg3=0, delay=500, scale=3)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 감지
