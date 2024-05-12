""" trigger/52010056_qd/eventsection_a_monster.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2002]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawnId=201, msg='$52010056_QD__EventSection_A_Monster__0$', duration=2800, delayTick=0)
        self.create_monster(spawnIds=[201], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[202], animationEffect=True) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[203], animationEffect=True) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[204], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[205], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[206], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[207], animationEffect=True) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[208], animationEffect=True) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[209], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[210], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[211], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[212], animationEffect=True) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[213], animationEffect=True) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[214], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[215], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[216], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[217], animationEffect=True) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[218], animationEffect=True) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[219], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[220], animationEffect=True) # 화이트 크림슨: 29000385


initial_state = Idle
