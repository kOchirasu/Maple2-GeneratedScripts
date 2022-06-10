using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003395: Nipa
/// </summary>
public class _11003395 : NpcScript {
    internal _11003395(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008595$ 
                // - 
                return true;
            case 10:
                // $script:0706160807008596$ 
                // - 
                return true;
            default:
                return true;
        }
    }
}
