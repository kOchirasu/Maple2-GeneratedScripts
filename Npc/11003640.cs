using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003640: Heidi
/// </summary>
public class _11003640 : NpcScript {
    internal _11003640(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109121007009114$ 
                // - When she asked if I like it hot, I had no idea she meant THIS... 
                return true;
            case 10:
                // $script:1109121007009115$ 
                // - How can people <i>live</i> like this! At least they could turn on the AC... Are you on vacation here, too? 
                switch (selection) {
                    // $script:1109121007009116$
                    // - That's right.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109121007009117$ 
                // - You liar. You've got $npcName:11003535[gender:1]$'s fingerprints all over you. 
                switch (selection) {
                    // $script:1109121007009118$
                    // - <i>All</i> over me?
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109121007009119$ 
                // - Don't look so surprised. Any trained Dark Wind agent knows the signs. Anyway, I'm guessing you're here for my message? 
                switch (selection) {
                    // $script:1109121007009120$
                    // - You guessed right.
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:1109121007009121$ 
                // - Listen closely. "Jeans. Air conditioner! Poker?" 
                switch (selection) {
                    // $script:1109121007009122$
                    // - Is that really the message?
                    case 0:
                        Id = 14;
                        return false;
                }
                return true;
            case 14:
                // $script:1109121007009123$ 
                // - Oh, please. Anyway, I need some space, so shoo. This heat is killing me... 
                return true;
            default:
                return true;
        }
    }
}
