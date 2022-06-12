using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000475: Wheel of Joy
/// </summary>
public class _11000475 : NpcScript {
    protected override int First() {
        // TODO: Job 30
        // TODO: RandomPick 40
    }

    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180610000459$
                // - Spin, spin!
                return 30;
            case (30, 1):
                // functionID=1 
                // $script:0831180610000460$
                // - Congratulations, you're a winner!
                //   You get to draw a <font color="#ffd200">wondrous item</font>!
                return 30;
            case (30, 2):
                // $script:0831180610000461$
                // - Come on, spin the roulette for your chance to win amazing items!
                //   May luck be with you, <font color="#ffd200">$MyPCName$</font>!
                return -1;
            case (40, 0):
                // $script:0831180610000462$
                // - You get only <font color="#ffd200">one chance to spin $npc:11000475$</font>.
                //   Want to spin again? Then you'll have to win again!
                return 40;
            case (40, 1):
                // $script:0831180610000463$
                // - I hope you come back and win again soon!
                //   Have a lucky journey!
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
