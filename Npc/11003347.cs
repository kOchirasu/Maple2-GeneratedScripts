using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003347: Ralph's Lackey
/// </summary>
public class _11003347 : NpcScript {
    internal _11003347(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0517164307008490$ 
                // - I've never met someone as strong as you.
                return true;
            case 30:
                // $script:0517164307008493$ 
                // - I can take you to the boss if you're lost.
                switch (selection) {
                    // $script:0517164307008494$
                    // - Lead the way.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0517164307008495$ functionID=1 
                // - Sure thing. Right this way.
                return true;
            default:
                return true;
        }
    }
}
