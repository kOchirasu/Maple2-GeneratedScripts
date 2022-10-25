""" trigger/52000030_qd/main_w.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101], jobCode=30):
            return 연출시작(self.ctx)


class 연출시작(common.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='Nutaman_intro.swf', movieId=1)
        self.select_camera(triggerId=301, enable=True)
        self.create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 이슈라대사01(self.ctx)


class 이슈라대사01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[603], visible=True)
        self.set_conversation(type=2, spawnId=11000032, script='$52000030_QD__MAIN_W__0$', arg4=4, arg5=0)
        self.set_skip(state=NPC 단체 이동)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4500):
            return NPC 단체 이동(self.ctx)


class NPC 단체 이동(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_1001')
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002')
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1003')
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData_1004')
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_1005')
        self.move_npc(spawnId=1006, patrolName='MS2PatrolData_1006')
        self.move_npc(spawnId=1007, patrolName='MS2PatrolData_1007')
        self.move_npc(spawnId=1008, patrolName='MS2PatrolData_1008')
        self.move_npc(spawnId=1009, patrolName='MS2PatrolData_1009')
        self.move_npc(spawnId=1010, patrolName='MS2PatrolData_1010')
        self.move_npc(spawnId=1011, patrolName='MS2PatrolData_1011')
        self.move_npc(spawnId=1012, patrolName='MS2PatrolData_1001')
        self.move_npc(spawnId=1013, patrolName='MS2PatrolData_1002')
        self.move_npc(spawnId=1014, patrolName='MS2PatrolData_1003')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014]):
            return 전투판으로이동(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014])
        self.create_monster(spawnIds=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,2001,2002], animationEffect=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 전투판으로이동(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=301, enable=False)
        self.move_user(mapId=52000030, portalId=100)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2002]):
            return 차전투2(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[2001])


class 차전투2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2003,2004], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2003]):
            return 이슈라대사02(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[2004])


class 이슈라대사02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001578, script='$52000030_QD__MAIN_W__1$', arg4=2, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 차전투3(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 차전투3(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2005], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2005]):
            return 이슈라대사03(self.ctx)


class 이슈라대사03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(triggerIds=[604], visible=True)
        self.set_conversation(type=2, spawnId=11000032, script='$52000030_QD__MAIN_W__3$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_user(mapId=52000031, portalId=0)
            return 종료(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 종료(common.Trigger):
    pass


initial_state = 대기
