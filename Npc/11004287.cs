using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004287: Alberto Bean
/// </summary>
public class _11004287 : NpcScript {
    internal _11004287(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0220212507014570$ 
                // - Nice to meet you.
                return true;
            case 10:
                // $script:0220212507014571$ 
                // - You just might be up to the Queen Bean Rumble.
                // $script:0220212507014572$ 
                // - I do think you shall be an amusement for Her Highness.
                return true;
            default:
                return true;
        }
    }
}
