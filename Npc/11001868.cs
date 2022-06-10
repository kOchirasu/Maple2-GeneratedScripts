using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001868: Rachael
/// </summary>
public class _11001868 : NpcScript {
    internal _11001868(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1213150207007549$ 
                // - Ah, nice to see you! 
                return true;
            case 20:
                // $script:1213150207007551$ 
                // - This mine is run by the Nerman Guild. We've got all the materials a blacksmith might need. 
                return true;
            default:
                return true;
        }
    }
}
