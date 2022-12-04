""" trigger/02010055_bf/scene02.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 룸체크(self.ctx)


class 룸체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return 난이도체크(self.ctx)
        if not self.is_dungeon_room():
            return 퀘스트던전대기(self.ctx)


class 난이도체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_level(level=2):
            return 레이드대기(self.ctx)
        if self.dungeon_level(level=3):
            return None # Missing State: 카오스레이드


class 퀘스트던전대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2299]):
            return 영상준비(self.ctx)


class 레이드대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2099]):
            return 영상준비(self.ctx)


class 카오스레이드대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2199]):
            return 영상준비(self.ctx)


class 연출시작딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=302, enable=True)
        self.create_monster(spawnIds=[1002,1003,1004], animationEffect=False)
        self.set_skip(state=NPC이동)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 스타츠대사01(self.ctx)


class 스타츠대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip(state=NPC이동)
        self.set_conversation(type=2, spawnId=11001292, script='$02010055_BF__SCENE02__0$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 타라대사01(self.ctx)


class 타라대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip(state=NPC이동)
        self.set_conversation(type=2, spawnId=11001218, script='$02010055_BF__SCENE02__1$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 스타츠대사02(self.ctx)


class 스타츠대사02(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip(state=NPC이동)
        self.set_conversation(type=2, spawnId=11001292, script='$02010055_BF__SCENE02__2$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=302, enable=False)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_A')
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_A')
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            self.destroy_monster(spawnIds=[1002,1003,1004])
            return 종료(self.ctx)


class 영상준비(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_timer(timerId='21', seconds=10)
        self.select_camera_path(pathIds=[601,602], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='21'):
            return 영상재생(self.ctx)


class 영상재생(trigger_api.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='common\KarKarBossEvent.usm', movieId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
