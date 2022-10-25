""" trigger/52000073_qd/losteve.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9900]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[50001683], questStates=[3]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[50001683], questStates=[2]):
            return 대원있음(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[50001683], questStates=[1]):
            return 대원있음(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[50001682], questStates=[3]):
            return 대원있음(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[50001682], questStates=[2]):
            return 대원있음(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[50001682], questStates=[1]):
            return 대원있음(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[50001681], questStates=[3]):
            return 대원있음(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[50001681], questStates=[2]):
            return 대원등장(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[50001681], questStates=[1]):
            return 대원등장(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[50001680], questStates=[3]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[50001680], questStates=[2]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[50001680], questStates=[1]):
            return 기본상태(self.ctx)


class 기본상태(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[401])

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9900]):
            return 퀘스트조건체크(self.ctx)


class 대원있음(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[401], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return None # Missing State: 종료


class 대원등장(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[401]) # 윈 스틸던의 시체

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대원대사(self.ctx)


class 대원대사(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_pcTurn')
        self.select_camera_path(pathIds=[8003,8004], returnView=False)
        self.move_npc(spawnId=401, patrolName='MS2PatrolData_2001')
        self.add_cinematic_talk(npcId=11003446, illustId='0', msg='$52000073_QD__LOSTEVE__0$', duration=4000, align='right') # 호르헤 대사
        self.face_emotion(spawnId=101, emotionName='Upset')
        self.set_scene_skip(state=연출종료, action='exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 카트반대사(self.ctx)


class 카트반대사(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11000044, illustId='0', msg='$52000073_QD__LOSTEVE__1$', duration=4000, align='right') # 호르헤 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 연출종료(self.ctx)


class 연출종료(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return None # Missing State: 종료


initial_state = 대기
