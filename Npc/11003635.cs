using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003635: Chandler
/// </summary>
public class _11003635 : NpcScript {
    internal _11003635(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109121007009054$ 
                // - Science is the answer!
                return true;
            case 10:
                // $script:1109121007009055$ 
                // - Ah, greetings, fellow scientist! Are you here to discuss the latest theories in electromathography?
                switch (selection) {
                    // $script:1109121007009056$
                    // - I'm looking for someone, actually.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109121007009057$ 
                // - In that case, you've found the right person, $MyPCName$.
                switch (selection) {
                    // $script:1109121007009058$
                    // - How do you know me?
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109121007009059$ 
                // - Everyone in Dark Wind knows you.
                switch (selection) {
                    // $script:1109121007009060$
                    // - Then you must have a message for $npcName:11003535[gender:1]$.
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:1109121007009061$ 
                // - "Pancakes, with extra syrup!"
                switch (selection) {
                    // $script:1109121007009062$
                    // - If I give you pancakes, will you tell me the message?
                    case 0:
                        Id = 14;
                        return false;
                }
                return true;
            case 14:
                // $script:1109121007009063$ 
                // - That <i>is</i> the message. Now, about those theories...
                return true;
            default:
                return true;
        }
    }
}
