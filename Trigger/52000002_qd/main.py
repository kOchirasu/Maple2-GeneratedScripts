""" trigger/52000002_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010])
        destroy_monster(spawnIds=[2099])
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3007,3008,3009,3010,3011,3012,3013], visible=True, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000606], state=2)
        set_interact_object(triggerIds=[10000607,10000608,10000609,10000610,10000611], state=2)
        set_interact_object(triggerIds=[10000612,10000613,10000614,10000615,10000616], state=2)
        create_monster(spawnIds=[1099], arg2=False)
        create_monster(spawnIds=[1101], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 던전시작()
        if not user_detected(boxIds=[101]):
            return 종료()


class 던전시작(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 차목표1()
        if not user_detected(boxIds=[101]):
            return 종료()


class 차목표1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3, script='$52000002_QD__MAIN__0$')
        set_timer(timerId='5', seconds=5)
        set_skip(state=오브젝트생성)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 오브젝트생성()
        if not user_detected(boxIds=[101]):
            return 종료()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 오브젝트생성(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000607,10000608,10000609,10000610,10000611], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000607,10000608,10000609,10000610,10000611], arg2=0):
            return 단계준비2()
        if not user_detected(boxIds=[101]):
            return 종료()


class 단계준비2(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        show_guide_summary(entityId=25200202, textId=25200202)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 레버대기()
        if not user_detected(boxIds=[101]):
            return 종료()


class 레버대기(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=25200202)
        set_interact_object(triggerIds=[10000606], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000606], arg2=0):
            return 다리생성()
        if not user_detected(boxIds=[101]):
            return 종료()


class 다리생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006], visible=True, arg3=0, arg4=300, arg5=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 단계시작2()
        if not user_detected(boxIds=[101]):
            return 종료()


class 단계시작2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3, script='$52000002_QD__MAIN__2$')
        set_timer(timerId='5', seconds=5)
        set_skip(state=양생성)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 양생성()
        if not user_detected(boxIds=[101]):
            return 종료()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 양생성(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000612,10000613,10000614,10000615,10000616], state=1)
        create_monster(spawnIds=[2001,2002,2003,2004,2005], arg2=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000612,10000613,10000614,10000615,10000616], arg2=2):
            return 단계준비3()
        if not user_detected(boxIds=[101]):
            return 종료()


class 단계준비3(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        show_guide_summary(entityId=25200202, textId=25200202)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 단계대기3()
        if not user_detected(boxIds=[101]):
            return 종료()


class 단계대기3(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=25200202)
        set_mesh(triggerIds=[3007,3008,3009,3010,3011,3012,3013], visible=False, arg3=0, arg4=200, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[106]):
            return 단계시작3()
        if not user_detected(boxIds=[101]):
            return 종료()


class 단계시작3(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3, script='$52000002_QD__MAIN__4$')
        set_timer(timerId='5', seconds=5)
        set_skip(state=늑대생성)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 늑대생성()
        if not user_detected(boxIds=[101]):
            return 종료()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 늑대생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2006,2007,2008,2009,2010], arg2=False)
        create_monster(spawnIds=[2099], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2099]):
            return 성공대기()
        if not user_detected(boxIds=[101]):
            return 종료()


class 성공대기(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[101]):
            return 종료()
        if time_expired(timerId='2'):
            return 미션성공()


class 미션성공(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1102], arg2=False)
        move_npc(spawnId=1102, patrolName='MS2PatrolData_1102')
        set_event_ui(type=7, arg2='$52000002_QD__MAIN__5$', arg3='3000', arg4='0')
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 포털생성()
        if not user_detected(boxIds=[101]):
            return 종료()


class 포털생성(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1102, script='$52000002_QD__MAIN__6$', arg4=6)
        set_timer(timerId='30', seconds=30)
        show_guide_summary(entityId=25200203, textId=25200203)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            move_user(mapId=2000002, portalId=30, boxId=101)
            return 종료()
        if not user_detected(boxIds=[101]):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=25200203)
        hide_guide_summary(entityId=25200202)
        destroy_monster(spawnIds=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010])
        destroy_monster(spawnIds=[2099])
        destroy_monster(spawnIds=[1099])
        destroy_monster(spawnIds=[1101])
        destroy_monster(spawnIds=[1102])
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000606], state=2)
        set_interact_object(triggerIds=[10000607,10000608,10000609,10000610,10000611], state=2)
        set_interact_object(triggerIds=[10000612,10000613,10000614,10000615,10000616], state=2)

    def on_tick(self) -> state.State:
        if true():
            return 대기()


