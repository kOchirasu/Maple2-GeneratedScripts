using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001458: Fin
/// </summary>
public class _11001458 : NpcScript {
    internal _11001458(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1222171407005462$ 
                // - What is it? 
                return true;
            case 30:
                // $script:1222171407005465$ 
                // - We aren't some fly-by-night operation. We're the Blackstars! 
                return true;
            default:
                return true;
        }
    }
}
