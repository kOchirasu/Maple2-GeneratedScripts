using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004514: Mannstad Quartermaster
/// </summary>
public class _11004514 : NpcScript {
    internal _11004514(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1228182607012472$ 
                // - We'll be eating shoe leather at this rate... 
                return true;
            case 10:
                // $script:1228182607012473$ 
                // - We'll be eating shoe leather at this rate... 
                // $script:1228182607012474$ 
                // - With all the land routes cut off, we've been relying on air drops for supplies. We don't have the spare planes to keep that up forever, though. If something doesn't happen soon, the fortress will fall. 
                return true;
            default:
                return true;
        }
    }
}
