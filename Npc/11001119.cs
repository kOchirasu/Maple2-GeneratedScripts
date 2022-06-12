using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001119: Hart
/// </summary>
public class _11001119 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:0909142907003757$
    // - Welcome, $MyPCName$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0909142907003761$
                // - Did you come to join the event? I'm sorry, but you forgot the most important thing. To spin this $npcName:11001120$, you need a $item:30000406$. Luckily, they're easy to get!
                return 40;
            case (40, 1):
                // $script:0914175707003915$
                // - You'll get a <i>free cake</i> in the mail every 20 minutes, just for having a good time in Maple World! You can receive up to <b>9 a day</b>. If you get a hold of a $item:30000406$, be sure to swing by $map:02000064:$!
                return -1;
            case (50, 0):
                // $script:0909142907003762$
                // - Oh good, you have a $item:30000406$! You can use $itemPlural:30000406$ to spin this here $npcName:11001120$ next to me for a chance to win great prizes. Come on, why not try it?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
