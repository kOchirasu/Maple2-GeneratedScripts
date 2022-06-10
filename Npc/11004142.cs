using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004142: Merin
/// </summary>
public class _11004142 : NpcScript {
    internal _11004142(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010555$ 
                // - Wow! 
                return true;
            case 10:
                // $script:0806025707010556$ 
                // - My favorite game is hide-and-seek! 
                return true;
            default:
                return true;
        }
    }
}
