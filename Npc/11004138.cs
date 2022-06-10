using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004138: Doctor Harold
/// </summary>
public class _11004138 : NpcScript {
    internal _11004138(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0730132107010541$ 
                // - Sigh, another patient?
                return true;
            case 10:
                // $script:0730132107010542$ 
                // - And just who's going to treat <i>my</i> injuries?
                return true;
            default:
                return true;
        }
    }
}
