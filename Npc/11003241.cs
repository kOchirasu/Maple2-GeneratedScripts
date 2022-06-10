using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003241: Ralph
/// </summary>
public class _11003241 : NpcScript {
    internal _11003241(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008138$ 
                // - Ugh! 
                return true;
            case 30:
                // $script:0403155707008141$ 
                // - $MyPCName$? Why?! 
                return true;
            default:
                return true;
        }
    }
}
