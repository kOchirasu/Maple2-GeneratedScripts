using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000126: Poffo
/// </summary>
public class _11000126 : NpcScript {
    internal _11000126(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000545$ 
                // - Um... Hi. What is it?
                return true;
            case 30:
                // $script:0831180407000548$ 
                // - I mustered up the courage to come here, but now I'm too scared to move. I have to hunt monsters, or get the treasure from the cliff. I need the money...
                return true;
            default:
                return true;
        }
    }
}
