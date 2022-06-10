using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004050: Rejan
/// </summary>
public class _11004050 : NpcScript {
    internal _11004050(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010073$ 
                // - Since none of Terrun Calibre elders are in a position to leave the island, I decided to come and help out. 
                return true;
            case 10:
                // $script:0614185307010074$ 
                // - Since none of Terrun Calibre elders are in a position to leave the island, I decided to come and help out. 
                return true;
            default:
                return true;
        }
    }
}
