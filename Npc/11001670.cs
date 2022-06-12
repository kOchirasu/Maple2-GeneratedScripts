using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001670: Hart
/// </summary>
public class _11001670 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0620231807006389$
    // - Welcome, $MyPCName$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0620231807006393$
                // - For one spin of the $npcName:11001654$, you need 3 $itemPlural:30000554$. You'll get 3 $itemPlural:30000554$ in your mailbox every day just for logging in. You'll also get bonus coins as you spend more time in Maple World. And let's not forget that many of our events also award coins for joining in!
                return 40;
            case (40, 1):
                // $script:0620231807006394$
                // - If you have $itemPlural:30000554$ to burn, be sure to come to $map:63000032$!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
