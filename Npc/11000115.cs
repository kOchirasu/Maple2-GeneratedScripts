using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000115: Elly
/// </summary>
public class _11000115 : NpcScript {
    internal _11000115(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000483$ 
                // - What is it?
                return true;
            case 40:
                // $script:0831180407000487$ 
                // - Hmph! Just as well. I hope the road stays destroyed forever.
                switch (selection) {
                    // $script:0831180407000488$
                    // - Why's that?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407000489$ 
                // - Smith left for $map:02000001$ to see the court instead of staying with me for my birthday. I don't need a boyfriend who cares more about the empress than me. I hope he'll never come back. Hmph!
                return true;
            default:
                return true;
        }
    }
}
