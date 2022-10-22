""" trigger/63000050_cs/tria_seige_ready.xml """
from common import *
import state


class start(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[1000], questIds=[20002263], questStates=[3]):
            return 트라이아침공전시작()
        if quest_user_detected(boxIds=[1000], questIds=[20002263], questStates=[2]):
            return 트라이아방공호로()
        if quest_user_detected(boxIds=[1000], questIds=[20002263], questStates=[1]):
            return 트라이아침공전시작()


class 트라이아침공전시작(state.State):
    def on_enter(self):
        move_user(mapId=52000068, portalId=1)


class 트라이아방공호로(state.State):
    def on_enter(self):
        move_user(mapId=52000069, portalId=1)


