using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001672: Junta
/// </summary>
public class _11001672 : NpcScript {
    internal _11001672(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0711210007006722$ 
                // - You have something to say to me?
                return true;
            case 30:
                // $script:0727223007006893$ 
                // - They've pushed us all the way back to $map:63000029$...
                switch (selection) {
                    // $script:0727223007006894$
                    // - What's our next move?
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0727223007006895$ 
                // - I thought we could handle this on our own, but there are too many of them. We have no choice but to report the situation to the master. He will know what to do.
                return true;
            default:
                return true;
        }
    }
}
