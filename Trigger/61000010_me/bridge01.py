""" trigger/61000010_me/bridge01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000041], state=1)
        self.set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000041], stateValue=0):
            self.set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110], visible=False, arg3=0, delay=100, scale=1)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
