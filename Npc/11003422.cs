using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003422: Niya
/// </summary>
public class _11003422 : NpcScript {
    internal _11003422(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008631$ 
                // - Ooof...
                return true;
            case 10:
                // $script:0706160807008632$ 
                // - Ooof...
                return true;
            default:
                return true;
        }
    }
}
