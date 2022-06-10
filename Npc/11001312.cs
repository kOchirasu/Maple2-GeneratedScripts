using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001312: Teddy
/// </summary>
public class _11001312 : NpcScript {
    internal _11001312(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005031$ 
                // - Glory to the empress!
                return true;
            case 30:
                // $script:1227194507005669$ 
                // - No matter how long these missions get, the guard is impervious to fatigue!
                //   <font color="#909090">(There are deep bags under his eyes.)</font> 
                // $script:1227194507005670$ 
                // - Okay, I admit, I'm a <i>tiny</i> bit tired. I just haven't gotten used to my new quarters. I miss... Well, I have my reasons for being tired, okay? 
                switch (selection) {
                    // $script:1227194507005671$
                    // - Such as...?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1227194507005672$ 
                // - Please don't ask. I... I don't want to get into it.
                return true;
            default:
                return true;
        }
    }
}
