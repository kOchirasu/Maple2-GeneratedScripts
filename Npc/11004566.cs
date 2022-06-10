using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004566: Pathos
/// </summary>
public class _11004566 : NpcScript {
    internal _11004566(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0220211107014544$ 
                // - Ah... 
                return true;
            case 10:
                // $script:0220211107014545$ 
                // - Huh? 
                // $script:0220211107014546$ 
                // - I have nothing to say to you. We can work out our differences in the ring. 
                return true;
            default:
                return true;
        }
    }
}
