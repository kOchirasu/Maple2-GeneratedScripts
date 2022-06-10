using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001074: Allison
/// </summary>
public class _11001074 : NpcScript {
    internal _11001074(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003663$ 
                // - Hello.
                return true;
            case 30:
                // $script:0831180407003666$ 
                // - Every single picture here is drawn by a child. Amazing, right?
                return true;
            default:
                return true;
        }
    }
}
