using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003206: Mark
/// </summary>
public class _11003206 : NpcScript {
    internal _11003206(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0404083307008235$ 
                // - If it weren't for you, those thugs would have got me. I owe you.
                return true;
            case 10:
                // $script:0404083307008236$ 
                // - I'd be a goner if you hadn't shown up.
                return true;
            default:
                return true;
        }
    }
}
