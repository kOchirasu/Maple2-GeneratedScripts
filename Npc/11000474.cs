using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000474: Wheel of Joy
/// </summary>
public class _11000474 : NpcScript {
    protected override int First() {
        // TODO: Job 30
        // TODO: RandomPick 40
    }

    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180610000452$
                // - Spin, spin!
                return 30;
            case (30, 1):
                // functionID=1 
                // $script:0831180610000453$
                // - Welcome!
                //   $npc:11000474$ is filled with <font color="#ffd200">wondrous items</font>!
                return 30;
            case (30, 2):
                // $script:0831180610000454$
                // - Spin $npc:11000474$ for your chance to win the wondrous items!
                //   May luck be with you, <font color="#ffd200">$MyPCName$</font>!
                return -1;
            case (40, 0):
                // $script:0831180610000455$
                // - You get only <font color="#ffd200">one chance to spin $npc:11000474$</font>.
                //   Want to spin $npc:11000474$ again? Then <font color="#ffd200">find another hat</font>!
                return 40;
            case (40, 1):
                // $script:0831180610000456$
                // - This might sound crazy, but if you come across a hat in a field, don't hesitate to throw yourself inside of it! You heard me!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Roulette,
            (30, 2) => NpcTalkButton.Empty,
            _ => NpcTalkButton.None,
        };
    }
}
