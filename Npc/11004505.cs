using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004505: Mannstad Sentry
/// </summary>
public class _11004505 : NpcScript {
    internal _11004505(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1228182607012429$ 
                // - Identify yourself! 
                return true;
            case 10:
                // $script:1228182607012430$ 
                // - Identify yourself! 
                switch (selection) {
                    // $script:1228182607012431$
                    // - Whoa, there. I'm a friend!
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1228182607012432$ 
                // - Hey, you're that outlander. I read a report on you. 
                // $script:1228182607012433$ 
                // - Sorry if I seem on edge. Not all of the outlanders have been as... helpful as you. 
                return true;
            default:
                return true;
        }
    }
}
