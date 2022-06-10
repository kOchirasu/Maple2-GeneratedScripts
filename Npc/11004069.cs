using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004069: Cheez
/// </summary>
public class _11004069 : NpcScript {
    internal _11004069(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0619202207010143$ 
                // - It's breezy up here!
                return true;
            case 10:
                // $script:0619202207010144$ 
                // - It's breezy up here!
                // $script:0619202207010145$ 
                // - Huh? What do <i>you</i> want?
                switch (selection) {
                    // $script:0619202207010146$
                    // - $npcName:11000367$'s owner is worried...
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0619202207010147$ 
                // - That's too bad. $npcName:11000367$ and I were meant for each other. It was fate.
                switch (selection) {
                    // $script:0619202207010148$
                    // - How'd you two meet, anyway?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0619202207010149$ 
                // - How is that any of your business? Let's just say that Skittle saved me from a really tough situation.
                // $script:0619202207010150$ 
                // - You should just wish us happiness, okay?
                return true;
            default:
                return true;
        }
    }
}
