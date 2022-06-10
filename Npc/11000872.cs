using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000872: Skan
/// </summary>
public class _11000872 : NpcScript {
    internal _11000872(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003151$ 
                // - What? Do you have something to say to me? 
                return true;
            case 30:
                // $script:0831180407003154$ 
                // - Don't rely on Fairy Dew too much. This place is teeming with monsters that are stronger than you. 
                return true;
            default:
                return true;
        }
    }
}
