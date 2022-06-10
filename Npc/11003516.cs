using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003516: Jahari
/// </summary>
public class _11003516 : NpcScript {
    internal _11003516(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0817044507008840$ 
                // - What? 
                return true;
            case 30:
                // $script:0817044507008843$ 
                // - What? 
                switch (selection) {
                    // $script:0817044507008844$
                    // - Tell me about the five auras.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0817044507008845$ 
                // - Lycaos live in the wastelands to the southwest. You can capture them to get their Enduring Health. 
                switch (selection) {
                    // $script:0817044507008846$
                    // - Tell me about lycaos.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0817044507008847$ 
                // - They're not easy to capture. If you don't tie them up or stun them, they'll slip away. 
                return true;
            default:
                return true;
        }
    }
}
