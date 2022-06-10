using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003089: Orde
/// </summary>
public class _11003089 : NpcScript {
    internal _11003089(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0207122607007932$ 
                // - It's hot! Too hot! Even the air-conditioning spell isn't helping.
                return true;
            case 10:
                // $script:0207122607007933$ 
                // - Going from cold to hot so quick is not good for your health. Messes up your skin! And our skin is important for mages... helps us sense mana better.
                return true;
            default:
                return true;
        }
    }
}
