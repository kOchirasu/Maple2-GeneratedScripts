using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000460: Adam
/// </summary>
public class _11000460 : NpcScript {
    internal _11000460(INpcScriptContext context) : base(context) {
        Id = 50;
        // TODO: RandomPick 50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002044$ 
                // - What is it?
                return true;
            case 50:
                // $script:0831180407002047$ 
                // - Hey, I know what you're thinking, and that's not why I'm here at $map:02000107$. I'm all natural! No cosmetic surgery here! I just came to get some fresh air, and check out the latest beauty... trends. While I'm at it.
                return true;
            default:
                return true;
        }
    }
}
