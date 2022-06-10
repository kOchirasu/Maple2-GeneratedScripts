using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001195: Pat
/// </summary>
public class _11001195 : NpcScript {
    internal _11001195(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1016202007004194$ 
                // - This place is dry, hot, and unbearably loud. It is absolutely <i>the worst</i>.  
                return true;
            case 30:
                // $script:1016202007004197$ 
                // - I must've been out of my mind when I agreed to come here. Hmm? And just who are you supposed to be? Wait, did my wise little owl send here? 
                switch (selection) {
                    // $script:1016202007004198$
                    // - Your what?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1016202007004200$ 
                // - I'm talking about my beautiful muse! The brains behind our Educational programming, Joanna, of course. <i>Whooo</i>~ else? 
                switch (selection) {
                    // $script:1016210507004215$
                    // - But what was that with the owl thing?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1016202007004201$ 
                // - Owls are smart. It's just a cute nickname, honey. Get over yourself.  
                return true;
            default:
                return true;
        }
    }
}
