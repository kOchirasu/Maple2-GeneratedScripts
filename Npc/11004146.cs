using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004146: Mint
/// </summary>
public class _11004146 : NpcScript {
    internal _11004146(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010563$ 
                // - Mm? Are you here to see little old me?
                return true;
            case 10:
                // $script:0806025707010564$ 
                // - Hello! It's another beautiful day in Royale Park, wouldn't you say?
                return true;
            default:
                return true;
        }
    }
}
