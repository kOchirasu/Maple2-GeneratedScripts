using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004158: Miel
/// </summary>
public class _11004158 : NpcScript {
    internal _11004158(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010587$ 
                // - It's so close, but I can't reach it. It comes to me in the night and vanishes at dawn.
                return true;
            case 10:
                // $script:0806025707010588$ 
                // - Many things shine, not all of them valuable.
                return true;
            default:
                return true;
        }
    }
}
