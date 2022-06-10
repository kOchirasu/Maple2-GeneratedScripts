using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001109: Viata
/// </summary>
public class _11001109 : NpcScript {
    internal _11001109(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0908154107003727$ 
                // - Hey! Good to see you again!
                return true;
            case 30:
                // $script:0908154107003730$ 
                // - Mm? You're the one who saved me from $map:03009023$, aren't you?
                switch (selection) {
                    // $script:0907172207003699$
                    // - Why are you still in the Land of Darkness?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0908154107003731$ 
                // - That's... I want to stay with $npcName:11000614[gender:0]$. I never want to be separated from him again. 
                return true;
            default:
                return true;
        }
    }
}
