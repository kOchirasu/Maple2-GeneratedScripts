""" trigger/52010056_qd/eventsection_d_monster.xml """
from common import *
import state


class Idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2003]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[501], arg2=False) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[502], arg2=False) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[503], arg2=False) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[504], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[505], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[506], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[507], arg2=False) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[508], arg2=False) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[509], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[510], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[511], arg2=False) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[512], arg2=False) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[513], arg2=False) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[514], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[515], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[516], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[517], arg2=False) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[518], arg2=False) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[519], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[520], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[521], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[522], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[523], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[524], arg2=False) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[525], arg2=False) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[526], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[527], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[528], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[529], arg2=False) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[530], arg2=False) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[531], arg2=False) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[532], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[533], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[534], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[535], arg2=False) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[536], arg2=False) # 퍼플 크림슨: 29000383
        create_monster(spawnIds=[537], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[538], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[539], arg2=False) # 크림슨 스피어: 29000386
        create_monster(spawnIds=[540], arg2=False) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[541], arg2=False) # 브라운 크림슨: 29000384
        create_monster(spawnIds=[542], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[543], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[544], arg2=False) # 화이트 크림슨: 29000385
        create_monster(spawnIds=[545], arg2=False) # 퍼플 크림슨: 29000383


