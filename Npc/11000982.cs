using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000982: Christopher
/// </summary>
public class _11000982 : NpcScript {
    internal _11000982(INpcScriptContext context) : base(context) {
        // TODO: Condition $script:0831180610001142$
        // Id = 1;
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610001141$ 
                // - Ahoy!  
                return true;
            case 1:
                // $script:0831180610001142$ 
                // - $MyPCName$, what you did was fantastic!
Now all you have to do is return to $map:02000062$ for a debriefing.
It's 4,000 mesos to go back on the ship, the same fare as before.
Do you want to depart for $map:02000062$ now? 
                return true;
            case 40:
                // $script:0831180610001146$ 
                // - You need something? 
                switch (selection) {
                    // $script:0831180610001147$
                    // - Can I board the ship?
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0831180610001148$
                    // - I'm just looking around.
                    case 1:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180610001149$ 
                // - The <i>Marco</i> only transports adventurers who are carrying out special missions in $map:02000068$. Other adventurers and ordinary civilians can't board. 
                return true;
            case 42:
                // $script:0831180610001150$ 
                // - This place isn't too safe. You'd better be careful. 
                return true;
            case 50:
                // $script:0831180610001151$ 
                // - The operation of the Marco is mostly paid by the $map:02000068$, so the passengers only pay a small fare of 4,000 mesos. If you want to board, that's your price. 
                return true;
            default:
                return true;
        }
    }
}
