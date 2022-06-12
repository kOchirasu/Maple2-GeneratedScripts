using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003169: Joddy
/// </summary>
public class _11003169 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20;30
    }

    // Select 0:
    // $script:0516084007008474$
    // - This place is dark. And wet. Just the sort of place I'd do crimes if <i>I</i> was a bad guy.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0516084007008475$
                // - You saved me. Again. Jeez, I can't do anything right...
                switch (selection) {
                    // $script:0516084007008476$
                    // - You'll get the hang of it.
                    case 0:
                        return 11;
                    // $script:0516084007008477$
                    // - Get a grip.
                    case 1:
                        return 12;
                }
                return -1;
            case (11, 0):
                // $script:0516084007008478$
                // - Y-yeah! Next time, it's <i>my</i> turn to save <i>you</i>!
                return -1;
            case (12, 0):
                // $script:0516084007008479$
                // - Y-yes, $male:sir,female:ma'am$. <font size='20'>Aw man...</font>
                return -1;
            case (20, 0):
                // $script:0516084007008480$
                // - If I was stronger, you wouldn't have to go through so much trouble. I'm sorry I'm such a burden...
                return -1;
            case (30, 0):
                // $script:0516084007008481$
                // - How'd you get to be so strong, $MyPCName$?
                switch (selection) {
                    // $script:0516084007008482$
                    // - The secret is hard work.
                    case 0:
                        return 31;
                    // $script:0516084007008483$
                    // - What can I say? I was born this good.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0516084007008484$
                // - Hard work! I can do that. I'll start tomorrow! Or maybe next week...
                return -1;
            case (32, 0):
                // $script:0516084007008485$
                // - It's all natural talent? Oh man. I guess there's no hope for me...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            (12, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
