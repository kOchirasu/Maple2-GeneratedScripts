""" trigger/63000050_cs/tria_seige_ready.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[1000], questIds=[20002263], questStates=[3]):
            # [20002263 위기의 트라이아] 진행중 일시
            return 트라이아침공전시작(self.ctx)
        if self.quest_user_detected(boxIds=[1000], questIds=[20002263], questStates=[2]):
            # [20002263 위기의 트라이아] 진행중 일시
            return 트라이아방공호로(self.ctx)
        if self.quest_user_detected(boxIds=[1000], questIds=[20002263], questStates=[1]):
            # [20002263 위기의 트라이아] 진행중 일시
            return 트라이아침공전시작(self.ctx)


class 트라이아침공전시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52000068, portalId=1)


class 트라이아방공호로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52000069, portalId=1)


initial_state = start
