using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004568: Mika
/// </summary>
public class _11004568 : NpcScript {
    internal _11004568(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0220211107014560$ 
                // - Aaaah. 
                return true;
            case 10:
                // $script:0220211107014561$ 
                // - Hmm hm hummm! 
                // $script:0220211107014562$ 
                // - Huh? Did you say something? 
                switch (selection) {
                    // $script:0220211107014563$
                    // - Take off your headphones!
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:0220211107014564$ 
                // - Good idea! There we go. You're here for the Queen Bean Rumble? 
                // $script:0220211107014565$ 
                // - Me too! I bet you didn't know I could fight. 
                switch (selection) {
                    // $script:0220211107014566$
                    // - I haven't thought about it.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 30:
                // $script:0220211107014567$ 
                // - Well, I can, and I'm really good at it, too. 
                // $script:0220211107014568$ 
                // - In fact, I'm the very first fighter the Pink Beans invited. It wasn't easy for them, either. Karkar isn't exactly in their backyard. 
                // $script:0220211107014569$ 
                // - Anyway, I'll see you in the fight! 
                return true;
            default:
                return true;
        }
    }
}
