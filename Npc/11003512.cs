using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003512: Babatundey
/// </summary>
public class _11003512 : NpcScript {
    internal _11003512(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0817044507008802$ 
                // - Need something?
                return true;
            case 30:
                // $script:0817044507008803$ 
                // - The boss's word is good. What more do you need?
                switch (selection) {
                    // $script:0817044507008804$
                    // - Tell me about the exam.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0817044507008805$ 
                // - Humans can't do anything alone. If you can't figure it out, ask someone to help you.
                return true;
            default:
                return true;
        }
    }
}
