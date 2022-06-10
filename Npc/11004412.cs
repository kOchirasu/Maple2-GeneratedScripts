using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004412: Mason
/// </summary>
public class _11004412 : NpcScript {
    internal _11004412(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1113161307011841$ 
                // - It is time my order stood with the rest of the empire.
                return true;
            case 10:
                // $script:1113161307011842$ 
                // - Whatever challenges this new land has in store for us, let them come. I will show them my true power.
                return true;
            default:
                return true;
        }
    }
}
