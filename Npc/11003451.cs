using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003451: Namid
/// </summary>
public class _11003451 : NpcScript {
    internal _11003451(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008657$ 
                // - Who will protect $map:02000051$? 
                return true;
            case 10:
                // $script:0706160807008658$ 
                // - Who will protect $map:02000051$? 
                return true;
            default:
                return true;
        }
    }
}
