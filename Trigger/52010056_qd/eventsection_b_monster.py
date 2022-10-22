""" trigger/52010056_qd/eventsection_b_monster.xml """
from common import *
import state


class Idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2003]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[301], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[302], arg2=True) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[303], arg2=True) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[304], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[305], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[306], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[307], arg2=True) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[308], arg2=True) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[309], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[310], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[311], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[312], arg2=True) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[313], arg2=True) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[314], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[315], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[316], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[317], arg2=True) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[318], arg2=True) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[319], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[320], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[321], arg2=True) # 화이트 크림슨: 29000385


