using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001120: Lucky Wheel
/// </summary>
public class _11001120 : NpcScript {
    protected override int First() {
        // TODO: Job 30
        // TODO: RandomPick 40
    }

    // Select 0:
    // $script:0909140310001156$
    // - Spin the $npc:11001120$ for just 1 $item:30000406$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0909140310001157$
                // - Look at all those $itemPlural:30000406$> you've got! You're sitting pretty! Why don't you invest them in a chance to spin the $npc:11001120$? Could be a wise investment, indeed!
                return 30;
            case (30, 1):
                // functionID=1 
                // $script:0909140310001158$
                // - Spin the wheel for a chance at great prizes! You know you want to.
                return 30;
            case (30, 2):
                // $script:0909140310001159$
                // - Here's hoping Lady Luck's on your side!
                return -1;
            case (40, 0):
                // $script:0909140310001160$
                // - To take a spin on the $npc:11001120$, you need $itemPlural:30000406$. But good news! You can get 1 $item:30000406$ in your mailbox every 20 minutes, up to 9 times a day.
                return 40;
            case (40, 1):
                // $script:0909140310001161$
                // - If you get a $item:30000406$, don't forget to come to $map:02000064$!
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
