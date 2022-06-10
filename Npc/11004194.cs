using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004194: Eupheria
/// </summary>
public class _11004194 : NpcScript {
    internal _11004194(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0813101707010956$ 
                // - ...
                return true;
            case 10:
                // $script:0813101707010957$ 
                // - The Green Lapenta... The flow of life... All these memories...
                return true;
            default:
                return true;
        }
    }
}
