using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003633: Anton
/// </summary>
public class _11003633 : NpcScript {
    internal _11003633(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109121007009025$ 
                // - Goods for sale! Get your goods at various prices! 
                return true;
            case 10:
                // $script:1109121007009026$ 
                // - Knick-knacks for sale! I've also got paddywhacks! 
                switch (selection) {
                    // $script:1109121007009027$
                    // - Not interested.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:1109121007009028$
                    // - You're no ordinary peddler...
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 11:
                // $script:1109121007009029$ 
                // - Heh! That was a test, $MyPCName$. And you failed. 
                switch (selection) {
                    // $script:1109121007009030$
                    // - You know me?
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109121007009031$ 
                // - Our mutual friend sent you, didn't she? Tell her, "the cuckoo bird goes caw caw." 
                switch (selection) {
                    // $script:1109121007009032$
                    // - What does that even mean?
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:1109121007009033$ 
                // - Ahem! Pardon me, $male:sir,female:ma'am$, but if you're not buying anything, please make way for paying customers. 
                return true;
            default:
                return true;
        }
    }
}
