using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001838: Joddy
/// </summary>
public class _11001838 : NpcScript {
    internal _11001838(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1111015907007375$ 
                // - Ah... What should I do?
                return true;
            case 30:
                // $script:1111015907007378$ 
                // - I thought everything'd work out if I could just get into the army. Now I'm not sure I'm cut out for this...
                switch (selection) {
                    // $script:1111015907007379$
                    // - I believe in you.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:1111015907007380$
                    // - Stop slacking and train harder!
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:1111015907007381$ 
                // - Th-thank you! I'll do my best. 
                return true;
            case 32:
                // $script:1111015907007382$ 
                // - T-train harder... Yeah, that'll help...
                return true;
            default:
                return true;
        }
    }
}
