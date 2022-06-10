using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004480: Throin
/// </summary>
public class _11004480 : NpcScript {
    internal _11004480(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012205$ 
                // - Yikes! You startled me. I... I didn't really expect another person to just walk up to me in a place like this.
                return true;
            case 10:
                // $script:1227192907012206$ 
                // - Yikes! You startled me. I... I didn't really expect another person to just walk up to me in a place like this.
                // $script:1227192907012207$ 
                // - See this tree? I thought it was some kind of mechane at first. But all of my tests show that this is, in fact, a living plant.
                // $script:1227192907012208$ 
                // - Those cogwheels are actually leaves. Eventually they'll fall off and the tree will grow new ones. I'm still trying to wrap my head around the ecosystem here...
                // $script:1227192907012209$ 
                // - If my report is convincing enough, maybe Dr. $npcName:11004492[gender:0]$ will authorize a permanent research camp here.
                switch (selection) {
                    // $script:0114163707012710$
                    // - I'm sure it'll happen.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0114163707012711$ 
                // - I just want to lose myself in my research!
                return true;
            default:
                return true;
        }
    }
}
