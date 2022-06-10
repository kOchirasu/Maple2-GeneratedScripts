using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000649: Prisoner 170121
/// </summary>
public class _11000649 : NpcScript {
    internal _11000649(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002656$ 
                // - What are you looking at?
                return true;
            case 40:
                // $script:0831180407002660$ 
                // - Another tourist? Come to see all the animals in their cages?
                switch (selection) {
                    // $script:0831180407002661$
                    // - How did you end up in here?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407002662$ 
                // - I swore, and apparently that's SO wrong that they had to throw me into prison?
                return true;
            case 50:
                // $script:1211023307004934$ 
                // - Another tourist? Come to see all the animals in their cages?
                switch (selection) {
                    // $script:1211023307004935$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:1211023307004936$ 
                // - No. Get lost.
                return true;
            default:
                return true;
        }
    }
}
