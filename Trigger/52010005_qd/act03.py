""" trigger/52010005_qd/act03.xml """
import trigger_api


class 퀘스트조건03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000872], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[10002822], questStates=[1]):
            # 3rd Quest
            return Q3_딜레이01(self.ctx)


class Q3_딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='100', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='100'):
            return Q3_미카등장01(self.ctx)


# 3rd Quest
class Q3_미카등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='20', seconds=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[601], animationEffect=False)
        self.move_npc(spawnId=601, patrolName='MS2PatrolData_6010')
        self.destroy_monster(spawnIds=[401])
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[501], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='20'):
            return Q3_미카연출01(self.ctx)


class Q3_미카연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='21', seconds=5)
        self.select_camera_path(pathIds=[2001,2002], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='21'):
            return Q3_미카연출02(self.ctx)


class Q3_미카연출02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=8003, spawnIds=[601]):
            return Q3_미카연출03(self.ctx)


class Q3_미카연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='22', seconds=4)
        self.move_npc(spawnId=601, patrolName='MS2PatrolData_6011')
        self.select_camera_path(pathIds=[2002,2001], returnView=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='22'):
            return Q3_미카연출04(self.ctx)


class Q3_미카연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000872], state=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000872], stateValue=0):
            return Q3_영상재생(self.ctx)


class Q3_영상재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='MemoryofDragon.swf', movieId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return Q3_시네마틱연출01(self.ctx)


class Q3_시네마틱연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='25', seconds=4)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001285, script='$52010005_QD__ACT03__0$', arg4=4)
        self.set_skip(state=Q3_시네마틱연출02대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='25'):
            return Q3_시네마틱연출02대기(self.ctx)


class Q3_시네마틱연출02대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Q3_시네마틱연출02(self.ctx)


class Q3_시네마틱연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=4001, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Q3_시네마틱연출03(self.ctx)


class Q3_시네마틱연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='26', seconds=3)
        self.set_conversation(type=2, spawnId=11001316, script='$52010005_QD__ACT03__1$', arg4=3)
        self.set_skip(state=Q3_시네마틱연출04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='26'):
            return Q3_시네마틱연출04(self.ctx)


class Q3_시네마틱연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return Q3_시네마틱연출05(self.ctx)


class Q3_시네마틱연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='27', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='27'):
            return Q3_미카퇴장01(self.ctx)


class Q3_미카퇴장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='30', seconds=2)
        self.move_npc(spawnId=601, patrolName='MS2PatrolData_6013')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='30'):
            return Q3_미카퇴장02(self.ctx)


class Q3_미카퇴장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='31', seconds=3)
        self.set_conversation(type=2, spawnId=11001285, script='$52010005_QD__ACT03__2$', arg4=3)
        self.set_skip(state=Q3_미카퇴장03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='31'):
            return Q3_미카퇴장03(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Q3_미카퇴장03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=601, patrolName='MS2PatrolData_6014')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=8010, spawnIds=[601]):
            return Q3_미카퇴장04(self.ctx)


class Q3_미카퇴장04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[601])
        self.set_timer(timerId='40', seconds=1)
        self.select_camera(triggerId=4001, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='40'):
            return Q3_업적발생(self.ctx)


class Q3_업적발생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(triggerId=9001, type='trigger', achieve='Intothememory')
        self.destroy_monster(spawnIds=[501])
        self.create_monster(spawnIds=[502], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[10002823], questStates=[2]):
            # 3rd Quest
            return Q3_유저퇴장01(self.ctx)


class Q3_유저퇴장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='41', seconds=2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='41'):
            return Q3_유저퇴장02(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Q3_유저퇴장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='42', seconds=4)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001316, script='$52010005_QD__ACT03__3$', arg4=4)
        self.set_skip(state=Q3_유저퇴장03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='42'):
            return Q3_유저퇴장03(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Q3_유저퇴장03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(mapId=2010026, portalId=3, boxId=9000)


initial_state = 퀘스트조건03
