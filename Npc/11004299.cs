using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004299: Ghost
/// </summary>
public class _11004299 : NpcScript {
    internal _11004299(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1002141907011387$ 
                // - Everything in its place. 
                return true;
            case 30:
                // $script:1002141907011390$ 
                // - A guest came the other day, but I haven't seen him lately. I do hope he's having a nice visit.
                switch (selection) {
                    // $script:1002141907011391$
                    // - Who are you talking about?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1002141907011392$ 
                // - A gentleman with a large briefcase. None of the other ghosts recognized him, but it seems that he was an acquaintance of mademoiselle.
                switch (selection) {
                    // $script:1002141907011393$
                    // - Mademoiselle?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1002141907011394$ 
                // - Yes, the lady of the hotel. There were evil thoughts in her mind when she met the gentleman. A ghost has a sixth sense about these things, you know.
                return true;
            default:
                return true;
        }
    }
}
