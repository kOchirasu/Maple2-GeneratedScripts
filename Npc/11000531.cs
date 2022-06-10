using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000531: Zorba
/// </summary>
public class _11000531 : NpcScript {
    internal _11000531(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002284$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:0831180407002287$ 
                // - Cough, cough... It's so dusty in here! I've had it with all these old books.  
                switch (selection) {
                    // $script:0831180407002288$
                    // - Are you really going to close your bookstore?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407002289$ 
                // - Well, I'm certainly thinking about it. Ha ha... My bookstore is the oldest business on $map:02000147$, you know. I'd rather keep it open, but I'm getting too old to run it on my own. 
                return true;
            case 40:
                // $script:0831180407002290$ 
                // - Do you like books? 
                switch (selection) {
                    // $script:0831180407002291$
                    // - Yep!
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0831180407002292$
                    // - Nope!
                    case 1:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407002293$ 
                // - Ha, do you? People like you amaze me. I've owned this store for over thirty years, but reading always puts me right to sleep. It's so boring. 
                // $script:0831180407002294$ 
                // - I'm glad not everyone feels like I do. I'd have long since shut down, ha! 
                return true;
            case 42:
                // $script:0831180407002295$ 
                // - You don't? Ha, you're just like me. I've owned this store for over thirty years, but reading always puts me right to sleep. It's so boring. Just between you and me, I've never finished a single book in my whole life. 
                return true;
            default:
                return true;
        }
    }
}
