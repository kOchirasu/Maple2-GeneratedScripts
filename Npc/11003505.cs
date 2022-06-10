using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003505: Rieve
/// </summary>
public class _11003505 : NpcScript {
    internal _11003505(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0816160115009002$ 
                // - See the hungry $itemPlural:61000002$ over there? This place is getting crowded because of them...
                return true;
            case 30:
                // $script:0816160115009003$ 
                // - You're way too green to cut it in Team Mushroom.
                return true;
            case 40:
                // $script:0816160115009004$ 
                // - Tamed monsters are called 'combat pets.' Don't forget that, 'cause it might be on the test!
                return true;
            default:
                return true;
        }
    }
}
