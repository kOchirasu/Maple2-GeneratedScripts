using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004490: Valens
/// </summary>
public class _11004490 : NpcScript {
    internal _11004490(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012318$ 
                // - Hm? Oh, you're that $male:fellow,female:lady$ from Sky Fortress!
                return true;
            case 10:
                // $script:1227192907012319$ 
                // - Hm? Oh, you're that $male:fellow,female:lady$ from Sky Fortress!
                // $script:1227192907012320$ 
                // - Here to admire the architecture? It's breathtaking, isn't it?
                switch (selection) {
                    // $script:1227192907012321$
                    // - Not really.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012322$ 
                // - Balderdash! Surely even a hardened adventurer like you is moved by such grandeur. There's nothing like this in all of Maple World!
                // $script:1227192907012323$ 
                // - Why, this building is a testament to the power of science. Even though I'm standing here, I feel as if I'm witnessing some impossible dream.
                // $script:1227192907012324$ 
                // - Dr. $npcName:11004499[gender:0]$ will be over the moon when he sees this!
                switch (selection) {
                    // $script:0114162107012708$
                    // - Good luck with that.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0114162107012709$ 
                // - Thank you!
                return true;
            default:
                return true;
        }
    }
}
