using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004525: Timid Soldieretto
/// </summary>
public class _11004525 : NpcScript {
    internal _11004525(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0103163407012506$ 
                // - Beeep... Beeep...
                return true;
            case 10:
                // $script:0103163407012507$ 
                // - Beep... Beep... Beep...
                // $script:0103163407012508$ 
                // - Beep... Beep... Beeep! Bee...
                return true;
            default:
                return true;
        }
    }
}
