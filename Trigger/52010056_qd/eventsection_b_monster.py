""" trigger/52010056_qd/eventsection_b_monster.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2003]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[301], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[302], animationEffect=True) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[303], animationEffect=True) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[304], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[305], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[306], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[307], animationEffect=True) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[308], animationEffect=True) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[309], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[310], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[311], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[312], animationEffect=True) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[313], animationEffect=True) # 브라운 크림슨: 29000384
        self.create_monster(spawnIds=[314], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[315], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[316], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[317], animationEffect=True) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[318], animationEffect=True) # 퍼플 크림슨: 29000383
        self.create_monster(spawnIds=[319], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[320], animationEffect=True) # 화이트 크림슨: 29000385
        self.create_monster(spawnIds=[321], animationEffect=True) # 화이트 크림슨: 29000385


initial_state = Idle
