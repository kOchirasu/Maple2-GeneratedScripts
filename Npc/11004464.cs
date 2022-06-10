using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004464: Richmonde Defender
/// </summary>
public class _11004464 : NpcScript {
    internal _11004464(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012087$ 
                // - Huh? You don't look like a refugee.
                return true;
            case 10:
                // $script:1227192907012088$ 
                // - Huh? You don't look like a refugee.
                switch (selection) {
                    // $script:1227192907012089$
                    // - I have come from the distant land of Maple World.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012090$ 
                // - Never heard of it. Look, just keep your head down and try not to get caught in the crossfire.
                return true;
            default:
                return true;
        }
    }
}
