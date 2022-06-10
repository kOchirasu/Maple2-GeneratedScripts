using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003647: Olive
/// </summary>
public class _11003647 : NpcScript {
    internal _11003647(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109121007009186$ 
                // - So much to do, so much mortal danger...
                return true;
            case 10:
                // $script:1109121007009187$ 
                // - What's have we here? A foreigner, in a place like this?
                switch (selection) {
                    // $script:1109121007009188$
                    // - I'm here on business.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109121007009189$ 
                // - In that case, $npcName:11003535[gender:1]$ must have sent you. I see she can't be bothered to visit me in person... as usual.
                switch (selection) {
                    // $script:1109121007009190$
                    // - Uh, she tells me that you're doing very important work.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109121007009191$ 
                // - That's kind of you to say, but I know the truth. Anyway, please tell her that I said, "Parrot. Shoes. Perfume."
                switch (selection) {
                    // $script:1109121007009192$
                    // - I'll make sure she gets the messsage.
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:1109121007009193$ 
                // - Please remind her that us agents get lonely sometimes, would you?
                return true;
            default:
                return true;
        }
    }
}
