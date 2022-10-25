""" trigger/02000356_bf/scene01.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201])
        self.set_effect(triggerIds=[401], visible=False)
        self.set_effect(triggerIds=[601], visible=False) # 벨라 음성
        self.set_effect(triggerIds=[602], visible=False) # 벨라 음성
        self.set_effect(triggerIds=[603], visible=False) # 벨라 음성
        self.set_effect(triggerIds=[604], visible=False) # 벨라 음성
        self.set_effect(triggerIds=[605], visible=False) # 벨라 음성
        self.set_effect(triggerIds=[606], visible=False) # 레논 음성
        self.set_effect(triggerIds=[607], visible=False) # 알론 음성
        self.set_effect(triggerIds=[608], visible=False) # 알론 음성
        self.set_effect(triggerIds=[609], visible=False) # 알론 음성

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SetSkillA', value=1):
            return 연출시작딜레이(self.ctx)


class 연출시작딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 연출시작(self.ctx)


class 연출시작(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 데보라크대사(self.ctx)


class 데보라크대사(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.set_conversation(type=2, spawnId=23000007, script='$02000213_BF__SCENE01__0$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 레논등장(self.ctx)


class 레논등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[203])
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 레논대사1(self.ctx)


class 레논대사1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.set_effect(triggerIds=[606], visible=True) # 2.33
        self.set_conversation(type=2, spawnId=11000064, script='$02000213_BF__SCENE01__1$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라등장(self.ctx)


class 벨라등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[202])
        self.set_effect(triggerIds=[401], visible=True)
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사1(self.ctx)


class 벨라대사1(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[401], visible=False)
        self.set_timer(timerId='1', seconds=4)
        self.set_effect(triggerIds=[601], visible=True) # 3.40
        self.set_conversation(type=2, spawnId=11000057, script='$02000213_BF__SCENE01__2$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사2(self.ctx)


class 벨라대사2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)
        self.set_effect(triggerIds=[602], visible=True) # 2.54
        self.set_conversation(type=2, spawnId=11000057, script='$02000213_BF__SCENE01__3$', arg4=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 알론등장(self.ctx)


class 알론등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[204])
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 알론대사1(self.ctx)


class 알론대사1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=4)
        self.set_effect(triggerIds=[607], visible=True) # 3.68
        self.set_conversation(type=2, spawnId=11000076, script='$02000213_BF__SCENE01__4$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사3(self.ctx)


class 벨라대사3(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=4)
        self.set_effect(triggerIds=[603], visible=True) # 4.10
        self.set_conversation(type=2, spawnId=11000057, script='$02000213_BF__SCENE01__5$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사4(self.ctx)


class 벨라대사4(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=4)
        self.set_effect(triggerIds=[604], visible=True) # 3.38
        self.set_conversation(type=2, spawnId=11000057, script='$02000213_BF__SCENE01__6$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사5(self.ctx)


class 벨라대사5(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.set_effect(triggerIds=[605], visible=True) # 2.10
        self.set_conversation(type=2, spawnId=11000057, script='$02000213_BF__SCENE01__7$', arg4=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라사라짐이펙트(self.ctx)


class 벨라사라짐이펙트(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_effect(triggerIds=[407], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라사라짐(self.ctx)


class 벨라사라짐(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera_path(pathIds=[302], returnView=True)
        self.destroy_monster(spawnIds=[202])
        self.destroy_monster(spawnIds=[203])
        self.destroy_monster(spawnIds=[204])
        self.create_monster(spawnIds=[205])

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 알론대사2(self.ctx)


class 알론대사2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=4)
        self.set_effect(triggerIds=[608], visible=True) # 3.27
        self.set_conversation(type=1, spawnId=205, script='$02000213_BF__SCENE01__8$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 알론대사3(self.ctx)


class 알론대사3(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=4)
        self.set_effect(triggerIds=[609], visible=True) # 3.33
        self.set_conversation(type=1, spawnId=205, script='$02000213_BF__SCENE01__9$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 연출끝(self.ctx)


class 연출끝(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=301, enable=False)
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 끝(self.ctx)


class 끝(common.Trigger):
    pass


initial_state = 시작대기중
