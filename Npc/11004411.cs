using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004411: Nairin
/// </summary>
public class _11004411 : NpcScript {
    internal _11004411(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1113161307011839$ 
                // - Would you like to take on a mission for Green Hoods? 
                return true;
            case 10:
                // $script:1113161307011840$ 
                // - A brand new world, chock full of new data to analyze! 
                return true;
            default:
                return true;
        }
    }
}
