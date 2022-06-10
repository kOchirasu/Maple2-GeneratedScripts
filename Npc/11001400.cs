using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001400: Martino
/// </summary>
public class _11001400 : NpcScript {
    internal _11001400(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217193307005400$ 
                // - What brings you here? C'mon, let's hear it!
                return true;
            case 30:
                // $script:1228164407005736$ 
                // - A high salary is good, but there are other important factors when choosing a job. Comfort, for instance. And safety... I've made a terrible mistake...
                switch (selection) {
                    // $script:1228164407005737$
                    // - What's wrong?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1228164407005738$ 
                // - Where do I begin?! How about the fact that I can't get out of this death trap!
                return true;
            default:
                return true;
        }
    }
}
