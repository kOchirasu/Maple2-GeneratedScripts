""" trigger/52010056_qd/eventsection_c_monster.xml """
import common


class Idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[2003]):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[401], animationEffect=False) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[402], animationEffect=False) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[403], animationEffect=False) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[404], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[405], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[406], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[407], animationEffect=False) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[408], animationEffect=False) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[409], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[410], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[411], animationEffect=False) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[412], animationEffect=False) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[413], animationEffect=False) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[414], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[415], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[416], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[417], animationEffect=False) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[418], animationEffect=False) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[419], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[420], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[421], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[422], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[423], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[424], animationEffect=False) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[425], animationEffect=False) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[426], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[427], animationEffect=False) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[428], animationEffect=False) # 화이트 크림슨: 29000385


initial_state = Idle
