using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004154: Unita
/// </summary>
public class _11004154 : NpcScript {
    internal _11004154(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010579$ 
                // - Hello.
                return true;
            case 10:
                // $script:0806025707010580$ 
                // - Wow, just look at that ocean! This place is so different from $map:02000051$. It really is nice to get out and explore the world once in a while.
                return true;
            default:
                return true;
        }
    }
}
