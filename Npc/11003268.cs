using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003268: Ladin
/// </summary>
public class _11003268 : NpcScript {
    internal _11003268(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008218$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0403155707008219$ 
                // - After the Blue Lapenta broke, top scholars from across the world descended on $map:02000026$. Ultimately, I am confident that it will be an alchemist to uncover the secrets of the Land of Darkness and the Shadow World.
                return true;
            default:
                return true;
        }
    }
}
