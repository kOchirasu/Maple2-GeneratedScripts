using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003645: Mario
/// </summary>
public class _11003645 : NpcScript {
    internal _11003645(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109121007009164$ 
                // - Hm... Interesting.
                return true;
            case 10:
                // $script:1109121007009165$ 
                // - Ah, $MyPCName$. You're just on time.
                switch (selection) {
                    // $script:1109121007009166$
                    // - You were expecting me?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109121007009167$ 
                // - Based on your past travel patterns, current wind pressure readings, and my horoscope for today, I predicted a 96.9% chance that you would drop by.
                switch (selection) {
                    // $script:1109121007009168$
                    // - That's amazing.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109121007009169$ 
                // - Anyway, how do you like my disguise?
                switch (selection) {
                    // $script:1109121007009170$
                    // - It's okay, I guess?
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:1109121007009171$ 
                // - I see. This is perhaps the greatest disguise I've ever designed, and you say such things...
                switch (selection) {
                    // $script:1109121007009172$
                    // - Um... Do you have a message for me?
                    case 0:
                        Id = 14;
                        return false;
                }
                return true;
            case 14:
                // $script:1109121007009173$ 
                // - Oh, yes, good point. Let's see... "Sunshine. Ocean. Wind."
                switch (selection) {
                    // $script:1109121007009174$
                    // - See you later.
                    case 0:
                        Id = 15;
                        return false;
                }
                return true;
            case 15:
                // $script:1109121007009175$ 
                // - According to my research, you will indeed see me again. But it will be sooner than you think...
                return true;
            default:
                return true;
        }
    }
}
