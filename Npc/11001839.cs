using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001839: Joddy
/// </summary>
public class _11001839 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1020165907007297$
    // - Ah... What should I do?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1020165907007300$
                // - I can't wait to become a full-fledged guard.
                switch (selection) {
                    // $script:1020165907007301$
                    // - Did you run into any mushrooms on the way here?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1020165907007302$
                // - M-mushrooms? Are there mushrooms here? Oh no... 
                //   <font color="#909090">(All the color drains from $npcName:11001839[gender:0]$'s face. What terrible happening has made him so afraid of something as innocuous as mushrooms?)</font>
                switch (selection) {
                    // $script:1020165907007303$
                    // - Relax, I was only kidding.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1020165907007304$
                // - H-how could you do that to me, $MyPCName$? I... I thought we were friends. Have you just been pretending to like me all this time?
                //   <font color="#909090">($npcName:11001839[gender:0]$'s eyes begin to water.)</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
