using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001498: Dunba
/// </summary>
public class _11001498 : NpcScript {
    internal _11001498(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0118150907005828$ 
                // - You know I outrank you, right? Hah hah! 
                return true;
            case 30:
                // $script:0118150907005831$ 
                // - Don't just stare at your food, eat it! So rude. 
                switch (selection) {
                    // $script:0120170607005853$
                    // - Tell me about your past.
                    case 0:
                        Id = 0; // TODO: 31 | 32
                        return false;
                }
                return true;
            case 31:
                // $script:0120170607005854$ functionID=1 
                // - If not for him... 
                return true;
            case 32:
                // $script:0120170607005855$ 
                // - I'm sorry, but I just want to eat right now. 
                return true;
            case 40:
                // $script:0127102807005857$ 
                // - Don't just stare at your food, eat it! So rude. 
                return true;
            default:
                return true;
        }
    }
}
