using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003648: Poppy
/// </summary>
public class _11003648 : NpcScript {
    internal _11003648(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109121007009194$ 
                // - What a creepy place...
                return true;
            case 10:
                // $script:1109121007009195$ 
                // - Oh, $MyPCName$! What a pleasant surprise.
                switch (selection) {
                    // $script:1109121007009196$
                    // - Have we met?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109121007009197$ 
                // - You wound me. We've talked at length, my friend! Of course, I was wearing a different face at the time...
                switch (selection) {
                    // $script:1109121007009198$
                    // - I honestly have no idea who you are.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109121007009199$ 
                // - A pity. Anyway, you must be here about the dragon-man.
                switch (selection) {
                    // $script:1109121007009200$
                    // - Who said anything about a dragon-man?
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:1109121007009201$ 
                // - Don't be so transparent, my friend. I already knew why you were here from the beginning.
                switch (selection) {
                    // $script:1109121007009202$
                    // - $npcName:11003535[gender:1]$ sent me...
                    case 0:
                        Id = 14;
                        return false;
                }
                return true;
            case 14:
                // $script:1109121007009203$ 
                // - Then please pass my message along to her: "Torch. Jar. Treasure chest."
                switch (selection) {
                    // $script:1109121007009204$
                    // - All right.
                    case 0:
                        Id = 15;
                        return false;
                }
                return true;
            case 15:
                // $script:1109121007009205$ 
                // - I would advise you leave this place as soon as you can. It's most eerie here...
                return true;
            default:
                return true;
        }
    }
}
