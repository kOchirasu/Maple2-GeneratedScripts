using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001546: Zabeth
/// </summary>
public class _11001546 : NpcScript {
    internal _11001546(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0516130207006114$ 
                // - What're you looking at? You got something to say?
                return true;
            case 10:
                // $script:0531170907006244$ 
                // - <font color="#909090">($npc:11001546[gender:0]$ scowls at you.)</font>
                switch (selection) {
                    // $script:0531170907006245$
                    // - Um... Can I help you?
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:0531170907006246$ 
                // - Go back to your corner and practice. I'm busy.
                return true;
            default:
                return true;
        }
    }
}
