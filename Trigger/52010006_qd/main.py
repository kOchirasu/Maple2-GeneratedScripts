""" trigger/52010006_qd/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1001], animationEffect=False)
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3002,3003,3004,3005], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3006,3007,3008,3009], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 미카등장(self.ctx)


class 미카등장(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 미카대사01(self.ctx)


class 미카대사01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001285, script='$52010006_QD__MAIN__0$', arg4=4)
        self.set_scene_skip(state=미카대사02_0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 미카대사02(self.ctx)


class 미카대사02_0(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 미카대사02(self.ctx)


class 미카대사02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001285, script='$52010006_QD__MAIN__10$', arg4=4)
        self.set_scene_skip(state=몬스터생성_0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            return 몬스터생성(self.ctx)


class 몬스터생성_0(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 몬스터생성(self.ctx)


class 몬스터생성(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_1001_A')
        self.create_monster(spawnIds=[2001], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 미카이동(self.ctx)


class 미카이동(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_1001_B')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=104, spawnIds=[1001]):
            return 미카교체(self.ctx)


class 미카교체(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1001])
        self.create_monster(spawnIds=[1007], animationEffect=False)
        self.move_npc(spawnId=1007, patrolName='MS2PatrolData_1001_C')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[1007]):
            return 사슬(self.ctx)


class 사슬(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1002], animationEffect=False)
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 카보대사01(self.ctx)


class 카보대사01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001319, script='$52010006_QD__MAIN__1$', arg4=5)
        self.set_scene_skip(state=카보대사02_0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 카보대사02(self.ctx)


class 카보대사02_0(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 카보대사02(self.ctx)


class 카보대사02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001319, script='$52010006_QD__MAIN__2$', arg4=5)
        self.set_scene_skip(state=미카친구들소환_0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 미카친구들소환(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 미카친구들소환_0(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 미카친구들소환(self.ctx)


class 미카친구들소환(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.create_monster(spawnIds=[1003,1004,1005], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=200):
            return 스타츠대사01(self.ctx)


class 스타츠대사01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_A')
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_A')
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_A')
        self.set_conversation(type=2, spawnId=11001292, script='$52010006_QD__MAIN__3$', arg4=2)
        self.set_scene_skip(state=둔바대사01_0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 둔바대사01(self.ctx)


class 둔바대사01_0(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 둔바대사01(self.ctx)


class 둔바대사01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001217, script='$52010006_QD__MAIN__11$', arg4=2)
        self.set_scene_skip(state=타라대사01_0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 타라대사01(self.ctx)


class 타라대사01_0(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 타라대사01(self.ctx)


class 타라대사01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001218, script='$52010006_QD__MAIN__12$', arg4=3)
        self.set_scene_skip(state=카보대사03_0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카보대사03(self.ctx)


class 카보대사03_0(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 카보대사03(self.ctx)


class 카보대사03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002_A')
        self.set_conversation(type=2, spawnId=11001319, script='$52010006_QD__MAIN__4$', arg4=5)
        self.set_scene_skip(state=카보소환_0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 카보소환(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 카보소환_0(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 카보소환(self.ctx)


class 카보소환(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.destroy_monster(spawnIds=[1002])
        self.create_monster(spawnIds=[2002], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 카보대사04(self.ctx)


class 카보대사04(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2002])
        self.create_monster(spawnIds=[1006], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001319, script='$52010006_QD__MAIN__5$', arg4=5)
        self.set_scene_skip(state=카보대사05_0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 카보대사05(self.ctx)


class 카보대사05_0(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 카보대사05(self.ctx)


class 카보대사05(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001319, script='$52010006_QD__MAIN__6$', arg4=5)
        self.move_npc(spawnId=1006, patrolName='MS2PatrolData_1002_B')
        self.set_scene_skip(state=사슬해제_0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            self.destroy_monster(spawnIds=[1006])
            return 사슬해제(self.ctx)


class 사슬해제_0(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 사슬해제(self.ctx)


class 사슬해제(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1003_B')
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData_1004_B')
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_1005_B')
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=3)
        self.set_mesh(triggerIds=[3002,3003,3004,3005], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3006,3007,3008,3009], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            self.move_npc(spawnId=1007, patrolName='MS2PatrolData_1001_D')
            return 스타츠대사02(self.ctx)


class 스타츠대사02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001292, script='$52010006_QD__MAIN__7$', arg4=5)
        self.set_scene_skip(state=스타츠대사03_0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 스타츠대사03(self.ctx)


class 스타츠대사03_0(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스타츠대사03(self.ctx)


class 스타츠대사03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001292, script='$52010006_QD__MAIN__8$', arg4=5)
        self.set_scene_skip(state=스타츠대사04_0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 스타츠대사04(self.ctx)


class 스타츠대사04_0(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 스타츠대사04(self.ctx)


class 스타츠대사04(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001292, script='$52010006_QD__MAIN__9$', arg4=5)
        self.set_scene_skip(state=업적이벤트발생_0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            return 업적이벤트발생(self.ctx)


class 업적이벤트발생_0(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 업적이벤트발생(self.ctx)


class 업적이벤트발생(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_achievement(triggerId=103, type='trigger', achieve='RescueMika')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 강제이동(self.ctx)


class 강제이동(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2010030, portalId=4, boxId=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
