using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004045: Erda
/// </summary>
public class _11004045 : NpcScript {
    internal _11004045(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010063$ 
                // - I'm so very sorry... 
                return true;
            case 10:
                // $script:0614185307010064$ 
                // - I'm so very sorry... 
                return true;
            default:
                return true;
        }
    }
}
