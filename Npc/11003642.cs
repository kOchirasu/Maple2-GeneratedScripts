using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003642: Jacqueline
/// </summary>
public class _11003642 : NpcScript {
    internal _11003642(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109121007009134$ 
                // - I feel like a diamond in a toilet...
                return true;
            case 10:
                // $script:1109121007009135$ 
                // - Who are you?
                switch (selection) {
                    // $script:1109121007009136$
                    // - Um... What are you doing up here?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109121007009137$ 
                // - Yes, yes, I know. A beauty like mine doesn't belong in a disgusting place like this.
                switch (selection) {
                    // $script:1109121007009138$
                    // - That's not quite what I meant...
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109121007009139$ 
                // - Still, I have a job to do. Tell the boss that I said, "Twinkle, twinkle, little star."
                switch (selection) {
                    // $script:1109121007009140$
                    // - Oh, you're one of ours?
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:1109121007009141$ 
                // - I understand why you're so confused. I'm way too gorgeous for this kind of work! I should've become a model or an actress. Even waitressing would be better than this.
                return true;
            default:
                return true;
        }
    }
}
