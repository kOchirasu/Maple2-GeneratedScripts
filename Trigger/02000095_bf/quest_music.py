""" trigger/02000095_bf/quest_music.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_effect(triggerIds=[101], visible=False)
        set_interact_object(triggerIds=[10000465], state=1)

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000465], arg2=0):
            return NPC대화()

    def on_exit(self):
        create_monster(spawnIds=[892])
        create_monster(spawnIds=[893])
        create_monster(spawnIds=[894])


class NPC대화(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=892, script='$02000095_BF__QUEST_MUSIC__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=893, script='$02000095_BF__QUEST_MUSIC__1$', arg4=2, arg5=2)
        set_conversation(type=1, spawnId=894, script='$02000095_BF__QUEST_MUSIC__2$', arg4=2, arg5=4)
        set_timer(timerId='1', seconds=8)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기시간()


class 대기시간(state.State):
    def on_enter(self):
        set_effect(triggerIds=[101], visible=True)
        destroy_monster(spawnIds=[892])
        destroy_monster(spawnIds=[893])
        destroy_monster(spawnIds=[894])
        set_timer(timerId='1', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


