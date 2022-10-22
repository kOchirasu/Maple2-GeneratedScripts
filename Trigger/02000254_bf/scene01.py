""" trigger/02000254_bf/scene01.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101])
        create_monster(spawnIds=[107])
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3002], visible=True, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[601], visible=False) # 칼 음성
        set_effect(triggerIds=[602], visible=False) # 벨라 음성
        set_effect(triggerIds=[603], visible=False) # 벨라 음성
        set_effect(triggerIds=[604], visible=False) # 칼 음성
        set_effect(triggerIds=[605], visible=False) # 칼 음성
        set_effect(triggerIds=[606], visible=False) # 벨라 음성
        set_effect(triggerIds=[607], visible=False) # 벨라 음성
        set_effect(triggerIds=[608], visible=False) # 벨라 음성
        set_effect(triggerIds=[401], visible=False)
        set_effect(triggerIds=[402], visible=False)
        set_effect(triggerIds=[403], visible=False)
        set_effect(triggerIds=[404], visible=False)
        set_effect(triggerIds=[405], visible=False)
        set_effect(triggerIds=[406], visible=False)
        set_effect(triggerIds=[407], visible=False)
        set_effect(triggerIds=[408], visible=False)
        set_effect(triggerIds=[409], visible=False)
        set_effect(triggerIds=[410], visible=False)
        set_effect(triggerIds=[411], visible=False)
        set_effect(triggerIds=[412], visible=False)
        set_effect(triggerIds=[413], visible=False)
        set_effect(triggerIds=[414], visible=False)
        set_effect(triggerIds=[415], visible=False)
        set_effect(triggerIds=[416], visible=False)
        set_effect(triggerIds=[417], visible=False)
        set_effect(triggerIds=[418], visible=False)
        set_effect(triggerIds=[419], visible=False)
        set_effect(triggerIds=[420], visible=False)
        set_effect(triggerIds=[421], visible=False)
        set_effect(triggerIds=[422], visible=False)
        set_effect(triggerIds=[423], visible=False)
        set_effect(triggerIds=[424], visible=False)
        set_effect(triggerIds=[425], visible=False)
        set_effect(triggerIds=[426], visible=False)
        set_effect(triggerIds=[427], visible=False)
        set_effect(triggerIds=[428], visible=False)
        set_effect(triggerIds=[429], visible=False)
        set_effect(triggerIds=[430], visible=False)
        set_effect(triggerIds=[431], visible=False)
        set_effect(triggerIds=[432], visible=False)
        set_effect(triggerIds=[433], visible=False)
        set_effect(triggerIds=[434], visible=False)
        set_effect(triggerIds=[435], visible=False)
        set_effect(triggerIds=[436], visible=False)
        set_effect(triggerIds=[437], visible=False)
        set_effect(triggerIds=[438], visible=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=901, boxId=1):
            return 연출시작딜레이()


class 연출시작딜레이(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        set_scene_skip(state=스킵벨라이동딜레이, arg2='nextState')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대화시작()


class 대화시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[401], visible=False)
        set_timer(timerId='1', seconds=6)
        # <action name="이펙트를설정한다" arg1="601" arg2="1"/>
        add_cinematic_talk(npcId=11000074, illustId='Karl_closeEye', msg='$02000254_BF__SCENE01__0$', duration=6000, align='center')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사1()


class 벨라대사1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=4)
        # <action name="이펙트를설정한다" arg1="602" arg2="1"/>
        set_conversation(type=2, spawnId=11000057, script='$02000254_BF__SCENE01__1$', arg4=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사2()


class 벨라대사2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=7)
        # <action name="이펙트를설정한다" arg1="603" arg2="1"/>
        set_conversation(type=2, spawnId=11000057, script='$02000254_BF__SCENE01__2$', arg4=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 칼대사1()


class 칼대사1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5)
        # <action name="이펙트를설정한다" arg1="604" arg2="1"/>
        add_cinematic_talk(npcId=11000074, illustId='Karl_closeEye', msg='$02000254_BF__SCENE01__3$', duration=5000, align='center')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 칼대사2()


class 칼대사2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5)
        # <action name="이펙트를설정한다" arg1="605" arg2="1"/>
        add_cinematic_talk(npcId=11000074, illustId='Karl_closeEye', msg='$02000254_BF__SCENE01__4$', duration=5000, align='center')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사3()


class 벨라대사3(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=6)
        # <action name="이펙트를설정한다" arg1="606" arg2="1"/>
        set_conversation(type=2, spawnId=11000057, script='$02000254_BF__SCENE01__5$', arg4=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사4()


class 벨라대사4(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=10)
        # <action name="이펙트를설정한다" arg1="607" arg2="1"/>
        set_conversation(type=2, spawnId=11000057, script='$02000254_BF__SCENE01__6$', arg4=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라이동()


class 벨라이동딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라이동()


class 벨라이동(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0)
        move_npc(spawnId=101, patrolName='MS2PatrolData_1')

    def on_tick(self) -> state.State:
        if true():
            return 카메라원위치()


class 카메라원위치(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        select_camera_path(pathIds=[301], returnView=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 카메라원위치2()


class 카메라원위치2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if count_users(boxId=902, boxId=1):
            return 쿠당탕()


class 쿠당탕(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102])
        set_effect(triggerIds=[402], visible=True)
        set_effect(triggerIds=[403], visible=True)
        set_effect(triggerIds=[404], visible=True)
        set_effect(triggerIds=[405], visible=True)
        set_effect(triggerIds=[406], visible=True)
        set_effect(triggerIds=[407], visible=True)
        set_effect(triggerIds=[408], visible=True)
        set_effect(triggerIds=[409], visible=True)
        set_effect(triggerIds=[410], visible=True)
        set_effect(triggerIds=[411], visible=True)
        set_effect(triggerIds=[412], visible=True)
        set_effect(triggerIds=[413], visible=True)
        set_effect(triggerIds=[414], visible=True)
        set_effect(triggerIds=[415], visible=True)
        set_effect(triggerIds=[416], visible=True)
        set_effect(triggerIds=[417], visible=True)
        set_effect(triggerIds=[418], visible=True)
        set_effect(triggerIds=[419], visible=True)
        set_effect(triggerIds=[420], visible=True)
        set_effect(triggerIds=[421], visible=True)
        set_effect(triggerIds=[422], visible=True)
        set_effect(triggerIds=[423], visible=True)
        set_effect(triggerIds=[424], visible=True)
        set_effect(triggerIds=[425], visible=True)
        set_effect(triggerIds=[426], visible=True)
        set_effect(triggerIds=[427], visible=True)
        set_effect(triggerIds=[428], visible=True)
        set_effect(triggerIds=[429], visible=True)
        set_effect(triggerIds=[430], visible=True)
        set_effect(triggerIds=[431], visible=True)
        set_effect(triggerIds=[432], visible=True)
        set_effect(triggerIds=[433], visible=True)
        set_effect(triggerIds=[434], visible=True)
        set_effect(triggerIds=[435], visible=True)
        set_effect(triggerIds=[436], visible=True)
        set_effect(triggerIds=[437], visible=True)
        set_effect(triggerIds=[438], visible=True)

    def on_tick(self) -> state.State:
        if true(arg1=True):
            return 벨라대사5()


class 스킵벨라이동딜레이(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_timer(timerId='1', seconds=1)
        select_camera_path(pathIds=[301], returnView=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킵벨라이동()


class 스킵벨라이동(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0)
        move_npc(spawnId=101, patrolName='MS2PatrolData_1')

    def on_tick(self) -> state.State:
        if true():
            return 스킵카메라원위치()


class 스킵카메라원위치(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=902, boxId=1):
            return 스킵쿠당탕()


class 스킵쿠당탕(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102])
        set_effect(triggerIds=[402], visible=True)
        set_effect(triggerIds=[403], visible=True)
        set_effect(triggerIds=[404], visible=True)
        set_effect(triggerIds=[405], visible=True)
        set_effect(triggerIds=[406], visible=True)
        set_effect(triggerIds=[407], visible=True)
        set_effect(triggerIds=[408], visible=True)
        set_effect(triggerIds=[409], visible=True)
        set_effect(triggerIds=[410], visible=True)
        set_effect(triggerIds=[411], visible=True)
        set_effect(triggerIds=[412], visible=True)
        set_effect(triggerIds=[413], visible=True)
        set_effect(triggerIds=[414], visible=True)
        set_effect(triggerIds=[415], visible=True)
        set_effect(triggerIds=[416], visible=True)
        set_effect(triggerIds=[417], visible=True)
        set_effect(triggerIds=[418], visible=True)
        set_effect(triggerIds=[419], visible=True)
        set_effect(triggerIds=[420], visible=True)
        set_effect(triggerIds=[421], visible=True)
        set_effect(triggerIds=[422], visible=True)
        set_effect(triggerIds=[423], visible=True)
        set_effect(triggerIds=[424], visible=True)
        set_effect(triggerIds=[425], visible=True)
        set_effect(triggerIds=[426], visible=True)
        set_effect(triggerIds=[427], visible=True)
        set_effect(triggerIds=[428], visible=True)
        set_effect(triggerIds=[429], visible=True)
        set_effect(triggerIds=[430], visible=True)
        set_effect(triggerIds=[431], visible=True)
        set_effect(triggerIds=[432], visible=True)
        set_effect(triggerIds=[433], visible=True)
        set_effect(triggerIds=[434], visible=True)
        set_effect(triggerIds=[435], visible=True)
        set_effect(triggerIds=[436], visible=True)
        set_effect(triggerIds=[437], visible=True)
        set_effect(triggerIds=[438], visible=True)

    def on_tick(self) -> state.State:
        if true(arg1=True):
            return 벨라대사5딜레이()


class 벨라대사5딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 벨라대사5()


class 벨라대사5(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        set_scene_skip(state=벨라이동2, arg2='nextState')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_timer(timerId='1', seconds=6)
        set_conversation(type=2, spawnId=11000057, script='$02000254_BF__SCENE01__7$', arg4=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사6()


class 벨라대사6(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=4)
        # <action name="이펙트를설정한다" arg1="608" arg2="1"/>
        set_conversation(type=2, spawnId=11000057, script='$02000254_BF__SCENE01__8$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라이동2()


class 벨라이동2(state.State):
    def on_enter(self):
        set_scene_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_timer(timerId='1', seconds=4)
        move_npc(spawnId=102, patrolName='MS2PatrolData_2')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 이펙트1()


class 이펙트1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_effect(triggerIds=[401], visible=True)
        destroy_monster(spawnIds=[102])

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라몬스터소환()


class 벨라몬스터소환(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)
        select_camera(triggerId=303, enable=True)
        create_monster(spawnIds=[106])
        create_monster(spawnIds=[103])

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 끝()


class 끝(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        select_camera_path(pathIds=[303], returnView=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 끝2()


class 끝2(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=False)
        select_camera(triggerId=303, enable=False)
        set_mesh(triggerIds=[3002], visible=False, arg3=0, arg4=0, arg5=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


