""" trigger/52010056_qd/eventsection_a_monster.xml """
from common import *
import state


class Idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2002]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=201, msg='$52010056_QD__EventSection_A_Monster__0$', duration=2800, delayTick=0)
        create_monster(spawnIds=[201], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[202], arg2=True) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[203], arg2=True) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[204], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[205], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[206], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[207], arg2=True) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[208], arg2=True) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[209], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[210], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[211], arg2=True) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[212], arg2=True) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[213], arg2=True) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[214], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[215], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[216], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[217], arg2=True) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[218], arg2=True) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[219], arg2=True) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[220], arg2=True) # 화이트 크림슨: 29000385


