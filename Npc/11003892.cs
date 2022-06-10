using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003892: Turka
/// </summary>
public class _11003892 : NpcScript {
    internal _11003892(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0515102507009942$ 
                // - Hehehe...
                return true;
            case 20:
                // $script:0515102507009943$ 
                // - Hehehe... So you've come to me. Does that mean you're finally ready to accept my terms?
                return true;
            case 30:
                // $script:0515102507009944$ 
                // - Who are you to give me orders?
                return true;
            default:
                return true;
        }
    }
}
