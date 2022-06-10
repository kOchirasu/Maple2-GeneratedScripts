using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003169: Joddy
/// </summary>
public class _11003169 : NpcScript {
    internal _11003169(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0516084007008474$ 
                // - This place is dark. And wet. Just the sort of place I'd do crimes if <i>I</i> was a bad guy.
                return true;
            case 10:
                // $script:0516084007008475$ 
                // - You saved me. Again. Jeez, I can't do anything right...
                switch (selection) {
                    // $script:0516084007008476$
                    // - You'll get the hang of it.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0516084007008477$
                    // - Get a grip.
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 11:
                // $script:0516084007008478$ 
                // - Y-yeah! Next time, it's <i>my</i> turn to save <i>you</i>!
                return true;
            case 12:
                // $script:0516084007008479$ 
                // - Y-yes, $male:sir,female:ma'am$. <font size='20'>Aw man...</font>
                return true;
            case 20:
                // $script:0516084007008480$ 
                // - If I was stronger, you wouldn't have to go through so much trouble. I'm sorry I'm such a burden...
                return true;
            case 30:
                // $script:0516084007008481$ 
                // - How'd you get to be so strong, $MyPCName$?
                switch (selection) {
                    // $script:0516084007008482$
                    // - The secret is hard work.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0516084007008483$
                    // - What can I say? I was born this good.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0516084007008484$ 
                // - Hard work! I can do that. I'll start tomorrow! Or maybe next week...
                return true;
            case 32:
                // $script:0516084007008485$ 
                // - It's all natural talent? Oh man. I guess there's no hope for me...
                return true;
            default:
                return true;
        }
    }
}
