using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003517: Ashim
/// </summary>
public class _11003517 : NpcScript {
    internal _11003517(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0817044507008848$ 
                // - What? 
                return true;
            case 30:
                // $script:0817044507008851$ 
                // - What? 
                switch (selection) {
                    // $script:0817044507008852$
                    // - Tell me about the five auras.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0817044507008853$ 
                // - Aur-what? Look, I just want to finish my exam and grab some grub. 
                return true;
            default:
                return true;
        }
    }
}
