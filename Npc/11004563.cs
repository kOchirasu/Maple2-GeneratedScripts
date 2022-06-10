using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004563: Allon
/// </summary>
public class _11004563 : NpcScript {
    internal _11004563(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0220211107014520$ 
                // - Hm?
                return true;
            case 10:
                // $script:0220211107014521$ 
                // - Hm?
                // $script:0220211107014522$ 
                // - I had a feeling I'd see you here.
                switch (selection) {
                    // $script:0220211107014523$
                    // - I didn't think you were into this kind of thing.
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:0220211107014524$ 
                // - Come now. I wouldn't pass up the chance to fight the hero of Tria.
                // $script:0220211107014525$ 
                // - I look forward to our match.
                return true;
            default:
                return true;
        }
    }
}
