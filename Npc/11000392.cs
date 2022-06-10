using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000392: Timus
/// </summary>
public class _11000392 : NpcScript {
    internal _11000392(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001592$ 
                // - Huh?
                return true;
            case 20:
                // $script:0831180407001594$ 
                // - Did you hear the court was canceled? I thought it would be a big to-do, so I arrived two weeks ago.
                // $script:0831180407001595$ 
                // - And now it's canceled! Argh, I stayed at the hotel for two weeks for nothing!
                return true;
            default:
                return true;
        }
    }
}
