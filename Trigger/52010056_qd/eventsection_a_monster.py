""" trigger/52010056_qd/eventsection_a_monster.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2002]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=201, msg='$52010056_QD__EventSection_A_Monster__0$', duration=2800, delay_tick=0)
        self.spawn_monster(spawn_ids=[201], auto_target=True) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[202], auto_target=True) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[203], auto_target=True) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[204], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[205], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[206], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[207], auto_target=True) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[208], auto_target=True) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[209], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[210], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[211], auto_target=True) # 크림슨 스피어: 29000386
        self.spawn_monster(spawn_ids=[212], auto_target=True) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[213], auto_target=True) # 브라운 크림슨: 29000384
        self.spawn_monster(spawn_ids=[214], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[215], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[216], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[217], auto_target=True) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[218], auto_target=True) # 퍼플 크림슨: 29000383
        self.spawn_monster(spawn_ids=[219], auto_target=True) # 화이트 크림슨: 29000385
        self.spawn_monster(spawn_ids=[220], auto_target=True) # 화이트 크림슨: 29000385


initial_state = Idle
