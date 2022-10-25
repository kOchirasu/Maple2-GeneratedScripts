""" trigger/52010056_qd/eventsection_d_monster.xml """
import common


class Idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[2003]):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[501], animationEffect=False) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[502], animationEffect=False) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[503], animationEffect=False) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[504], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[505], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[506], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[507], animationEffect=False) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[508], animationEffect=False) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[509], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[510], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[511], animationEffect=False) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[512], animationEffect=False) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[513], animationEffect=False) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[514], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[515], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[516], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[517], animationEffect=False) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[518], animationEffect=False) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[519], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[520], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[521], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[522], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[523], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[524], animationEffect=False) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[525], animationEffect=False) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[526], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[527], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[528], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[529], animationEffect=False) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[530], animationEffect=False) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[531], animationEffect=False) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[532], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[533], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[534], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[535], animationEffect=False) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[536], animationEffect=False) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[537], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[538], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[539], animationEffect=False) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[540], animationEffect=False) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[541], animationEffect=False) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[542], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[543], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[544], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[545], animationEffect=False) # 퍼플 크림슨: 29000383


initial_state = Idle
