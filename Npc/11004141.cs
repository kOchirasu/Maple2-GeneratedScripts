using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004141: Kaitlyn
/// </summary>
public class _11004141 : NpcScript {
    internal _11004141(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010553$ 
                // - What is it?
                return true;
            case 10:
                // $script:0806025707010554$ 
                // - I wish he wore glasses. He's so intelligent and sensitive... It would be perfect... 
                return true;
            default:
                return true;
        }
    }
}
