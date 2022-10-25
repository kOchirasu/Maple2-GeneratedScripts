""" trigger/63000050_cs/tria_seige_ready.xml """
import common


class start(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[1000], questIds=[20002263], questStates=[3]):
            return 트라이아침공전시작(self.ctx)
        if self.quest_user_detected(boxIds=[1000], questIds=[20002263], questStates=[2]):
            return 트라이아방공호로(self.ctx)
        if self.quest_user_detected(boxIds=[1000], questIds=[20002263], questStates=[1]):
            return 트라이아침공전시작(self.ctx)


class 트라이아침공전시작(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000068, portalId=1)


class 트라이아방공호로(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000069, portalId=1)


initial_state = start
