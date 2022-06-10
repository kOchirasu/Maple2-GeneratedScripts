using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000223: Morris
/// </summary>
public class _11000223 : NpcScript {
    internal _11000223(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000973$ 
                // - Are you here to talk to me? But why?
                return true;
            case 20:
                // $script:0831180407000975$ 
                // - I don't understand women. It feels like they're always changing their minds. 
                return true;
            default:
                return true;
        }
    }
}
