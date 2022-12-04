""" trigger/52010056_qd/eventsection_d.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=2005, spawnIds=[999]):
            return 연출준비(self.ctx)


class 연출준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera_path(pathIds=[4006], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 경비병_외침(self.ctx)


class 경비병_외침(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawnId=999, sequenceName='Attack_01_B')
        self.add_cinematic_talk(npcId=11003816, msg='$52010056_QD__EventSection_D__0$', duration=3727)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3727):
            return 크림슨스피어_출동(self.ctx)

    def on_exit(self):
        self.create_monster(spawnIds=[901], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[902], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[903], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[904], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[905], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[906], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[907], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[908], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[909], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[910], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[911], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[912], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[913], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[914], animationEffect=True) # 크림슨 스피어: 29000386
        self.create_monster(spawnIds=[915], animationEffect=True) # 크림슨 스피어: 29000386
        self.change_monster(removeSpawnId=999, addSpawnId=901)


class 크림슨스피어_출동(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4007], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)
        self.remove_buff(boxId=2001, skillId=70000107)


initial_state = Idle
