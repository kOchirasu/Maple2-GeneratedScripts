using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000060: Betty
/// </summary>
public class _11000060 : NpcScript {
    internal _11000060(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000269$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407000272$ 
                // - $MyPCName$, are you also going to the mainland?
                switch (selection) {
                    // $script:0831180407000273$
                    // - That's right.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0831180407000274$
                    // - I don't know.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000275$ 
                // - You've made a good decision. I've stayed on this small island my whole life, but I want you to go see more of the this world.
                // $script:0831180407000276$ 
                // - While you're there at the court, you might as well explore the rest of the mainland. I'd love for you to come back with tales of the things you saw.
                return true;
            case 32:
                // $script:0831180407000277$ 
                // - Cross the sea to the mainland to experience more of what this world can offer.Go on, don't be afraid.
                return true;
            default:
                return true;
        }
    }
}
