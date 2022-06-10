using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004298: Ghost
/// </summary>
public class _11004298 : NpcScript {
    internal _11004298(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1002141907011381$ 
                // - Clean clean clean... 
                return true;
            case 30:
                // $script:1002141907011384$ 
                // - It's my job to keep this hotel clean, and I'm darn good at it! Except... there's this one thing I can't seem to tidy up!
                switch (selection) {
                    // $script:1002141907011385$
                    // - What might that be?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1002141907011386$ 
                // - Over there, in the sofa by the window. There are papers stuck in there that I can't seem to get loose. Did someone put those there on purpose? 
                return true;
            default:
                return true;
        }
    }
}
