using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001396: Navila
/// </summary>
public class _11001396 : NpcScript {
    internal _11001396(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217193307005396$ 
                // - What's wrong?
                return true;
            case 30:
                // $script:1226235907005592$ 
                // - The ruins... These diseases... They all broke out around... No, the timeline doesn't fit.
                switch (selection) {
                    // $script:1226235907005593$
                    // - What are you mumbling about?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1226235907005594$ 
                // - Ah, yes? Can I help you?
                switch (selection) {
                    // $script:1226235907005595$
                    // - You look like you've got a lot on your mind.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1226235907005596$ 
                // - Yes, you're right. I'm trying to figure some things out. And you're interrupting me.
                switch (selection) {
                    // $script:1226235907005597$
                    // - Oops! I didn't mean to.
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:1226235907005598$ 
                // - Good.
                return true;
            case 40:
                // $script:1227015507005608$ 
                // - This is all my fault...
                return true;
            case 50:
                // $script:0201104007005866$ 
                // - I won't be so arrogant or impatient ever again. I'll try to be careful from now on. Thank you for your help, $MyPCName$.
                return true;
            default:
                return true;
        }
    }
}
