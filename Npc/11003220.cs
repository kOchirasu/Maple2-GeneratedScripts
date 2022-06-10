using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003220: Joddy
/// </summary>
public class _11003220 : NpcScript {
    internal _11003220(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0404083307008245$ 
                // - And now we're fighting literal devils... 
                return true;
            case 10:
                // $script:0404083307008246$ 
                // - I never thought I'd miss my drill sergeant... 
                return true;
            default:
                return true;
        }
    }
}
