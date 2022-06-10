using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004406: Frey
/// </summary>
public class _11004406 : NpcScript {
    internal _11004406(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1113161307011829$ 
                // - What is it?
                return true;
            case 10:
                // $script:1113161307011830$ 
                // - This turn of events bodes ill. I think it's time my cadets redoubled their training.
                return true;
            default:
                return true;
        }
    }
}
