using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004054: Rejan
/// </summary>
public class _11004054 : NpcScript {
    internal _11004054(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010081$ 
                // - My master and the leaders of Terrun Calibre will definitely return. Until then, I'll carry out their will.
                return true;
            case 10:
                // $script:0614185307010082$ 
                // - My master and the leaders of Terrun Calibre will definitely return. Until then, I'll carry out their will.
                return true;
            default:
                return true;
        }
    }
}
