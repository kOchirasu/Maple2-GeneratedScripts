using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000251: Wei Hong
/// </summary>
public class _11000251 : NpcScript {
    internal _11000251(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001049$ 
                // - What brings you here? 
                return true;
            case 20:
                // $script:0831180407001051$ 
                // - My organization is using $map:02000216$ as a foothold to expand its business to other areas. You didn't think we'd stay in the shadows forever, did you? Don't be ridiculous.   
                return true;
            case 30:
                // $script:0831180407001052$ 
                // - ...Get lost. 
                return true;
            default:
                return true;
        }
    }
}
