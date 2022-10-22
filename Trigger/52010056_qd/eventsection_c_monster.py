""" trigger/52010056_qd/eventsection_c_monster.xml """
from common import *
import state


class Idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2003]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[401], arg2=False) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[402], arg2=False) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[403], arg2=False) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[404], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[405], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[406], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[407], arg2=False) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[408], arg2=False) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[409], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[410], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[411], arg2=False) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[412], arg2=False) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[413], arg2=False) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[414], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[415], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[416], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[417], arg2=False) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[418], arg2=False) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[419], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[420], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[421], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[422], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[423], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[424], arg2=False) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[425], arg2=False) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[426], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[427], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[428], arg2=False) # 화이트 크림슨: 29000385


