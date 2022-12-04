""" trigger/52000020_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[60001022], questStates=[1]):
            return camera_01(self.ctx)


class camera_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return monster_spawn_01(self.ctx)


class monster_spawn_01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[111,112,113,114], animationEffect=True) # 1차 스폰
        self.set_conversation(type=1, spawnId=111, script='$52000020_QD__MAIN__2$', arg4=5)
        self.set_conversation(type=1, spawnId=112, script='$52000020_QD__MAIN__3$', arg4=5)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return battle_01(self.ctx)
        if self.monster_dead(boxIds=[111,112,113,114]):
            return camera_02(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class battle_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[111,112,113,114]):
            return camera_02(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=110)


class camera_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timerId='1', seconds=1)
        self.select_camera_path(pathIds=[8003,8004], returnView=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return monster_spawn_02(self.ctx)


class monster_spawn_02(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[121,122,123,124,125,126], animationEffect=True) # 2차 스폰
        self.set_conversation(type=1, spawnId=121, script='$52000020_QD__MAIN__4$', arg4=5)
        self.set_conversation(type=1, spawnId=124, script='$52000020_QD__MAIN__5$', arg4=5)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return battle_02(self.ctx)
        if self.monster_dead(boxIds=[121,122,123,124,125,126]):
            return camera_03(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class battle_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[121,122,123,124,125,126]):
            return camera_03(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=110)


class camera_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timerId='1', seconds=1)
        self.select_camera_path(pathIds=[8005,8006], returnView=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return monster_spawn_03(self.ctx)


class monster_spawn_03(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[131,132,133,134,135,136], animationEffect=True) # 3차 스폰
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return battle_03(self.ctx)
        if self.monster_dead(boxIds=[131,132,133,134,135,136]):
            return complete(self.ctx)

    def on_exit(self):
        self.set_conversation(type=1, spawnId=131, script='$52000020_QD__MAIN__1$', arg4=5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class battle_03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[131,132,133,134,135,136]):
            return complete(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=110)


class complete(trigger_api.Trigger):
    pass


initial_state = idle
