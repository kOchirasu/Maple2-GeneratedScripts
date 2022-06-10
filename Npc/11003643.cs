using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003643: Kevin
/// </summary>
public class _11003643 : NpcScript {
    internal _11003643(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109121007009142$ 
                // - Well done, well done. 
                return true;
            case 10:
                // $script:1109121007009143$ 
                // - You must be the new grad student. 
                switch (selection) {
                    // $script:1109121007009144$
                    // - Not exactly...
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109121007009145$ 
                // - No? Then you must be one of $npcName:11003535[gender:1]$'s $male:men,female:women$. There aren't many other reasons to come to this pit... 
                switch (selection) {
                    // $script:1109121007009146$
                    // - This can't be an easy posting.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109121007009147$ 
                // - It is what it is. Anyway, you're here for a coded message, right? "Queen. Ace of Spades. Ten of Clovers." 
                switch (selection) {
                    // $script:1109121007009148$
                    // - I'll pass that along.
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:1109121007009149$ 
                // - I really need to take some leave when this is all over. 
                return true;
            default:
                return true;
        }
    }
}
