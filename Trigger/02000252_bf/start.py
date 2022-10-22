""" trigger/02000252_bf/start.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[151,152,153,154,155,156], visible=True)
        set_effect(triggerIds=[601], visible=False) # 벨라 음성
        set_effect(triggerIds=[602], visible=False) # 벨라 음성
        set_effect(triggerIds=[603], visible=False) # 벨라 음성
        set_effect(triggerIds=[8001], visible=False)
        set_effect(triggerIds=[8002], visible=False)
        set_effect(triggerIds=[8003], visible=False)
        set_effect(triggerIds=[8004], visible=False)
        set_effect(triggerIds=[8005], visible=False)
        set_effect(triggerIds=[8006], visible=False)
        set_effect(triggerIds=[8007], visible=False)
        set_effect(triggerIds=[8008], visible=False)
        set_effect(triggerIds=[8009], visible=False)
        set_effect(triggerIds=[8010], visible=False)
        set_effect(triggerIds=[8011], visible=False)
        set_effect(triggerIds=[8012], visible=False)

    def on_tick(self) -> state.State:
        if check_user():
            return 로딩딜레이()


class 로딩딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        hide_guide_summary(entityId=20002521)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라소환()

state.DungeonStart = DungeonStart


class 연출해제(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라소환()


class 벨라소환(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[8801,8802], returnView=False)
        create_monster(spawnIds=[1001])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 벨라대사()


class 벨라대사(state.State):
    def on_enter(self):
        set_scene_skip(state=벨라스킬딜레이, arg2='nextState')
        set_skip(state=벨라스킬딜레이)
        set_timer(timerId='1', seconds=6) # action name="이펙트를설정한다" arg1="601" arg2="1"/
        set_conversation(type=2, spawnId=11000057, script='$02000252_BF__START__4$', arg4=3) # action name="스킵을설정한다" arg1="벨라스킬딜레이" /

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사2()


class 벨라대사2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=8)
        # <action name="이펙트를설정한다" arg1="602" arg2="1"/>
        set_conversation(type=2, spawnId=11000057, script='$02000252_BF__START__5$', arg4=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사3()


class 벨라대사3(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=4)
        set_scene_skip()
        # <action name="이펙트를설정한다" arg1="603" arg2="1"/>
        set_conversation(type=2, spawnId=11000057, script='$02000252_BF__START__6$', arg4=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6243):
            return 벨라스킬딜레이()


class 벨라스킬딜레이(state.State):
    def on_enter(self):
        move_npc(spawnId=1001, patrolName='MS2PatrolData_1')
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 예고이펙트()


class 예고이펙트(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8804], returnView=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_achievement(triggerId=999, type='trigger', achieve='Bellafirst')
        set_effect(triggerIds=[8001], visible=True)
        set_effect(triggerIds=[8002], visible=True)
        set_effect(triggerIds=[8003], visible=True)
        set_effect(triggerIds=[8004], visible=True)
        set_effect(triggerIds=[8005], visible=True)
        set_effect(triggerIds=[8006], visible=True)
        set_effect(triggerIds=[8007], visible=True)
        set_effect(triggerIds=[8008], visible=True)
        set_effect(triggerIds=[8009], visible=True)
        set_effect(triggerIds=[8010], visible=True)
        set_effect(triggerIds=[8011], visible=True)
        set_effect(triggerIds=[8012], visible=True)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 스킬시작대기()


class 스킬시작대기(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002522, textId=20002522)
        set_mesh(triggerIds=[151,152,153,154,155,156], visible=False)
        create_monster(spawnIds=[1051], arg2=False)
        create_monster(spawnIds=[1052], arg2=False)
        create_monster(spawnIds=[1053], arg2=False)
        create_monster(spawnIds=[1054], arg2=False)
        create_monster(spawnIds=[1055], arg2=False)
        create_monster(spawnIds=[1056], arg2=False)
        create_monster(spawnIds=[1057], arg2=False)
        create_monster(spawnIds=[1058], arg2=False)
        create_monster(spawnIds=[1059], arg2=False)
        create_monster(spawnIds=[1060], arg2=False)
        create_monster(spawnIds=[1061], arg2=False)
        create_monster(spawnIds=[1062], arg2=False)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            destroy_monster(spawnIds=[1001])
            return 스킬시작대기2()


class 스킬시작대기2(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_effect(triggerIds=[8001], visible=False)
        set_effect(triggerIds=[8002], visible=False)
        set_effect(triggerIds=[8003], visible=False)
        set_effect(triggerIds=[8004], visible=False)
        set_effect(triggerIds=[8005], visible=False)
        set_effect(triggerIds=[8006], visible=False)
        set_effect(triggerIds=[8007], visible=False)
        set_effect(triggerIds=[8008], visible=False)
        set_effect(triggerIds=[8009], visible=False)
        set_effect(triggerIds=[8010], visible=False)
        set_effect(triggerIds=[8011], visible=False)
        set_effect(triggerIds=[8012], visible=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 스킬To08()


class 스킬To08(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[515], isEnable=True)
        set_skill(triggerIds=[516], isEnable=True)
        set_skill(triggerIds=[517], isEnable=True)
        set_skill(triggerIds=[518], isEnable=True)
        set_skill(triggerIds=[519], isEnable=True)
        set_skill(triggerIds=[520], isEnable=True)
        set_skill(triggerIds=[521], isEnable=True)
        set_skill(triggerIds=[522], isEnable=True)
        set_skill(triggerIds=[523], isEnable=True)
        set_skill(triggerIds=[524], isEnable=True)
        set_skill(triggerIds=[525], isEnable=True)
        set_skill(triggerIds=[526], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬To07대기()


class 스킬To07대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[515], isEnable=False)
        set_skill(triggerIds=[516], isEnable=False)
        set_skill(triggerIds=[517], isEnable=False)
        set_skill(triggerIds=[518], isEnable=False)
        set_skill(triggerIds=[519], isEnable=False)
        set_skill(triggerIds=[520], isEnable=False)
        set_skill(triggerIds=[521], isEnable=False)
        set_skill(triggerIds=[522], isEnable=False)
        set_skill(triggerIds=[523], isEnable=False)
        set_skill(triggerIds=[524], isEnable=False)
        set_skill(triggerIds=[525], isEnable=False)
        set_skill(triggerIds=[526], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬To07()


class 스킬To07(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[564], isEnable=True)
        set_skill(triggerIds=[517], isEnable=True)
        set_skill(triggerIds=[518], isEnable=True)
        set_skill(triggerIds=[519], isEnable=True)
        set_skill(triggerIds=[520], isEnable=True)
        set_skill(triggerIds=[521], isEnable=True)
        set_skill(triggerIds=[522], isEnable=True)
        set_skill(triggerIds=[523], isEnable=True)
        set_skill(triggerIds=[524], isEnable=True)
        set_skill(triggerIds=[525], isEnable=True)
        set_skill(triggerIds=[526], isEnable=True)
        set_skill(triggerIds=[527], isEnable=True)
        set_skill(triggerIds=[528], isEnable=True)
        set_skill(triggerIds=[529], isEnable=True)
        set_skill(triggerIds=[530], isEnable=True)
        set_skill(triggerIds=[531], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬To06대기()


class 스킬To06대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[564], isEnable=False)
        set_skill(triggerIds=[517], isEnable=False)
        set_skill(triggerIds=[518], isEnable=False)
        set_skill(triggerIds=[519], isEnable=False)
        set_skill(triggerIds=[520], isEnable=False)
        set_skill(triggerIds=[521], isEnable=False)
        set_skill(triggerIds=[522], isEnable=False)
        set_skill(triggerIds=[523], isEnable=False)
        set_skill(triggerIds=[524], isEnable=False)
        set_skill(triggerIds=[525], isEnable=False)
        set_skill(triggerIds=[526], isEnable=False)
        set_skill(triggerIds=[527], isEnable=False)
        set_skill(triggerIds=[528], isEnable=False)
        set_skill(triggerIds=[529], isEnable=False)
        set_skill(triggerIds=[530], isEnable=False)
        set_skill(triggerIds=[531], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬To06()


class 스킬To06(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[565], isEnable=True)
        set_skill(triggerIds=[564], isEnable=True)
        set_skill(triggerIds=[522], isEnable=True)
        set_skill(triggerIds=[523], isEnable=True)
        set_skill(triggerIds=[524], isEnable=True)
        set_skill(triggerIds=[525], isEnable=True)
        set_skill(triggerIds=[526], isEnable=True)
        set_skill(triggerIds=[527], isEnable=True)
        set_skill(triggerIds=[528], isEnable=True)
        set_skill(triggerIds=[529], isEnable=True)
        set_skill(triggerIds=[530], isEnable=True)
        set_skill(triggerIds=[531], isEnable=True)
        set_skill(triggerIds=[532], isEnable=True)
        set_skill(triggerIds=[533], isEnable=True)
        set_skill(triggerIds=[534], isEnable=True)
        set_skill(triggerIds=[535], isEnable=True)
        set_skill(triggerIds=[536], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬To05대기()


class 스킬To05대기(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002522)
        set_skill(triggerIds=[565], isEnable=False)
        set_skill(triggerIds=[564], isEnable=False)
        set_skill(triggerIds=[522], isEnable=False)
        set_skill(triggerIds=[523], isEnable=False)
        set_skill(triggerIds=[524], isEnable=False)
        set_skill(triggerIds=[525], isEnable=False)
        set_skill(triggerIds=[526], isEnable=False)
        set_skill(triggerIds=[527], isEnable=False)
        set_skill(triggerIds=[528], isEnable=False)
        set_skill(triggerIds=[529], isEnable=False)
        set_skill(triggerIds=[530], isEnable=False)
        set_skill(triggerIds=[531], isEnable=False)
        set_skill(triggerIds=[532], isEnable=False)
        set_skill(triggerIds=[533], isEnable=False)
        set_skill(triggerIds=[534], isEnable=False)
        set_skill(triggerIds=[535], isEnable=False)
        set_skill(triggerIds=[536], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬To05()


class 스킬To05(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[566], isEnable=True)
        set_skill(triggerIds=[567], isEnable=True)
        set_skill(triggerIds=[568], isEnable=True)
        set_skill(triggerIds=[565], isEnable=True)
        set_skill(triggerIds=[564], isEnable=True)
        set_skill(triggerIds=[527], isEnable=True)
        set_skill(triggerIds=[528], isEnable=True)
        set_skill(triggerIds=[529], isEnable=True)
        set_skill(triggerIds=[530], isEnable=True)
        set_skill(triggerIds=[531], isEnable=True)
        set_skill(triggerIds=[532], isEnable=True)
        set_skill(triggerIds=[533], isEnable=True)
        set_skill(triggerIds=[534], isEnable=True)
        set_skill(triggerIds=[535], isEnable=True)
        set_skill(triggerIds=[536], isEnable=True)
        set_skill(triggerIds=[537], isEnable=True)
        set_skill(triggerIds=[538], isEnable=True)
        set_skill(triggerIds=[539], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬To04대기()


class 스킬To04대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[566], isEnable=False)
        set_skill(triggerIds=[567], isEnable=False)
        set_skill(triggerIds=[568], isEnable=False)
        set_skill(triggerIds=[565], isEnable=False)
        set_skill(triggerIds=[564], isEnable=False)
        set_skill(triggerIds=[527], isEnable=False)
        set_skill(triggerIds=[528], isEnable=False)
        set_skill(triggerIds=[529], isEnable=False)
        set_skill(triggerIds=[530], isEnable=False)
        set_skill(triggerIds=[531], isEnable=False)
        set_skill(triggerIds=[532], isEnable=False)
        set_skill(triggerIds=[533], isEnable=False)
        set_skill(triggerIds=[534], isEnable=False)
        set_skill(triggerIds=[535], isEnable=False)
        set_skill(triggerIds=[536], isEnable=False)
        set_skill(triggerIds=[537], isEnable=False)
        set_skill(triggerIds=[538], isEnable=False)
        set_skill(triggerIds=[539], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬To04()


class 스킬To04(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[566], isEnable=False)
        set_skill(triggerIds=[567], isEnable=False)
        set_skill(triggerIds=[568], isEnable=False)
        set_skill(triggerIds=[565], isEnable=True)
        set_skill(triggerIds=[532], isEnable=True)
        set_skill(triggerIds=[533], isEnable=True)
        set_skill(triggerIds=[534], isEnable=True)
        set_skill(triggerIds=[535], isEnable=True)
        set_skill(triggerIds=[536], isEnable=True)
        set_skill(triggerIds=[537], isEnable=True)
        set_skill(triggerIds=[538], isEnable=True)
        set_skill(triggerIds=[539], isEnable=True)
        set_skill(triggerIds=[540], isEnable=True)
        set_skill(triggerIds=[541], isEnable=True)
        set_skill(triggerIds=[542], isEnable=True)
        set_skill(triggerIds=[543], isEnable=True)
        set_skill(triggerIds=[544], isEnable=True)
        set_skill(triggerIds=[545], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬To03대기()


class 스킬To03대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[566], isEnable=False)
        set_skill(triggerIds=[567], isEnable=False)
        set_skill(triggerIds=[568], isEnable=False)
        set_skill(triggerIds=[565], isEnable=False)
        set_skill(triggerIds=[532], isEnable=False)
        set_skill(triggerIds=[533], isEnable=False)
        set_skill(triggerIds=[534], isEnable=False)
        set_skill(triggerIds=[535], isEnable=False)
        set_skill(triggerIds=[536], isEnable=False)
        set_skill(triggerIds=[537], isEnable=False)
        set_skill(triggerIds=[538], isEnable=False)
        set_skill(triggerIds=[539], isEnable=False)
        set_skill(triggerIds=[540], isEnable=False)
        set_skill(triggerIds=[541], isEnable=False)
        set_skill(triggerIds=[542], isEnable=False)
        set_skill(triggerIds=[543], isEnable=False)
        set_skill(triggerIds=[544], isEnable=False)
        set_skill(triggerIds=[545], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬To03()


class 스킬To03(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[566], isEnable=True)
        set_skill(triggerIds=[567], isEnable=True)
        set_skill(triggerIds=[568], isEnable=True)
        set_skill(triggerIds=[537], isEnable=True)
        set_skill(triggerIds=[538], isEnable=True)
        set_skill(triggerIds=[539], isEnable=True)
        set_skill(triggerIds=[540], isEnable=True)
        set_skill(triggerIds=[541], isEnable=True)
        set_skill(triggerIds=[542], isEnable=True)
        set_skill(triggerIds=[543], isEnable=True)
        set_skill(triggerIds=[544], isEnable=True)
        set_skill(triggerIds=[545], isEnable=True)
        set_skill(triggerIds=[546], isEnable=True)
        set_skill(triggerIds=[547], isEnable=True)
        set_skill(triggerIds=[548], isEnable=True)
        set_skill(triggerIds=[549], isEnable=True)
        set_skill(triggerIds=[550], isEnable=True)
        set_skill(triggerIds=[551], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬To02대기()


class 스킬To02대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[566], isEnable=False)
        set_skill(triggerIds=[567], isEnable=False)
        set_skill(triggerIds=[568], isEnable=False)
        set_skill(triggerIds=[537], isEnable=False)
        set_skill(triggerIds=[538], isEnable=False)
        set_skill(triggerIds=[539], isEnable=False)
        set_skill(triggerIds=[540], isEnable=False)
        set_skill(triggerIds=[541], isEnable=False)
        set_skill(triggerIds=[542], isEnable=False)
        set_skill(triggerIds=[543], isEnable=False)
        set_skill(triggerIds=[544], isEnable=False)
        set_skill(triggerIds=[545], isEnable=False)
        set_skill(triggerIds=[546], isEnable=False)
        set_skill(triggerIds=[547], isEnable=False)
        set_skill(triggerIds=[548], isEnable=False)
        set_skill(triggerIds=[549], isEnable=False)
        set_skill(triggerIds=[550], isEnable=False)
        set_skill(triggerIds=[551], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬To02()


class 스킬To02(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[540], isEnable=True)
        set_skill(triggerIds=[541], isEnable=True)
        set_skill(triggerIds=[542], isEnable=True)
        set_skill(triggerIds=[543], isEnable=True)
        set_skill(triggerIds=[544], isEnable=True)
        set_skill(triggerIds=[545], isEnable=True)
        set_skill(triggerIds=[546], isEnable=True)
        set_skill(triggerIds=[547], isEnable=True)
        set_skill(triggerIds=[548], isEnable=True)
        set_skill(triggerIds=[549], isEnable=True)
        set_skill(triggerIds=[550], isEnable=True)
        set_skill(triggerIds=[551], isEnable=True)
        set_skill(triggerIds=[552], isEnable=True)
        set_skill(triggerIds=[553], isEnable=True)
        set_skill(triggerIds=[554], isEnable=True)
        set_skill(triggerIds=[555], isEnable=True)
        set_skill(triggerIds=[556], isEnable=True)
        set_skill(triggerIds=[557], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬To01대기()


class 스킬To01대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[540], isEnable=False)
        set_skill(triggerIds=[541], isEnable=False)
        set_skill(triggerIds=[542], isEnable=False)
        set_skill(triggerIds=[543], isEnable=False)
        set_skill(triggerIds=[544], isEnable=False)
        set_skill(triggerIds=[545], isEnable=False)
        set_skill(triggerIds=[546], isEnable=False)
        set_skill(triggerIds=[547], isEnable=False)
        set_skill(triggerIds=[548], isEnable=False)
        set_skill(triggerIds=[549], isEnable=False)
        set_skill(triggerIds=[550], isEnable=False)
        set_skill(triggerIds=[551], isEnable=False)
        set_skill(triggerIds=[552], isEnable=False)
        set_skill(triggerIds=[553], isEnable=False)
        set_skill(triggerIds=[554], isEnable=False)
        set_skill(triggerIds=[555], isEnable=False)
        set_skill(triggerIds=[556], isEnable=False)
        set_skill(triggerIds=[557], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬To01()


class 스킬To01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[546], isEnable=True)
        set_skill(triggerIds=[547], isEnable=True)
        set_skill(triggerIds=[548], isEnable=True)
        set_skill(triggerIds=[549], isEnable=True)
        set_skill(triggerIds=[550], isEnable=True)
        set_skill(triggerIds=[551], isEnable=True)
        set_skill(triggerIds=[552], isEnable=True)
        set_skill(triggerIds=[553], isEnable=True)
        set_skill(triggerIds=[554], isEnable=True)
        set_skill(triggerIds=[555], isEnable=True)
        set_skill(triggerIds=[556], isEnable=True)
        set_skill(triggerIds=[557], isEnable=True)
        set_skill(triggerIds=[558], isEnable=True)
        set_skill(triggerIds=[559], isEnable=True)
        set_skill(triggerIds=[560], isEnable=True)
        set_skill(triggerIds=[561], isEnable=True)
        set_skill(triggerIds=[562], isEnable=True)
        set_skill(triggerIds=[563], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬00대기()


class 스킬00대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[546], isEnable=False)
        set_skill(triggerIds=[547], isEnable=False)
        set_skill(triggerIds=[548], isEnable=False)
        set_skill(triggerIds=[549], isEnable=False)
        set_skill(triggerIds=[550], isEnable=False)
        set_skill(triggerIds=[551], isEnable=False)
        set_skill(triggerIds=[552], isEnable=False)
        set_skill(triggerIds=[553], isEnable=False)
        set_skill(triggerIds=[554], isEnable=False)
        set_skill(triggerIds=[555], isEnable=False)
        set_skill(triggerIds=[556], isEnable=False)
        set_skill(triggerIds=[557], isEnable=False)
        set_skill(triggerIds=[558], isEnable=False)
        set_skill(triggerIds=[559], isEnable=False)
        set_skill(triggerIds=[560], isEnable=False)
        set_skill(triggerIds=[561], isEnable=False)
        set_skill(triggerIds=[562], isEnable=False)
        set_skill(triggerIds=[563], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬00()


class 스킬00(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[552], isEnable=True)
        set_skill(triggerIds=[553], isEnable=True)
        set_skill(triggerIds=[554], isEnable=True)
        set_skill(triggerIds=[555], isEnable=True)
        set_skill(triggerIds=[556], isEnable=True)
        set_skill(triggerIds=[557], isEnable=True)
        set_skill(triggerIds=[558], isEnable=True)
        set_skill(triggerIds=[559], isEnable=True)
        set_skill(triggerIds=[560], isEnable=True)
        set_skill(triggerIds=[561], isEnable=True)
        set_skill(triggerIds=[562], isEnable=True)
        set_skill(triggerIds=[563], isEnable=True)
        set_skill(triggerIds=[301], isEnable=True)
        set_skill(triggerIds=[302], isEnable=True)
        set_skill(triggerIds=[303], isEnable=True)
        set_skill(triggerIds=[304], isEnable=True)
        set_skill(triggerIds=[305], isEnable=True)
        set_skill(triggerIds=[306], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬0.5대기()


class 스킬0.5대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[552], isEnable=False)
        set_skill(triggerIds=[553], isEnable=False)
        set_skill(triggerIds=[554], isEnable=False)
        set_skill(triggerIds=[555], isEnable=False)
        set_skill(triggerIds=[556], isEnable=False)
        set_skill(triggerIds=[557], isEnable=False)
        set_skill(triggerIds=[558], isEnable=False)
        set_skill(triggerIds=[559], isEnable=False)
        set_skill(triggerIds=[560], isEnable=False)
        set_skill(triggerIds=[561], isEnable=False)
        set_skill(triggerIds=[562], isEnable=False)
        set_skill(triggerIds=[563], isEnable=False)
        set_skill(triggerIds=[301], isEnable=False)
        set_skill(triggerIds=[302], isEnable=False)
        set_skill(triggerIds=[303], isEnable=False)
        set_skill(triggerIds=[304], isEnable=False)
        set_skill(triggerIds=[305], isEnable=False)
        set_skill(triggerIds=[306], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬0.5()


class 스킬0.5(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[558], isEnable=True)
        set_skill(triggerIds=[559], isEnable=True)
        set_skill(triggerIds=[560], isEnable=True)
        set_skill(triggerIds=[561], isEnable=True)
        set_skill(triggerIds=[562], isEnable=True)
        set_skill(triggerIds=[563], isEnable=True)
        set_skill(triggerIds=[301], isEnable=True)
        set_skill(triggerIds=[302], isEnable=True)
        set_skill(triggerIds=[303], isEnable=True)
        set_skill(triggerIds=[304], isEnable=True)
        set_skill(triggerIds=[305], isEnable=True)
        set_skill(triggerIds=[306], isEnable=True)
        set_skill(triggerIds=[307], isEnable=True)
        set_skill(triggerIds=[308], isEnable=True)
        set_skill(triggerIds=[309], isEnable=True)
        set_skill(triggerIds=[310], isEnable=True)
        set_skill(triggerIds=[311], isEnable=True)
        set_skill(triggerIds=[312], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬01대기()


class 스킬01대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[558], isEnable=False)
        set_skill(triggerIds=[559], isEnable=False)
        set_skill(triggerIds=[560], isEnable=False)
        set_skill(triggerIds=[561], isEnable=False)
        set_skill(triggerIds=[562], isEnable=False)
        set_skill(triggerIds=[563], isEnable=False)
        set_skill(triggerIds=[301], isEnable=False)
        set_skill(triggerIds=[302], isEnable=False)
        set_skill(triggerIds=[303], isEnable=False)
        set_skill(triggerIds=[304], isEnable=False)
        set_skill(triggerIds=[305], isEnable=False)
        set_skill(triggerIds=[306], isEnable=False)
        set_skill(triggerIds=[307], isEnable=False)
        set_skill(triggerIds=[308], isEnable=False)
        set_skill(triggerIds=[309], isEnable=False)
        set_skill(triggerIds=[310], isEnable=False)
        set_skill(triggerIds=[311], isEnable=False)
        set_skill(triggerIds=[312], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬01()


class 스킬01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[301], isEnable=True)
        set_skill(triggerIds=[302], isEnable=True)
        set_skill(triggerIds=[303], isEnable=True)
        set_skill(triggerIds=[304], isEnable=True)
        set_skill(triggerIds=[305], isEnable=True)
        set_skill(triggerIds=[306], isEnable=True)
        set_skill(triggerIds=[307], isEnable=True)
        set_skill(triggerIds=[308], isEnable=True)
        set_skill(triggerIds=[309], isEnable=True)
        set_skill(triggerIds=[310], isEnable=True)
        set_skill(triggerIds=[311], isEnable=True)
        set_skill(triggerIds=[312], isEnable=True)
        set_skill(triggerIds=[313], isEnable=True)
        set_skill(triggerIds=[314], isEnable=True)
        set_skill(triggerIds=[315], isEnable=True)
        set_skill(triggerIds=[316], isEnable=True)
        set_skill(triggerIds=[317], isEnable=True)
        set_skill(triggerIds=[318], isEnable=True)
        set_skill(triggerIds=[319], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬02대기()


class 스킬02대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[301], isEnable=False)
        set_skill(triggerIds=[302], isEnable=False)
        set_skill(triggerIds=[303], isEnable=False)
        set_skill(triggerIds=[304], isEnable=False)
        set_skill(triggerIds=[305], isEnable=False)
        set_skill(triggerIds=[306], isEnable=False)
        set_skill(triggerIds=[307], isEnable=False)
        set_skill(triggerIds=[308], isEnable=False)
        set_skill(triggerIds=[309], isEnable=False)
        set_skill(triggerIds=[310], isEnable=False)
        set_skill(triggerIds=[311], isEnable=False)
        set_skill(triggerIds=[312], isEnable=False)
        set_skill(triggerIds=[313], isEnable=False)
        set_skill(triggerIds=[314], isEnable=False)
        set_skill(triggerIds=[315], isEnable=False)
        set_skill(triggerIds=[316], isEnable=False)
        set_skill(triggerIds=[317], isEnable=False)
        set_skill(triggerIds=[318], isEnable=False)
        set_skill(triggerIds=[319], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬02()


class 스킬02(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[307], isEnable=True)
        set_skill(triggerIds=[308], isEnable=True)
        set_skill(triggerIds=[309], isEnable=True)
        set_skill(triggerIds=[310], isEnable=True)
        set_skill(triggerIds=[311], isEnable=True)
        set_skill(triggerIds=[312], isEnable=True)
        set_skill(triggerIds=[313], isEnable=True)
        set_skill(triggerIds=[314], isEnable=True)
        set_skill(triggerIds=[315], isEnable=True)
        set_skill(triggerIds=[316], isEnable=True)
        set_skill(triggerIds=[317], isEnable=True)
        set_skill(triggerIds=[318], isEnable=True)
        set_skill(triggerIds=[319], isEnable=True)
        set_skill(triggerIds=[320], isEnable=True)
        set_skill(triggerIds=[321], isEnable=True)
        set_skill(triggerIds=[322], isEnable=True)
        set_skill(triggerIds=[323], isEnable=True)
        set_skill(triggerIds=[324], isEnable=True)
        set_skill(triggerIds=[325], isEnable=True)
        set_skill(triggerIds=[326], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬03대기()


class 스킬03대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[307], isEnable=False)
        set_skill(triggerIds=[308], isEnable=False)
        set_skill(triggerIds=[309], isEnable=False)
        set_skill(triggerIds=[310], isEnable=False)
        set_skill(triggerIds=[311], isEnable=False)
        set_skill(triggerIds=[312], isEnable=False)
        set_skill(triggerIds=[313], isEnable=False)
        set_skill(triggerIds=[314], isEnable=False)
        set_skill(triggerIds=[315], isEnable=False)
        set_skill(triggerIds=[316], isEnable=False)
        set_skill(triggerIds=[317], isEnable=False)
        set_skill(triggerIds=[318], isEnable=False)
        set_skill(triggerIds=[319], isEnable=False)
        set_skill(triggerIds=[320], isEnable=False)
        set_skill(triggerIds=[321], isEnable=False)
        set_skill(triggerIds=[322], isEnable=False)
        set_skill(triggerIds=[323], isEnable=False)
        set_skill(triggerIds=[324], isEnable=False)
        set_skill(triggerIds=[325], isEnable=False)
        set_skill(triggerIds=[326], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬03()


class 스킬03(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[313], isEnable=True)
        set_skill(triggerIds=[314], isEnable=True)
        set_skill(triggerIds=[315], isEnable=True)
        set_skill(triggerIds=[316], isEnable=True)
        set_skill(triggerIds=[317], isEnable=True)
        set_skill(triggerIds=[318], isEnable=True)
        set_skill(triggerIds=[319], isEnable=True)
        set_skill(triggerIds=[320], isEnable=True)
        set_skill(triggerIds=[321], isEnable=True)
        set_skill(triggerIds=[322], isEnable=True)
        set_skill(triggerIds=[323], isEnable=True)
        set_skill(triggerIds=[324], isEnable=True)
        set_skill(triggerIds=[325], isEnable=True)
        set_skill(triggerIds=[326], isEnable=True)
        set_skill(triggerIds=[327], isEnable=True)
        set_skill(triggerIds=[328], isEnable=True)
        set_skill(triggerIds=[329], isEnable=True)
        set_skill(triggerIds=[330], isEnable=True)
        set_skill(triggerIds=[331], isEnable=True)
        set_skill(triggerIds=[332], isEnable=True)
        set_skill(triggerIds=[333], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬04대기()


class 스킬04대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[313], isEnable=False)
        set_skill(triggerIds=[314], isEnable=False)
        set_skill(triggerIds=[315], isEnable=False)
        set_skill(triggerIds=[316], isEnable=False)
        set_skill(triggerIds=[317], isEnable=False)
        set_skill(triggerIds=[318], isEnable=False)
        set_skill(triggerIds=[319], isEnable=False)
        set_skill(triggerIds=[320], isEnable=False)
        set_skill(triggerIds=[321], isEnable=False)
        set_skill(triggerIds=[322], isEnable=False)
        set_skill(triggerIds=[323], isEnable=False)
        set_skill(triggerIds=[324], isEnable=False)
        set_skill(triggerIds=[325], isEnable=False)
        set_skill(triggerIds=[326], isEnable=False)
        set_skill(triggerIds=[327], isEnable=False)
        set_skill(triggerIds=[328], isEnable=False)
        set_skill(triggerIds=[329], isEnable=False)
        set_skill(triggerIds=[330], isEnable=False)
        set_skill(triggerIds=[331], isEnable=False)
        set_skill(triggerIds=[332], isEnable=False)
        set_skill(triggerIds=[333], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬04()


class 스킬04(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[320], isEnable=True)
        set_skill(triggerIds=[321], isEnable=True)
        set_skill(triggerIds=[322], isEnable=True)
        set_skill(triggerIds=[323], isEnable=True)
        set_skill(triggerIds=[324], isEnable=True)
        set_skill(triggerIds=[325], isEnable=True)
        set_skill(triggerIds=[326], isEnable=True)
        set_skill(triggerIds=[327], isEnable=True)
        set_skill(triggerIds=[328], isEnable=True)
        set_skill(triggerIds=[329], isEnable=True)
        set_skill(triggerIds=[330], isEnable=True)
        set_skill(triggerIds=[331], isEnable=True)
        set_skill(triggerIds=[332], isEnable=True)
        set_skill(triggerIds=[333], isEnable=True)
        set_skill(triggerIds=[334], isEnable=True)
        set_skill(triggerIds=[335], isEnable=True)
        set_skill(triggerIds=[336], isEnable=True)
        set_skill(triggerIds=[337], isEnable=True)
        set_skill(triggerIds=[338], isEnable=True)
        set_skill(triggerIds=[339], isEnable=True)
        set_skill(triggerIds=[340], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬05대기()


class 스킬05대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[320], isEnable=False)
        set_skill(triggerIds=[321], isEnable=False)
        set_skill(triggerIds=[322], isEnable=False)
        set_skill(triggerIds=[323], isEnable=False)
        set_skill(triggerIds=[324], isEnable=False)
        set_skill(triggerIds=[325], isEnable=False)
        set_skill(triggerIds=[326], isEnable=False)
        set_skill(triggerIds=[327], isEnable=False)
        set_skill(triggerIds=[328], isEnable=False)
        set_skill(triggerIds=[329], isEnable=False)
        set_skill(triggerIds=[330], isEnable=False)
        set_skill(triggerIds=[331], isEnable=False)
        set_skill(triggerIds=[332], isEnable=False)
        set_skill(triggerIds=[333], isEnable=False)
        set_skill(triggerIds=[334], isEnable=False)
        set_skill(triggerIds=[335], isEnable=False)
        set_skill(triggerIds=[336], isEnable=False)
        set_skill(triggerIds=[337], isEnable=False)
        set_skill(triggerIds=[338], isEnable=False)
        set_skill(triggerIds=[339], isEnable=False)
        set_skill(triggerIds=[340], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬05()


class 스킬05(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[327], isEnable=True)
        set_skill(triggerIds=[328], isEnable=True)
        set_skill(triggerIds=[329], isEnable=True)
        set_skill(triggerIds=[330], isEnable=True)
        set_skill(triggerIds=[331], isEnable=True)
        set_skill(triggerIds=[332], isEnable=True)
        set_skill(triggerIds=[333], isEnable=True)
        set_skill(triggerIds=[334], isEnable=True)
        set_skill(triggerIds=[335], isEnable=True)
        set_skill(triggerIds=[336], isEnable=True)
        set_skill(triggerIds=[337], isEnable=True)
        set_skill(triggerIds=[338], isEnable=True)
        set_skill(triggerIds=[339], isEnable=True)
        set_skill(triggerIds=[340], isEnable=True)
        set_skill(triggerIds=[341], isEnable=True)
        set_skill(triggerIds=[342], isEnable=True)
        set_skill(triggerIds=[343], isEnable=True)
        set_skill(triggerIds=[344], isEnable=True)
        set_skill(triggerIds=[345], isEnable=True)
        set_skill(triggerIds=[346], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬06대기()


class 스킬06대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[327], isEnable=False)
        set_skill(triggerIds=[328], isEnable=False)
        set_skill(triggerIds=[329], isEnable=False)
        set_skill(triggerIds=[330], isEnable=False)
        set_skill(triggerIds=[331], isEnable=False)
        set_skill(triggerIds=[332], isEnable=False)
        set_skill(triggerIds=[333], isEnable=False)
        set_skill(triggerIds=[334], isEnable=False)
        set_skill(triggerIds=[335], isEnable=False)
        set_skill(triggerIds=[336], isEnable=False)
        set_skill(triggerIds=[337], isEnable=False)
        set_skill(triggerIds=[338], isEnable=False)
        set_skill(triggerIds=[339], isEnable=False)
        set_skill(triggerIds=[340], isEnable=False)
        set_skill(triggerIds=[341], isEnable=False)
        set_skill(triggerIds=[342], isEnable=False)
        set_skill(triggerIds=[343], isEnable=False)
        set_skill(triggerIds=[344], isEnable=False)
        set_skill(triggerIds=[345], isEnable=False)
        set_skill(triggerIds=[346], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬06()


class 스킬06(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[334], isEnable=True)
        set_skill(triggerIds=[335], isEnable=True)
        set_skill(triggerIds=[336], isEnable=True)
        set_skill(triggerIds=[337], isEnable=True)
        set_skill(triggerIds=[338], isEnable=True)
        set_skill(triggerIds=[339], isEnable=True)
        set_skill(triggerIds=[340], isEnable=True)
        set_skill(triggerIds=[341], isEnable=True)
        set_skill(triggerIds=[342], isEnable=True)
        set_skill(triggerIds=[343], isEnable=True)
        set_skill(triggerIds=[344], isEnable=True)
        set_skill(triggerIds=[345], isEnable=True)
        set_skill(triggerIds=[346], isEnable=True)
        set_skill(triggerIds=[347], isEnable=True)
        set_skill(triggerIds=[348], isEnable=True)
        set_skill(triggerIds=[349], isEnable=True)
        set_skill(triggerIds=[350], isEnable=True)
        set_skill(triggerIds=[351], isEnable=True)
        set_skill(triggerIds=[352], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬07대기()


class 스킬07대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[334], isEnable=False)
        set_skill(triggerIds=[335], isEnable=False)
        set_skill(triggerIds=[336], isEnable=False)
        set_skill(triggerIds=[337], isEnable=False)
        set_skill(triggerIds=[338], isEnable=False)
        set_skill(triggerIds=[339], isEnable=False)
        set_skill(triggerIds=[340], isEnable=False)
        set_skill(triggerIds=[341], isEnable=False)
        set_skill(triggerIds=[342], isEnable=False)
        set_skill(triggerIds=[343], isEnable=False)
        set_skill(triggerIds=[344], isEnable=False)
        set_skill(triggerIds=[345], isEnable=False)
        set_skill(triggerIds=[346], isEnable=False)
        set_skill(triggerIds=[347], isEnable=False)
        set_skill(triggerIds=[348], isEnable=False)
        set_skill(triggerIds=[349], isEnable=False)
        set_skill(triggerIds=[350], isEnable=False)
        set_skill(triggerIds=[351], isEnable=False)
        set_skill(triggerIds=[352], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬07()


class 스킬07(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[341], isEnable=True)
        set_skill(triggerIds=[342], isEnable=True)
        set_skill(triggerIds=[343], isEnable=True)
        set_skill(triggerIds=[344], isEnable=True)
        set_skill(triggerIds=[345], isEnable=True)
        set_skill(triggerIds=[346], isEnable=True)
        set_skill(triggerIds=[347], isEnable=True)
        set_skill(triggerIds=[348], isEnable=True)
        set_skill(triggerIds=[349], isEnable=True)
        set_skill(triggerIds=[350], isEnable=True)
        set_skill(triggerIds=[351], isEnable=True)
        set_skill(triggerIds=[352], isEnable=True)
        set_skill(triggerIds=[353], isEnable=True)
        set_skill(triggerIds=[354], isEnable=True)
        set_skill(triggerIds=[355], isEnable=True)
        set_skill(triggerIds=[356], isEnable=True)
        set_skill(triggerIds=[357], isEnable=True)
        set_skill(triggerIds=[358], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬08대기()


class 스킬08대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[341], isEnable=False)
        set_skill(triggerIds=[342], isEnable=False)
        set_skill(triggerIds=[343], isEnable=False)
        set_skill(triggerIds=[344], isEnable=False)
        set_skill(triggerIds=[345], isEnable=False)
        set_skill(triggerIds=[346], isEnable=False)
        set_skill(triggerIds=[347], isEnable=False)
        set_skill(triggerIds=[348], isEnable=False)
        set_skill(triggerIds=[349], isEnable=False)
        set_skill(triggerIds=[350], isEnable=False)
        set_skill(triggerIds=[351], isEnable=False)
        set_skill(triggerIds=[352], isEnable=False)
        set_skill(triggerIds=[353], isEnable=False)
        set_skill(triggerIds=[354], isEnable=False)
        set_skill(triggerIds=[355], isEnable=False)
        set_skill(triggerIds=[356], isEnable=False)
        set_skill(triggerIds=[357], isEnable=False)
        set_skill(triggerIds=[358], isEnable=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000409], arg2=0):
            return 굳음()
        if true():
            return 스킬08()


class 굳음(state.State):
    def on_enter(self):
        set_timer(timerId='20', seconds=20)

    def on_tick(self) -> state.State:
        if time_expired(timerId='20'):
            return 스킬08()


class 스킬08(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1101,1102,1103,1104,1105,1106,1107,1108], visible=False, arg3=0, arg4=100)
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[347], isEnable=True)
        set_skill(triggerIds=[348], isEnable=True)
        set_skill(triggerIds=[349], isEnable=True)
        set_skill(triggerIds=[350], isEnable=True)
        set_skill(triggerIds=[351], isEnable=True)
        set_skill(triggerIds=[352], isEnable=True)
        set_skill(triggerIds=[353], isEnable=True)
        set_skill(triggerIds=[354], isEnable=True)
        set_skill(triggerIds=[355], isEnable=True)
        set_skill(triggerIds=[356], isEnable=True)
        set_skill(triggerIds=[357], isEnable=True)
        set_skill(triggerIds=[358], isEnable=True)
        set_skill(triggerIds=[359], isEnable=True)
        set_skill(triggerIds=[360], isEnable=True)
        set_skill(triggerIds=[361], isEnable=True)
        set_skill(triggerIds=[362], isEnable=True)
        set_skill(triggerIds=[363], isEnable=True)
        set_skill(triggerIds=[364], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬09대기()


class 스킬09대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[347], isEnable=False)
        set_skill(triggerIds=[348], isEnable=False)
        set_skill(triggerIds=[349], isEnable=False)
        set_skill(triggerIds=[350], isEnable=False)
        set_skill(triggerIds=[351], isEnable=False)
        set_skill(triggerIds=[352], isEnable=False)
        set_skill(triggerIds=[353], isEnable=False)
        set_skill(triggerIds=[354], isEnable=False)
        set_skill(triggerIds=[355], isEnable=False)
        set_skill(triggerIds=[356], isEnable=False)
        set_skill(triggerIds=[357], isEnable=False)
        set_skill(triggerIds=[358], isEnable=False)
        set_skill(triggerIds=[359], isEnable=False)
        set_skill(triggerIds=[360], isEnable=False)
        set_skill(triggerIds=[361], isEnable=False)
        set_skill(triggerIds=[362], isEnable=False)
        set_skill(triggerIds=[363], isEnable=False)
        set_skill(triggerIds=[364], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬09()


class 스킬09(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[353], isEnable=True)
        set_skill(triggerIds=[354], isEnable=True)
        set_skill(triggerIds=[355], isEnable=True)
        set_skill(triggerIds=[356], isEnable=True)
        set_skill(triggerIds=[357], isEnable=True)
        set_skill(triggerIds=[358], isEnable=True)
        set_skill(triggerIds=[359], isEnable=True)
        set_skill(triggerIds=[360], isEnable=True)
        set_skill(triggerIds=[361], isEnable=True)
        set_skill(triggerIds=[362], isEnable=True)
        set_skill(triggerIds=[363], isEnable=True)
        set_skill(triggerIds=[364], isEnable=True)
        set_skill(triggerIds=[365], isEnable=True)
        set_skill(triggerIds=[366], isEnable=True)
        set_skill(triggerIds=[367], isEnable=True)
        set_skill(triggerIds=[368], isEnable=True)
        set_skill(triggerIds=[369], isEnable=True)
        set_skill(triggerIds=[370], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬10대기()


class 스킬10대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[353], isEnable=False)
        set_skill(triggerIds=[354], isEnable=False)
        set_skill(triggerIds=[355], isEnable=False)
        set_skill(triggerIds=[356], isEnable=False)
        set_skill(triggerIds=[357], isEnable=False)
        set_skill(triggerIds=[358], isEnable=False)
        set_skill(triggerIds=[359], isEnable=False)
        set_skill(triggerIds=[360], isEnable=False)
        set_skill(triggerIds=[361], isEnable=False)
        set_skill(triggerIds=[362], isEnable=False)
        set_skill(triggerIds=[363], isEnable=False)
        set_skill(triggerIds=[364], isEnable=False)
        set_skill(triggerIds=[365], isEnable=False)
        set_skill(triggerIds=[366], isEnable=False)
        set_skill(triggerIds=[367], isEnable=False)
        set_skill(triggerIds=[368], isEnable=False)
        set_skill(triggerIds=[369], isEnable=False)
        set_skill(triggerIds=[370], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬10()


class 스킬10(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[359], isEnable=True)
        set_skill(triggerIds=[360], isEnable=True)
        set_skill(triggerIds=[361], isEnable=True)
        set_skill(triggerIds=[362], isEnable=True)
        set_skill(triggerIds=[363], isEnable=True)
        set_skill(triggerIds=[364], isEnable=True)
        set_skill(triggerIds=[365], isEnable=True)
        set_skill(triggerIds=[366], isEnable=True)
        set_skill(triggerIds=[367], isEnable=True)
        set_skill(triggerIds=[368], isEnable=True)
        set_skill(triggerIds=[369], isEnable=True)
        set_skill(triggerIds=[370], isEnable=True)
        set_skill(triggerIds=[371], isEnable=True)
        set_skill(triggerIds=[372], isEnable=True)
        set_skill(triggerIds=[373], isEnable=True)
        set_skill(triggerIds=[374], isEnable=True)
        set_skill(triggerIds=[375], isEnable=True)
        set_skill(triggerIds=[376], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬11대기()


class 스킬11대기(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=0)
        set_skill(triggerIds=[359], isEnable=False)
        set_skill(triggerIds=[360], isEnable=False)
        set_skill(triggerIds=[361], isEnable=False)
        set_skill(triggerIds=[362], isEnable=False)
        set_skill(triggerIds=[363], isEnable=False)
        set_skill(triggerIds=[364], isEnable=False)
        set_skill(triggerIds=[365], isEnable=False)
        set_skill(triggerIds=[366], isEnable=False)
        set_skill(triggerIds=[367], isEnable=False)
        set_skill(triggerIds=[368], isEnable=False)
        set_skill(triggerIds=[369], isEnable=False)
        set_skill(triggerIds=[370], isEnable=False)
        set_skill(triggerIds=[371], isEnable=False)
        set_skill(triggerIds=[372], isEnable=False)
        set_skill(triggerIds=[373], isEnable=False)
        set_skill(triggerIds=[374], isEnable=False)
        set_skill(triggerIds=[375], isEnable=False)
        set_skill(triggerIds=[376], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬12()


class 스킬12(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[365], isEnable=True)
        set_skill(triggerIds=[366], isEnable=True)
        set_skill(triggerIds=[367], isEnable=True)
        set_skill(triggerIds=[368], isEnable=True)
        set_skill(triggerIds=[369], isEnable=True)
        set_skill(triggerIds=[370], isEnable=True)
        set_skill(triggerIds=[371], isEnable=True)
        set_skill(triggerIds=[372], isEnable=True)
        set_skill(triggerIds=[373], isEnable=True)
        set_skill(triggerIds=[374], isEnable=True)
        set_skill(triggerIds=[375], isEnable=True)
        set_skill(triggerIds=[376], isEnable=True)
        set_skill(triggerIds=[377], isEnable=True)
        set_skill(triggerIds=[378], isEnable=True)
        set_skill(triggerIds=[379], isEnable=True)
        set_skill(triggerIds=[380], isEnable=True)
        set_skill(triggerIds=[381], isEnable=True)
        set_skill(triggerIds=[382], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬13대기()


class 스킬13대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[365], isEnable=False)
        set_skill(triggerIds=[366], isEnable=False)
        set_skill(triggerIds=[367], isEnable=False)
        set_skill(triggerIds=[368], isEnable=False)
        set_skill(triggerIds=[369], isEnable=False)
        set_skill(triggerIds=[370], isEnable=False)
        set_skill(triggerIds=[371], isEnable=False)
        set_skill(triggerIds=[372], isEnable=False)
        set_skill(triggerIds=[373], isEnable=False)
        set_skill(triggerIds=[374], isEnable=False)
        set_skill(triggerIds=[375], isEnable=False)
        set_skill(triggerIds=[376], isEnable=False)
        set_skill(triggerIds=[377], isEnable=False)
        set_skill(triggerIds=[378], isEnable=False)
        set_skill(triggerIds=[379], isEnable=False)
        set_skill(triggerIds=[380], isEnable=False)
        set_skill(triggerIds=[381], isEnable=False)
        set_skill(triggerIds=[382], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬13()


class 스킬13(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[371], isEnable=True)
        set_skill(triggerIds=[372], isEnable=True)
        set_skill(triggerIds=[373], isEnable=True)
        set_skill(triggerIds=[374], isEnable=True)
        set_skill(triggerIds=[375], isEnable=True)
        set_skill(triggerIds=[376], isEnable=True)
        set_skill(triggerIds=[377], isEnable=True)
        set_skill(triggerIds=[378], isEnable=True)
        set_skill(triggerIds=[379], isEnable=True)
        set_skill(triggerIds=[380], isEnable=True)
        set_skill(triggerIds=[381], isEnable=True)
        set_skill(triggerIds=[382], isEnable=True)
        set_skill(triggerIds=[383], isEnable=True)
        set_skill(triggerIds=[384], isEnable=True)
        set_skill(triggerIds=[385], isEnable=True)
        set_skill(triggerIds=[386], isEnable=True)
        set_skill(triggerIds=[387], isEnable=True)
        set_skill(triggerIds=[388], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬14대기()


class 스킬14대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[371], isEnable=False)
        set_skill(triggerIds=[372], isEnable=False)
        set_skill(triggerIds=[373], isEnable=False)
        set_skill(triggerIds=[374], isEnable=False)
        set_skill(triggerIds=[375], isEnable=False)
        set_skill(triggerIds=[376], isEnable=False)
        set_skill(triggerIds=[377], isEnable=False)
        set_skill(triggerIds=[378], isEnable=False)
        set_skill(triggerIds=[379], isEnable=False)
        set_skill(triggerIds=[380], isEnable=False)
        set_skill(triggerIds=[381], isEnable=False)
        set_skill(triggerIds=[382], isEnable=False)
        set_skill(triggerIds=[383], isEnable=False)
        set_skill(triggerIds=[384], isEnable=False)
        set_skill(triggerIds=[385], isEnable=False)
        set_skill(triggerIds=[386], isEnable=False)
        set_skill(triggerIds=[387], isEnable=False)
        set_skill(triggerIds=[388], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬14()


class 스킬14(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[377], isEnable=True)
        set_skill(triggerIds=[378], isEnable=True)
        set_skill(triggerIds=[379], isEnable=True)
        set_skill(triggerIds=[380], isEnable=True)
        set_skill(triggerIds=[381], isEnable=True)
        set_skill(triggerIds=[382], isEnable=True)
        set_skill(triggerIds=[383], isEnable=True)
        set_skill(triggerIds=[384], isEnable=True)
        set_skill(triggerIds=[385], isEnable=True)
        set_skill(triggerIds=[386], isEnable=True)
        set_skill(triggerIds=[387], isEnable=True)
        set_skill(triggerIds=[388], isEnable=True)
        set_skill(triggerIds=[389], isEnable=True)
        set_skill(triggerIds=[390], isEnable=True)
        set_skill(triggerIds=[391], isEnable=True)
        set_skill(triggerIds=[392], isEnable=True)
        set_skill(triggerIds=[393], isEnable=True)
        set_skill(triggerIds=[394], isEnable=True)
        set_skill(triggerIds=[395], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬15대기()


class 스킬15대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[377], isEnable=False)
        set_skill(triggerIds=[378], isEnable=False)
        set_skill(triggerIds=[379], isEnable=False)
        set_skill(triggerIds=[380], isEnable=False)
        set_skill(triggerIds=[381], isEnable=False)
        set_skill(triggerIds=[382], isEnable=False)
        set_skill(triggerIds=[383], isEnable=False)
        set_skill(triggerIds=[384], isEnable=False)
        set_skill(triggerIds=[385], isEnable=False)
        set_skill(triggerIds=[386], isEnable=False)
        set_skill(triggerIds=[387], isEnable=False)
        set_skill(triggerIds=[388], isEnable=False)
        set_skill(triggerIds=[389], isEnable=False)
        set_skill(triggerIds=[390], isEnable=False)
        set_skill(triggerIds=[391], isEnable=False)
        set_skill(triggerIds=[392], isEnable=False)
        set_skill(triggerIds=[393], isEnable=False)
        set_skill(triggerIds=[394], isEnable=False)
        set_skill(triggerIds=[395], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬15()


class 스킬15(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[383], isEnable=True)
        set_skill(triggerIds=[384], isEnable=True)
        set_skill(triggerIds=[385], isEnable=True)
        set_skill(triggerIds=[386], isEnable=True)
        set_skill(triggerIds=[387], isEnable=True)
        set_skill(triggerIds=[388], isEnable=True)
        set_skill(triggerIds=[389], isEnable=True)
        set_skill(triggerIds=[390], isEnable=True)
        set_skill(triggerIds=[391], isEnable=True)
        set_skill(triggerIds=[392], isEnable=True)
        set_skill(triggerIds=[393], isEnable=True)
        set_skill(triggerIds=[394], isEnable=True)
        set_skill(triggerIds=[395], isEnable=True)
        set_skill(triggerIds=[396], isEnable=True)
        set_skill(triggerIds=[397], isEnable=True)
        set_skill(triggerIds=[398], isEnable=True)
        set_skill(triggerIds=[399], isEnable=True)
        set_skill(triggerIds=[400], isEnable=True)
        set_skill(triggerIds=[401], isEnable=True)
        set_skill(triggerIds=[402], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬16대기()


class 스킬16대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[383], isEnable=False)
        set_skill(triggerIds=[384], isEnable=False)
        set_skill(triggerIds=[385], isEnable=False)
        set_skill(triggerIds=[386], isEnable=False)
        set_skill(triggerIds=[387], isEnable=False)
        set_skill(triggerIds=[388], isEnable=False)
        set_skill(triggerIds=[389], isEnable=False)
        set_skill(triggerIds=[390], isEnable=False)
        set_skill(triggerIds=[391], isEnable=False)
        set_skill(triggerIds=[392], isEnable=False)
        set_skill(triggerIds=[393], isEnable=False)
        set_skill(triggerIds=[394], isEnable=False)
        set_skill(triggerIds=[395], isEnable=False)
        set_skill(triggerIds=[396], isEnable=False)
        set_skill(triggerIds=[397], isEnable=False)
        set_skill(triggerIds=[398], isEnable=False)
        set_skill(triggerIds=[399], isEnable=False)
        set_skill(triggerIds=[400], isEnable=False)
        set_skill(triggerIds=[401], isEnable=False)
        set_skill(triggerIds=[402], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬16()


class 스킬16(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[389], isEnable=True)
        set_skill(triggerIds=[390], isEnable=True)
        set_skill(triggerIds=[391], isEnable=True)
        set_skill(triggerIds=[392], isEnable=True)
        set_skill(triggerIds=[393], isEnable=True)
        set_skill(triggerIds=[394], isEnable=True)
        set_skill(triggerIds=[395], isEnable=True)
        set_skill(triggerIds=[396], isEnable=True)
        set_skill(triggerIds=[397], isEnable=True)
        set_skill(triggerIds=[398], isEnable=True)
        set_skill(triggerIds=[399], isEnable=True)
        set_skill(triggerIds=[400], isEnable=True)
        set_skill(triggerIds=[401], isEnable=True)
        set_skill(triggerIds=[402], isEnable=True)
        set_skill(triggerIds=[403], isEnable=True)
        set_skill(triggerIds=[404], isEnable=True)
        set_skill(triggerIds=[405], isEnable=True)
        set_skill(triggerIds=[406], isEnable=True)
        set_skill(triggerIds=[407], isEnable=True)
        set_skill(triggerIds=[408], isEnable=True)
        set_skill(triggerIds=[409], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬17대기()


class 스킬17대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[389], isEnable=False)
        set_skill(triggerIds=[390], isEnable=False)
        set_skill(triggerIds=[391], isEnable=False)
        set_skill(triggerIds=[392], isEnable=False)
        set_skill(triggerIds=[393], isEnable=False)
        set_skill(triggerIds=[394], isEnable=False)
        set_skill(triggerIds=[395], isEnable=False)
        set_skill(triggerIds=[396], isEnable=False)
        set_skill(triggerIds=[397], isEnable=False)
        set_skill(triggerIds=[398], isEnable=False)
        set_skill(triggerIds=[399], isEnable=False)
        set_skill(triggerIds=[400], isEnable=False)
        set_skill(triggerIds=[401], isEnable=False)
        set_skill(triggerIds=[402], isEnable=False)
        set_skill(triggerIds=[403], isEnable=False)
        set_skill(triggerIds=[404], isEnable=False)
        set_skill(triggerIds=[405], isEnable=False)
        set_skill(triggerIds=[406], isEnable=False)
        set_skill(triggerIds=[407], isEnable=False)
        set_skill(triggerIds=[408], isEnable=False)
        set_skill(triggerIds=[409], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬17()


class 스킬17(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[396], isEnable=True)
        set_skill(triggerIds=[397], isEnable=True)
        set_skill(triggerIds=[398], isEnable=True)
        set_skill(triggerIds=[399], isEnable=True)
        set_skill(triggerIds=[400], isEnable=True)
        set_skill(triggerIds=[401], isEnable=True)
        set_skill(triggerIds=[402], isEnable=True)
        set_skill(triggerIds=[403], isEnable=True)
        set_skill(triggerIds=[404], isEnable=True)
        set_skill(triggerIds=[405], isEnable=True)
        set_skill(triggerIds=[406], isEnable=True)
        set_skill(triggerIds=[407], isEnable=True)
        set_skill(triggerIds=[408], isEnable=True)
        set_skill(triggerIds=[409], isEnable=True)
        set_skill(triggerIds=[410], isEnable=True)
        set_skill(triggerIds=[411], isEnable=True)
        set_skill(triggerIds=[412], isEnable=True)
        set_skill(triggerIds=[413], isEnable=True)
        set_skill(triggerIds=[414], isEnable=True)
        set_skill(triggerIds=[415], isEnable=True)
        set_skill(triggerIds=[416], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬18대기()


class 스킬18대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[396], isEnable=False)
        set_skill(triggerIds=[397], isEnable=False)
        set_skill(triggerIds=[398], isEnable=False)
        set_skill(triggerIds=[399], isEnable=False)
        set_skill(triggerIds=[400], isEnable=False)
        set_skill(triggerIds=[401], isEnable=False)
        set_skill(triggerIds=[402], isEnable=False)
        set_skill(triggerIds=[403], isEnable=False)
        set_skill(triggerIds=[404], isEnable=False)
        set_skill(triggerIds=[405], isEnable=False)
        set_skill(triggerIds=[406], isEnable=False)
        set_skill(triggerIds=[407], isEnable=False)
        set_skill(triggerIds=[408], isEnable=False)
        set_skill(triggerIds=[409], isEnable=False)
        set_skill(triggerIds=[410], isEnable=False)
        set_skill(triggerIds=[411], isEnable=False)
        set_skill(triggerIds=[412], isEnable=False)
        set_skill(triggerIds=[413], isEnable=False)
        set_skill(triggerIds=[414], isEnable=False)
        set_skill(triggerIds=[415], isEnable=False)
        set_skill(triggerIds=[416], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬18()


class 스킬18(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[403], isEnable=True)
        set_skill(triggerIds=[404], isEnable=True)
        set_skill(triggerIds=[405], isEnable=True)
        set_skill(triggerIds=[406], isEnable=True)
        set_skill(triggerIds=[407], isEnable=True)
        set_skill(triggerIds=[408], isEnable=True)
        set_skill(triggerIds=[409], isEnable=True)
        set_skill(triggerIds=[410], isEnable=True)
        set_skill(triggerIds=[411], isEnable=True)
        set_skill(triggerIds=[412], isEnable=True)
        set_skill(triggerIds=[413], isEnable=True)
        set_skill(triggerIds=[414], isEnable=True)
        set_skill(triggerIds=[415], isEnable=True)
        set_skill(triggerIds=[416], isEnable=True)
        set_skill(triggerIds=[417], isEnable=True)
        set_skill(triggerIds=[418], isEnable=True)
        set_skill(triggerIds=[419], isEnable=True)
        set_skill(triggerIds=[420], isEnable=True)
        set_skill(triggerIds=[421], isEnable=True)
        set_skill(triggerIds=[422], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬19대기()


class 스킬19대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[403], isEnable=False)
        set_skill(triggerIds=[404], isEnable=False)
        set_skill(triggerIds=[405], isEnable=False)
        set_skill(triggerIds=[406], isEnable=False)
        set_skill(triggerIds=[407], isEnable=False)
        set_skill(triggerIds=[408], isEnable=False)
        set_skill(triggerIds=[409], isEnable=False)
        set_skill(triggerIds=[410], isEnable=False)
        set_skill(triggerIds=[411], isEnable=False)
        set_skill(triggerIds=[412], isEnable=False)
        set_skill(triggerIds=[413], isEnable=False)
        set_skill(triggerIds=[414], isEnable=False)
        set_skill(triggerIds=[415], isEnable=False)
        set_skill(triggerIds=[416], isEnable=False)
        set_skill(triggerIds=[417], isEnable=False)
        set_skill(triggerIds=[418], isEnable=False)
        set_skill(triggerIds=[419], isEnable=False)
        set_skill(triggerIds=[420], isEnable=False)
        set_skill(triggerIds=[421], isEnable=False)
        set_skill(triggerIds=[422], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬19()


class 스킬19(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[410], isEnable=True)
        set_skill(triggerIds=[411], isEnable=True)
        set_skill(triggerIds=[412], isEnable=True)
        set_skill(triggerIds=[413], isEnable=True)
        set_skill(triggerIds=[414], isEnable=True)
        set_skill(triggerIds=[415], isEnable=True)
        set_skill(triggerIds=[416], isEnable=True)
        set_skill(triggerIds=[417], isEnable=True)
        set_skill(triggerIds=[418], isEnable=True)
        set_skill(triggerIds=[419], isEnable=True)
        set_skill(triggerIds=[420], isEnable=True)
        set_skill(triggerIds=[421], isEnable=True)
        set_skill(triggerIds=[422], isEnable=True)
        set_skill(triggerIds=[423], isEnable=True)
        set_skill(triggerIds=[424], isEnable=True)
        set_skill(triggerIds=[425], isEnable=True)
        set_skill(triggerIds=[426], isEnable=True)
        set_skill(triggerIds=[427], isEnable=True)
        set_skill(triggerIds=[428], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬20대기()


class 스킬20대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[410], isEnable=False)
        set_skill(triggerIds=[411], isEnable=False)
        set_skill(triggerIds=[412], isEnable=False)
        set_skill(triggerIds=[413], isEnable=False)
        set_skill(triggerIds=[414], isEnable=False)
        set_skill(triggerIds=[415], isEnable=False)
        set_skill(triggerIds=[416], isEnable=False)
        set_skill(triggerIds=[417], isEnable=False)
        set_skill(triggerIds=[418], isEnable=False)
        set_skill(triggerIds=[419], isEnable=False)
        set_skill(triggerIds=[420], isEnable=False)
        set_skill(triggerIds=[421], isEnable=False)
        set_skill(triggerIds=[422], isEnable=False)
        set_skill(triggerIds=[423], isEnable=False)
        set_skill(triggerIds=[424], isEnable=False)
        set_skill(triggerIds=[425], isEnable=False)
        set_skill(triggerIds=[426], isEnable=False)
        set_skill(triggerIds=[427], isEnable=False)
        set_skill(triggerIds=[428], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬20()


class 스킬20(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[417], isEnable=True)
        set_skill(triggerIds=[418], isEnable=True)
        set_skill(triggerIds=[419], isEnable=True)
        set_skill(triggerIds=[420], isEnable=True)
        set_skill(triggerIds=[421], isEnable=True)
        set_skill(triggerIds=[422], isEnable=True)
        set_skill(triggerIds=[423], isEnable=True)
        set_skill(triggerIds=[424], isEnable=True)
        set_skill(triggerIds=[425], isEnable=True)
        set_skill(triggerIds=[426], isEnable=True)
        set_skill(triggerIds=[427], isEnable=True)
        set_skill(triggerIds=[428], isEnable=True)
        set_skill(triggerIds=[429], isEnable=True)
        set_skill(triggerIds=[430], isEnable=True)
        set_skill(triggerIds=[431], isEnable=True)
        set_skill(triggerIds=[432], isEnable=True)
        set_skill(triggerIds=[433], isEnable=True)
        set_skill(triggerIds=[434], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬21대기()


class 스킬21대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[417], isEnable=False)
        set_skill(triggerIds=[418], isEnable=False)
        set_skill(triggerIds=[419], isEnable=False)
        set_skill(triggerIds=[420], isEnable=False)
        set_skill(triggerIds=[421], isEnable=False)
        set_skill(triggerIds=[422], isEnable=False)
        set_skill(triggerIds=[423], isEnable=False)
        set_skill(triggerIds=[424], isEnable=False)
        set_skill(triggerIds=[425], isEnable=False)
        set_skill(triggerIds=[426], isEnable=False)
        set_skill(triggerIds=[427], isEnable=False)
        set_skill(triggerIds=[428], isEnable=False)
        set_skill(triggerIds=[429], isEnable=False)
        set_skill(triggerIds=[430], isEnable=False)
        set_skill(triggerIds=[431], isEnable=False)
        set_skill(triggerIds=[432], isEnable=False)
        set_skill(triggerIds=[433], isEnable=False)
        set_skill(triggerIds=[434], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬21()


class 스킬21(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[423], isEnable=True)
        set_skill(triggerIds=[424], isEnable=True)
        set_skill(triggerIds=[425], isEnable=True)
        set_skill(triggerIds=[426], isEnable=True)
        set_skill(triggerIds=[427], isEnable=True)
        set_skill(triggerIds=[428], isEnable=True)
        set_skill(triggerIds=[429], isEnable=True)
        set_skill(triggerIds=[430], isEnable=True)
        set_skill(triggerIds=[431], isEnable=True)
        set_skill(triggerIds=[432], isEnable=True)
        set_skill(triggerIds=[433], isEnable=True)
        set_skill(triggerIds=[434], isEnable=True)
        set_skill(triggerIds=[435], isEnable=True)
        set_skill(triggerIds=[436], isEnable=True)
        set_skill(triggerIds=[437], isEnable=True)
        set_skill(triggerIds=[438], isEnable=True)
        set_skill(triggerIds=[439], isEnable=True)
        set_skill(triggerIds=[440], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬22대기()


class 스킬22대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[423], isEnable=False)
        set_skill(triggerIds=[424], isEnable=False)
        set_skill(triggerIds=[425], isEnable=False)
        set_skill(triggerIds=[426], isEnable=False)
        set_skill(triggerIds=[427], isEnable=False)
        set_skill(triggerIds=[428], isEnable=False)
        set_skill(triggerIds=[429], isEnable=False)
        set_skill(triggerIds=[430], isEnable=False)
        set_skill(triggerIds=[431], isEnable=False)
        set_skill(triggerIds=[432], isEnable=False)
        set_skill(triggerIds=[433], isEnable=False)
        set_skill(triggerIds=[434], isEnable=False)
        set_skill(triggerIds=[435], isEnable=False)
        set_skill(triggerIds=[436], isEnable=False)
        set_skill(triggerIds=[437], isEnable=False)
        set_skill(triggerIds=[438], isEnable=False)
        set_skill(triggerIds=[439], isEnable=False)
        set_skill(triggerIds=[440], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬22()


class 스킬22(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[429], isEnable=True)
        set_skill(triggerIds=[430], isEnable=True)
        set_skill(triggerIds=[431], isEnable=True)
        set_skill(triggerIds=[432], isEnable=True)
        set_skill(triggerIds=[433], isEnable=True)
        set_skill(triggerIds=[434], isEnable=True)
        set_skill(triggerIds=[435], isEnable=True)
        set_skill(triggerIds=[436], isEnable=True)
        set_skill(triggerIds=[437], isEnable=True)
        set_skill(triggerIds=[438], isEnable=True)
        set_skill(triggerIds=[439], isEnable=True)
        set_skill(triggerIds=[440], isEnable=True)
        set_skill(triggerIds=[441], isEnable=True)
        set_skill(triggerIds=[442], isEnable=True)
        set_skill(triggerIds=[443], isEnable=True)
        set_skill(triggerIds=[444], isEnable=True)
        set_skill(triggerIds=[445], isEnable=True)
        set_skill(triggerIds=[446], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬23대기()


class 스킬23대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[429], isEnable=False)
        set_skill(triggerIds=[430], isEnable=False)
        set_skill(triggerIds=[431], isEnable=False)
        set_skill(triggerIds=[432], isEnable=False)
        set_skill(triggerIds=[433], isEnable=False)
        set_skill(triggerIds=[434], isEnable=False)
        set_skill(triggerIds=[435], isEnable=False)
        set_skill(triggerIds=[436], isEnable=False)
        set_skill(triggerIds=[437], isEnable=False)
        set_skill(triggerIds=[438], isEnable=False)
        set_skill(triggerIds=[439], isEnable=False)
        set_skill(triggerIds=[440], isEnable=False)
        set_skill(triggerIds=[441], isEnable=False)
        set_skill(triggerIds=[442], isEnable=False)
        set_skill(triggerIds=[443], isEnable=False)
        set_skill(triggerIds=[444], isEnable=False)
        set_skill(triggerIds=[445], isEnable=False)
        set_skill(triggerIds=[446], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬23()


class 스킬23(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[435], isEnable=True)
        set_skill(triggerIds=[436], isEnable=True)
        set_skill(triggerIds=[437], isEnable=True)
        set_skill(triggerIds=[438], isEnable=True)
        set_skill(triggerIds=[439], isEnable=True)
        set_skill(triggerIds=[440], isEnable=True)
        set_skill(triggerIds=[441], isEnable=True)
        set_skill(triggerIds=[442], isEnable=True)
        set_skill(triggerIds=[443], isEnable=True)
        set_skill(triggerIds=[444], isEnable=True)
        set_skill(triggerIds=[445], isEnable=True)
        set_skill(triggerIds=[446], isEnable=True)
        set_skill(triggerIds=[447], isEnable=True)
        set_skill(triggerIds=[448], isEnable=True)
        set_skill(triggerIds=[449], isEnable=True)
        set_skill(triggerIds=[450], isEnable=True)
        set_skill(triggerIds=[451], isEnable=True)
        set_skill(triggerIds=[452], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬24대기()


class 스킬24대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[435], isEnable=False)
        set_skill(triggerIds=[436], isEnable=False)
        set_skill(triggerIds=[437], isEnable=False)
        set_skill(triggerIds=[438], isEnable=False)
        set_skill(triggerIds=[439], isEnable=False)
        set_skill(triggerIds=[440], isEnable=False)
        set_skill(triggerIds=[441], isEnable=False)
        set_skill(triggerIds=[442], isEnable=False)
        set_skill(triggerIds=[443], isEnable=False)
        set_skill(triggerIds=[444], isEnable=False)
        set_skill(triggerIds=[445], isEnable=False)
        set_skill(triggerIds=[446], isEnable=False)
        set_skill(triggerIds=[447], isEnable=False)
        set_skill(triggerIds=[448], isEnable=False)
        set_skill(triggerIds=[449], isEnable=False)
        set_skill(triggerIds=[450], isEnable=False)
        set_skill(triggerIds=[451], isEnable=False)
        set_skill(triggerIds=[452], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬24()


class 스킬24(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[441], isEnable=True)
        set_skill(triggerIds=[442], isEnable=True)
        set_skill(triggerIds=[443], isEnable=True)
        set_skill(triggerIds=[444], isEnable=True)
        set_skill(triggerIds=[445], isEnable=True)
        set_skill(triggerIds=[446], isEnable=True)
        set_skill(triggerIds=[447], isEnable=True)
        set_skill(triggerIds=[448], isEnable=True)
        set_skill(triggerIds=[449], isEnable=True)
        set_skill(triggerIds=[450], isEnable=True)
        set_skill(triggerIds=[451], isEnable=True)
        set_skill(triggerIds=[452], isEnable=True)
        set_skill(triggerIds=[453], isEnable=True)
        set_skill(triggerIds=[454], isEnable=True)
        set_skill(triggerIds=[455], isEnable=True)
        set_skill(triggerIds=[456], isEnable=True)
        set_skill(triggerIds=[457], isEnable=True)
        set_skill(triggerIds=[458], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬25대기()


class 스킬25대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[441], isEnable=False)
        set_skill(triggerIds=[442], isEnable=False)
        set_skill(triggerIds=[443], isEnable=False)
        set_skill(triggerIds=[444], isEnable=False)
        set_skill(triggerIds=[445], isEnable=False)
        set_skill(triggerIds=[446], isEnable=False)
        set_skill(triggerIds=[447], isEnable=False)
        set_skill(triggerIds=[448], isEnable=False)
        set_skill(triggerIds=[449], isEnable=False)
        set_skill(triggerIds=[450], isEnable=False)
        set_skill(triggerIds=[451], isEnable=False)
        set_skill(triggerIds=[452], isEnable=False)
        set_skill(triggerIds=[453], isEnable=False)
        set_skill(triggerIds=[454], isEnable=False)
        set_skill(triggerIds=[455], isEnable=False)
        set_skill(triggerIds=[456], isEnable=False)
        set_skill(triggerIds=[457], isEnable=False)
        set_skill(triggerIds=[458], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬25()


class 스킬25(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[447], isEnable=True)
        set_skill(triggerIds=[448], isEnable=True)
        set_skill(triggerIds=[449], isEnable=True)
        set_skill(triggerIds=[450], isEnable=True)
        set_skill(triggerIds=[451], isEnable=True)
        set_skill(triggerIds=[452], isEnable=True)
        set_skill(triggerIds=[453], isEnable=True)
        set_skill(triggerIds=[454], isEnable=True)
        set_skill(triggerIds=[455], isEnable=True)
        set_skill(triggerIds=[456], isEnable=True)
        set_skill(triggerIds=[457], isEnable=True)
        set_skill(triggerIds=[458], isEnable=True)
        set_skill(triggerIds=[459], isEnable=True)
        set_skill(triggerIds=[460], isEnable=True)
        set_skill(triggerIds=[461], isEnable=True)
        set_skill(triggerIds=[462], isEnable=True)
        set_skill(triggerIds=[463], isEnable=True)
        set_skill(triggerIds=[464], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬26대기()


class 스킬26대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[447], isEnable=False)
        set_skill(triggerIds=[448], isEnable=False)
        set_skill(triggerIds=[449], isEnable=False)
        set_skill(triggerIds=[450], isEnable=False)
        set_skill(triggerIds=[451], isEnable=False)
        set_skill(triggerIds=[452], isEnable=False)
        set_skill(triggerIds=[453], isEnable=False)
        set_skill(triggerIds=[454], isEnable=False)
        set_skill(triggerIds=[455], isEnable=False)
        set_skill(triggerIds=[456], isEnable=False)
        set_skill(triggerIds=[457], isEnable=False)
        set_skill(triggerIds=[458], isEnable=False)
        set_skill(triggerIds=[459], isEnable=False)
        set_skill(triggerIds=[460], isEnable=False)
        set_skill(triggerIds=[461], isEnable=False)
        set_skill(triggerIds=[462], isEnable=False)
        set_skill(triggerIds=[463], isEnable=False)
        set_skill(triggerIds=[464], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬26()


class 스킬26(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[453], isEnable=True)
        set_skill(triggerIds=[454], isEnable=True)
        set_skill(triggerIds=[455], isEnable=True)
        set_skill(triggerIds=[456], isEnable=True)
        set_skill(triggerIds=[457], isEnable=True)
        set_skill(triggerIds=[458], isEnable=True)
        set_skill(triggerIds=[459], isEnable=True)
        set_skill(triggerIds=[460], isEnable=True)
        set_skill(triggerIds=[461], isEnable=True)
        set_skill(triggerIds=[462], isEnable=True)
        set_skill(triggerIds=[463], isEnable=True)
        set_skill(triggerIds=[464], isEnable=True)
        set_skill(triggerIds=[465], isEnable=True)
        set_skill(triggerIds=[466], isEnable=True)
        set_skill(triggerIds=[467], isEnable=True)
        set_skill(triggerIds=[468], isEnable=True)
        set_skill(triggerIds=[469], isEnable=True)
        set_skill(triggerIds=[470], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬27대기()


class 스킬27대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[453], isEnable=False)
        set_skill(triggerIds=[454], isEnable=False)
        set_skill(triggerIds=[455], isEnable=False)
        set_skill(triggerIds=[456], isEnable=False)
        set_skill(triggerIds=[457], isEnable=False)
        set_skill(triggerIds=[458], isEnable=False)
        set_skill(triggerIds=[459], isEnable=False)
        set_skill(triggerIds=[460], isEnable=False)
        set_skill(triggerIds=[461], isEnable=False)
        set_skill(triggerIds=[462], isEnable=False)
        set_skill(triggerIds=[463], isEnable=False)
        set_skill(triggerIds=[464], isEnable=False)
        set_skill(triggerIds=[465], isEnable=False)
        set_skill(triggerIds=[466], isEnable=False)
        set_skill(triggerIds=[467], isEnable=False)
        set_skill(triggerIds=[468], isEnable=False)
        set_skill(triggerIds=[469], isEnable=False)
        set_skill(triggerIds=[470], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬27()


class 스킬27(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[459], isEnable=True)
        set_skill(triggerIds=[460], isEnable=True)
        set_skill(triggerIds=[461], isEnable=True)
        set_skill(triggerIds=[462], isEnable=True)
        set_skill(triggerIds=[463], isEnable=True)
        set_skill(triggerIds=[464], isEnable=True)
        set_skill(triggerIds=[465], isEnable=True)
        set_skill(triggerIds=[466], isEnable=True)
        set_skill(triggerIds=[467], isEnable=True)
        set_skill(triggerIds=[468], isEnable=True)
        set_skill(triggerIds=[469], isEnable=True)
        set_skill(triggerIds=[470], isEnable=True)
        set_skill(triggerIds=[471], isEnable=True)
        set_skill(triggerIds=[472], isEnable=True)
        set_skill(triggerIds=[473], isEnable=True)
        set_skill(triggerIds=[474], isEnable=True)
        set_skill(triggerIds=[475], isEnable=True)
        set_skill(triggerIds=[476], isEnable=True)
        set_skill(triggerIds=[477], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬28대기()


class 스킬28대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[459], isEnable=False)
        set_skill(triggerIds=[460], isEnable=False)
        set_skill(triggerIds=[461], isEnable=False)
        set_skill(triggerIds=[462], isEnable=False)
        set_skill(triggerIds=[463], isEnable=False)
        set_skill(triggerIds=[464], isEnable=False)
        set_skill(triggerIds=[465], isEnable=False)
        set_skill(triggerIds=[466], isEnable=False)
        set_skill(triggerIds=[467], isEnable=False)
        set_skill(triggerIds=[468], isEnable=False)
        set_skill(triggerIds=[469], isEnable=False)
        set_skill(triggerIds=[470], isEnable=False)
        set_skill(triggerIds=[471], isEnable=False)
        set_skill(triggerIds=[472], isEnable=False)
        set_skill(triggerIds=[473], isEnable=False)
        set_skill(triggerIds=[474], isEnable=False)
        set_skill(triggerIds=[475], isEnable=False)
        set_skill(triggerIds=[476], isEnable=False)
        set_skill(triggerIds=[477], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬28()


class 스킬28(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[465], isEnable=True)
        set_skill(triggerIds=[466], isEnable=True)
        set_skill(triggerIds=[467], isEnable=True)
        set_skill(triggerIds=[468], isEnable=True)
        set_skill(triggerIds=[469], isEnable=True)
        set_skill(triggerIds=[470], isEnable=True)
        set_skill(triggerIds=[471], isEnable=True)
        set_skill(triggerIds=[472], isEnable=True)
        set_skill(triggerIds=[473], isEnable=True)
        set_skill(triggerIds=[474], isEnable=True)
        set_skill(triggerIds=[475], isEnable=True)
        set_skill(triggerIds=[476], isEnable=True)
        set_skill(triggerIds=[477], isEnable=True)
        set_skill(triggerIds=[478], isEnable=True)
        set_skill(triggerIds=[479], isEnable=True)
        set_skill(triggerIds=[480], isEnable=True)
        set_skill(triggerIds=[481], isEnable=True)
        set_skill(triggerIds=[482], isEnable=True)
        set_skill(triggerIds=[483], isEnable=True)
        set_skill(triggerIds=[484], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬29대기()


class 스킬29대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[465], isEnable=False)
        set_skill(triggerIds=[466], isEnable=False)
        set_skill(triggerIds=[467], isEnable=False)
        set_skill(triggerIds=[468], isEnable=False)
        set_skill(triggerIds=[469], isEnable=False)
        set_skill(triggerIds=[470], isEnable=False)
        set_skill(triggerIds=[471], isEnable=False)
        set_skill(triggerIds=[472], isEnable=False)
        set_skill(triggerIds=[473], isEnable=False)
        set_skill(triggerIds=[474], isEnable=False)
        set_skill(triggerIds=[475], isEnable=False)
        set_skill(triggerIds=[476], isEnable=False)
        set_skill(triggerIds=[477], isEnable=False)
        set_skill(triggerIds=[478], isEnable=False)
        set_skill(triggerIds=[479], isEnable=False)
        set_skill(triggerIds=[480], isEnable=False)
        set_skill(triggerIds=[481], isEnable=False)
        set_skill(triggerIds=[482], isEnable=False)
        set_skill(triggerIds=[483], isEnable=False)
        set_skill(triggerIds=[484], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬29()


class 스킬29(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[471], isEnable=True)
        set_skill(triggerIds=[472], isEnable=True)
        set_skill(triggerIds=[473], isEnable=True)
        set_skill(triggerIds=[474], isEnable=True)
        set_skill(triggerIds=[475], isEnable=True)
        set_skill(triggerIds=[476], isEnable=True)
        set_skill(triggerIds=[477], isEnable=True)
        set_skill(triggerIds=[478], isEnable=True)
        set_skill(triggerIds=[479], isEnable=True)
        set_skill(triggerIds=[480], isEnable=True)
        set_skill(triggerIds=[481], isEnable=True)
        set_skill(triggerIds=[482], isEnable=True)
        set_skill(triggerIds=[483], isEnable=True)
        set_skill(triggerIds=[484], isEnable=True)
        set_skill(triggerIds=[485], isEnable=True)
        set_skill(triggerIds=[486], isEnable=True)
        set_skill(triggerIds=[487], isEnable=True)
        set_skill(triggerIds=[488], isEnable=True)
        set_skill(triggerIds=[489], isEnable=True)
        set_skill(triggerIds=[490], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬30대기()


class 스킬30대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[471], isEnable=False)
        set_skill(triggerIds=[472], isEnable=False)
        set_skill(triggerIds=[473], isEnable=False)
        set_skill(triggerIds=[474], isEnable=False)
        set_skill(triggerIds=[475], isEnable=False)
        set_skill(triggerIds=[476], isEnable=False)
        set_skill(triggerIds=[477], isEnable=False)
        set_skill(triggerIds=[478], isEnable=False)
        set_skill(triggerIds=[479], isEnable=False)
        set_skill(triggerIds=[480], isEnable=False)
        set_skill(triggerIds=[481], isEnable=False)
        set_skill(triggerIds=[482], isEnable=False)
        set_skill(triggerIds=[483], isEnable=False)
        set_skill(triggerIds=[484], isEnable=False)
        set_skill(triggerIds=[485], isEnable=False)
        set_skill(triggerIds=[486], isEnable=False)
        set_skill(triggerIds=[487], isEnable=False)
        set_skill(triggerIds=[488], isEnable=False)
        set_skill(triggerIds=[489], isEnable=False)
        set_skill(triggerIds=[490], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬30()


class 스킬30(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[478], isEnable=True)
        set_skill(triggerIds=[479], isEnable=True)
        set_skill(triggerIds=[480], isEnable=True)
        set_skill(triggerIds=[481], isEnable=True)
        set_skill(triggerIds=[482], isEnable=True)
        set_skill(triggerIds=[483], isEnable=True)
        set_skill(triggerIds=[484], isEnable=True)
        set_skill(triggerIds=[485], isEnable=True)
        set_skill(triggerIds=[486], isEnable=True)
        set_skill(triggerIds=[487], isEnable=True)
        set_skill(triggerIds=[488], isEnable=True)
        set_skill(triggerIds=[489], isEnable=True)
        set_skill(triggerIds=[490], isEnable=True)
        set_skill(triggerIds=[491], isEnable=True)
        set_skill(triggerIds=[492], isEnable=True)
        set_skill(triggerIds=[493], isEnable=True)
        set_skill(triggerIds=[494], isEnable=True)
        set_skill(triggerIds=[495], isEnable=True)
        set_skill(triggerIds=[496], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬31대기()


class 스킬31대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[478], isEnable=False)
        set_skill(triggerIds=[479], isEnable=False)
        set_skill(triggerIds=[480], isEnable=False)
        set_skill(triggerIds=[481], isEnable=False)
        set_skill(triggerIds=[482], isEnable=False)
        set_skill(triggerIds=[483], isEnable=False)
        set_skill(triggerIds=[484], isEnable=False)
        set_skill(triggerIds=[485], isEnable=False)
        set_skill(triggerIds=[486], isEnable=False)
        set_skill(triggerIds=[487], isEnable=False)
        set_skill(triggerIds=[488], isEnable=False)
        set_skill(triggerIds=[489], isEnable=False)
        set_skill(triggerIds=[490], isEnable=False)
        set_skill(triggerIds=[491], isEnable=False)
        set_skill(triggerIds=[492], isEnable=False)
        set_skill(triggerIds=[493], isEnable=False)
        set_skill(triggerIds=[494], isEnable=False)
        set_skill(triggerIds=[495], isEnable=False)
        set_skill(triggerIds=[496], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬31()


class 스킬31(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[485], isEnable=True)
        set_skill(triggerIds=[486], isEnable=True)
        set_skill(triggerIds=[487], isEnable=True)
        set_skill(triggerIds=[488], isEnable=True)
        set_skill(triggerIds=[489], isEnable=True)
        set_skill(triggerIds=[490], isEnable=True)
        set_skill(triggerIds=[491], isEnable=True)
        set_skill(triggerIds=[492], isEnable=True)
        set_skill(triggerIds=[493], isEnable=True)
        set_skill(triggerIds=[494], isEnable=True)
        set_skill(triggerIds=[495], isEnable=True)
        set_skill(triggerIds=[496], isEnable=True)
        set_skill(triggerIds=[497], isEnable=True)
        set_skill(triggerIds=[498], isEnable=True)
        set_skill(triggerIds=[499], isEnable=True)
        set_skill(triggerIds=[500], isEnable=True)
        set_skill(triggerIds=[501], isEnable=True)
        set_skill(triggerIds=[502], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬32대기()


class 스킬32대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[485], isEnable=False)
        set_skill(triggerIds=[486], isEnable=False)
        set_skill(triggerIds=[487], isEnable=False)
        set_skill(triggerIds=[488], isEnable=False)
        set_skill(triggerIds=[489], isEnable=False)
        set_skill(triggerIds=[490], isEnable=False)
        set_skill(triggerIds=[491], isEnable=False)
        set_skill(triggerIds=[492], isEnable=False)
        set_skill(triggerIds=[493], isEnable=False)
        set_skill(triggerIds=[494], isEnable=False)
        set_skill(triggerIds=[495], isEnable=False)
        set_skill(triggerIds=[496], isEnable=False)
        set_skill(triggerIds=[497], isEnable=False)
        set_skill(triggerIds=[498], isEnable=False)
        set_skill(triggerIds=[499], isEnable=False)
        set_skill(triggerIds=[500], isEnable=False)
        set_skill(triggerIds=[501], isEnable=False)
        set_skill(triggerIds=[502], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬32()


class 스킬32(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[491], isEnable=True)
        set_skill(triggerIds=[492], isEnable=True)
        set_skill(triggerIds=[493], isEnable=True)
        set_skill(triggerIds=[494], isEnable=True)
        set_skill(triggerIds=[495], isEnable=True)
        set_skill(triggerIds=[496], isEnable=True)
        set_skill(triggerIds=[497], isEnable=True)
        set_skill(triggerIds=[498], isEnable=True)
        set_skill(triggerIds=[499], isEnable=True)
        set_skill(triggerIds=[500], isEnable=True)
        set_skill(triggerIds=[501], isEnable=True)
        set_skill(triggerIds=[502], isEnable=True)
        set_skill(triggerIds=[503], isEnable=True)
        set_skill(triggerIds=[504], isEnable=True)
        set_skill(triggerIds=[505], isEnable=True)
        set_skill(triggerIds=[506], isEnable=True)
        set_skill(triggerIds=[507], isEnable=True)
        set_skill(triggerIds=[508], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 스킬33대기()


class 스킬33대기(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=0)
        set_skill(triggerIds=[491], isEnable=False)
        set_skill(triggerIds=[492], isEnable=False)
        set_skill(triggerIds=[493], isEnable=False)
        set_skill(triggerIds=[494], isEnable=False)
        set_skill(triggerIds=[495], isEnable=False)
        set_skill(triggerIds=[496], isEnable=False)
        set_skill(triggerIds=[497], isEnable=False)
        set_skill(triggerIds=[498], isEnable=False)
        set_skill(triggerIds=[499], isEnable=False)
        set_skill(triggerIds=[500], isEnable=False)
        set_skill(triggerIds=[501], isEnable=False)
        set_skill(triggerIds=[502], isEnable=False)
        set_skill(triggerIds=[503], isEnable=False)
        set_skill(triggerIds=[504], isEnable=False)
        set_skill(triggerIds=[505], isEnable=False)
        set_skill(triggerIds=[506], isEnable=False)
        set_skill(triggerIds=[507], isEnable=False)
        set_skill(triggerIds=[508], isEnable=False)

    def on_tick(self) -> state.State:
        if true():
            return 스킬33()


class 스킬33(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[497], isEnable=True)
        set_skill(triggerIds=[498], isEnable=True)
        set_skill(triggerIds=[499], isEnable=True)
        set_skill(triggerIds=[500], isEnable=True)
        set_skill(triggerIds=[501], isEnable=True)
        set_skill(triggerIds=[502], isEnable=True)
        set_skill(triggerIds=[503], isEnable=True)
        set_skill(triggerIds=[504], isEnable=True)
        set_skill(triggerIds=[505], isEnable=True)
        set_skill(triggerIds=[506], isEnable=True)
        set_skill(triggerIds=[507], isEnable=True)
        set_skill(triggerIds=[508], isEnable=True)
        set_skill(triggerIds=[509], isEnable=True)
        set_skill(triggerIds=[510], isEnable=True)
        set_skill(triggerIds=[511], isEnable=True)
        set_skill(triggerIds=[512], isEnable=True)
        set_skill(triggerIds=[513], isEnable=True)
        set_skill(triggerIds=[514], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 끝()


class 끝(state.State):
    def on_enter(self):
        set_skill(triggerIds=[497], isEnable=False)
        set_skill(triggerIds=[498], isEnable=False)
        set_skill(triggerIds=[499], isEnable=False)
        set_skill(triggerIds=[500], isEnable=False)
        set_skill(triggerIds=[501], isEnable=False)
        set_skill(triggerIds=[502], isEnable=False)
        set_skill(triggerIds=[503], isEnable=False)
        set_skill(triggerIds=[504], isEnable=False)
        set_skill(triggerIds=[505], isEnable=False)
        set_skill(triggerIds=[506], isEnable=False)
        set_skill(triggerIds=[507], isEnable=False)
        set_skill(triggerIds=[508], isEnable=False)
        set_skill(triggerIds=[509], isEnable=False)
        set_skill(triggerIds=[510], isEnable=False)
        set_skill(triggerIds=[511], isEnable=False)
        set_skill(triggerIds=[512], isEnable=False)
        set_skill(triggerIds=[513], isEnable=False)
        set_skill(triggerIds=[514], isEnable=False)


