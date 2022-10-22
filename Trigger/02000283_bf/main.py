""" trigger/02000283_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000427], state=2)
        set_interact_object(triggerIds=[10000430], state=2)
        set_interact_object(triggerIds=[10000431], state=2)
        set_interact_object(triggerIds=[10000432], state=2)
        set_interact_object(triggerIds=[10000433], state=2)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False) # mesh.xml 에 있던 내용 2001스폰 아이디의 몬스터가 전투 상태로 되기 전에 죽어버리면 mesh.xml 내용이 작동 안하는 버그가 있어서 mesh.xml  내용을 이 main.xml에 포함시키는 형태로 수정했음
        set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 준비()


class 준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001], arg2=False)
        create_monster(spawnIds=[1002], arg2=False)
        create_monster(spawnIds=[1003], arg2=False)
        create_monster(spawnIds=[1004], arg2=False)
        create_monster(spawnIds=[1005], arg2=False)
        create_monster(spawnIds=[1006], arg2=False)
        create_monster(spawnIds=[1007], arg2=False)
        create_monster(spawnIds=[1008], arg2=False)
        set_interact_object(triggerIds=[10000427], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000427], arg2=0):
            return 엘리트스폰()


class 엘리트스폰(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2001], arg2=False)
        show_guide_summary(entityId=20002818, textId=20002818, duration=5000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01') # mesh.xml 에 있던 내용 2001스폰 아이디의 몬스터가 전투 상태로 되기 전에 죽어버리면 mesh.xml 내용이 작동 안하는 버그가 있어서 mesh.xml  내용을 이 main.xml에 포함시키는 형태로 수정했음
        set_random_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355], visible=False, meshCount=56, arg4=0, delay=30)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
            show_guide_summary(entityId=20002813, textId=20002813)
            play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            set_mesh(triggerIds=[400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416], visible=True, arg3=0, arg4=100, arg5=0)
            return 소멸대기()


class 소멸대기(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 소멸()


class 소멸(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002813)


