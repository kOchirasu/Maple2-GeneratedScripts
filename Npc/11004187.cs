using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004187: Pia
/// </summary>
public class _11004187 : NpcScript {
    internal _11004187(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010636$ 
                // - Hm...
                return true;
            case 10:
                // $script:0806025707010637$ 
                // - Ah, so plush and comfy!
                return true;
            default:
                return true;
        }
    }
}
