using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003515: Chipo
/// </summary>
public class _11003515 : NpcScript {
    internal _11003515(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0817044507008831$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0817044507008834$ 
                // - Can I help you?
                switch (selection) {
                    // $script:0817044507008835$
                    // - Tell me about the five auras.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0817044507008836$ 
                // - The placas live in the desert to the southeast. If you defeat them while they're dancing, you can obtain their Essences of Dance.
                switch (selection) {
                    // $script:0817044507008837$
                    // - Tell me about placas.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0817044507008838$ 
                // - They look gentle, but I wouldn't touch them. Their thorns are sharp! 
                // $script:0817044507008839$ 
                // - They're supposed to be good dancers, but I haven't seen it myself. They're not dancing all the time, you see. Do you think they prefer upbeat music?
                return true;
            default:
                return true;
        }
    }
}
