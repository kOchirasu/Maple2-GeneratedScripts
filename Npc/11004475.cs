using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004475: Sealon
/// </summary>
public class _11004475 : NpcScript {
    internal _11004475(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012161$ 
                // - You here for the big land grab? 
                return true;
            case 10:
                // $script:1227192907012162$ 
                // - You here for the big land grab? 
                // $script:1227192907012163$ 
                // - $map:02020041$ is the first city in the new world. This place is gonna be a hotbed of development once we kick the other riffraff off this continent! 
                // $script:1227192907012164$ 
                // - Sure, it seems like a shaky investment <i>now</i>, but just you wait! Any land you buy here today will be worth ten times as much a year from now! 
                return true;
            default:
                return true;
        }
    }
}
