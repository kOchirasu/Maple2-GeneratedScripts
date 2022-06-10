using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003423: Suri
/// </summary>
public class _11003423 : NpcScript {
    internal _11003423(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008633$ 
                // - Ugh...
                return true;
            case 10:
                // $script:0706160807008634$ 
                // - Ugh...
                return true;
            default:
                return true;
        }
    }
}
