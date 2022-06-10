using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003513: Latisha
/// </summary>
public class _11003513 : NpcScript {
    internal _11003513(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0817044507008806$ 
                // - What brings you here?
                return true;
            case 30:
                // $script:0817044507008809$ 
                // - What brings you here?
                switch (selection) {
                    // $script:0817044507008810$
                    // - Tell me about the five auras.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0817044507008811$ 
                // - The Vayar live in the mountains to the northeast. Break a Vayar apart, and you'll get some Steadfast Will. It isn't easy...
                switch (selection) {
                    // $script:0817044507008812$
                    // - Tell me about the Vayar.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0817044507008813$ 
                // - They're solid. And tough. Magic doesn't work on them, either. You've got to fight them up close!
                return true;
            default:
                return true;
        }
    }
}
