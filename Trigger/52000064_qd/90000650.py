""" trigger/52000064_qd/90000650.xml """
import trigger_api


class 시작대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], visible=True, arg3=0, delay=0, scale=0)
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.create_monster(spawnIds=[1001,1002,1003], animationEffect=False)
        self.create_monster(spawnIds=[1101,1102,1103], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 아이템생성(self.ctx)


class 아이템생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_item(spawnIds=[9000,9001,9002,9003,9004,9005,9006,9007,9008,9009,9010])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 완료대기(self.ctx)


class 완료대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[102]):
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_enter(self):
        self.create_item(spawnIds=[9011,9012,9013,9014,9015])
        self.set_event_ui(type=7, arg3='3000', arg4='0')
        self.set_achievement(triggerId=199, type='trigger', achieve='ArrivedFlyBalloon')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[90000650], questStates=[3]):
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기
