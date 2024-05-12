""" trigger/52010056_qd/eventsection_b_monster.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2003]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[301], auto_target=True) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[302], auto_target=True) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[303], auto_target=True) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[304], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[305], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[306], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[307], auto_target=True) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[308], auto_target=True) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[309], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[310], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[311], auto_target=True) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[312], auto_target=True) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[313], auto_target=True) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[314], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[315], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[316], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[317], auto_target=True) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[318], auto_target=True) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[319], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[320], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[321], auto_target=True) # 화이트 크림슨: 29000385


initial_state = Idle
